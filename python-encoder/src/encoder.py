'''
Created on Mar 21, 2015

@author: school
'''

import sys 
from OrganizingList import OrganizingList
from FifoQueue import FifoQueue
from math import log, floor, ceil


def read_and_clean_files(file_obj):
    contents = file_obj.read().split()
    return filter(lambda x : len(x) > 0, contents)

def int_to_bin(num, num_bits = 8):
    ans = ''
    result = [0] * num_bits
    counter = 0
    temp = int(num)
    while temp: 
        result[counter] = temp % 2
        temp = temp / 2
        counter += 1
    for bit in result:
        ans = str(bit) + ans 
    #print num, " ", ans
    return ans

def bin_to_int(num):
    ans = 0
    counter = 1
    for n in reversed(num):
        ans += (counter * int(n))
        counter *= 2
    return ans
    

if __name__ == '__main__':
    
    arguments = sys.argv
    image_file_name = arguments[1]
    secret_file_name = arguments[2]
    output_file_name = arguments[3]
    as_integer_name = arguments[4] 
    stream_file_name = arguments[5]
   
    image_file = open(image_file_name, 'r')
    secret_file = open(secret_file_name, 'r')
    output_file = open(output_file_name, 'w')
    as_integer_file = open(as_integer_name, 'w')
    stream_fl = open(stream_file_name, 'w')
    
    image_data = read_and_clean_files(image_file)
    secret_data = read_and_clean_files(secret_file)
    image_file.close()
    secret_file.close()
    
    image_storage = FifoQueue()
    secret_storage = FifoQueue()
    organizing_list = OrganizingList(4)
    intended_output = ''
    integer_output = []
    
    for data in image_data:
        image_storage.insert(int(data))
        
    for data in secret_data:
        secret_storage.insert(int(data))
        
    print "Number of image data points ", image_storage.size()
    counter = 0
    for vq_index in image_data:
        counter += 1
        list_index = organizing_list.insert(vq_index)
        if not list_index:
            to_add = '00' + str(int_to_bin(vq_index))
        else:
            secret_bit = secret_storage.get()
            if secret_bit:
                if list_index == 1:
                    to_add = (str(secret_bit) + '1')
                else:
                    num_bits = int(floor(log(list_index, 2)))
                    to_add = str(secret_bit) + ('0' * num_bits) + str(int_to_bin(list_index, num_bits + 1))
            else:
                if list_index == 1:
                    to_add = str(secret_bit) + '11'
                else:
                    num_bits = int(floor(log(list_index, 2)))
                    to_add = str(secret_bit) + '1' + ('0' * num_bits) + str(int_to_bin(list_index, num_bits + 1))
        intended_output += to_add
        integer_output.append(to_add)
            
    print "Number processed ", counter
    print "Streams produced ", len(integer_output)
    
    for bit in intended_output:
        output_file.write(bit + '\n')
    
    output_file.close()
    
    for num in integer_output:
        stream_fl.write(num + '\n')
        as_integer_file.write(str(bin_to_int(num)) + '\n')
    as_integer_file.close()
    
    
    
    
    
    