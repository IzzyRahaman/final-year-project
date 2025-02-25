import sys

args = sys.argv

f1_name = args[1]
f2_name = args[2]

f1 = open(f1_name, 'r')
f2 = open(f2_name, 'r')

f1_data = filter(lambda x : len(x) > 0, f1.read().split())
f2_data = filter(lambda x : len(x) > 0, f2.read().split())

f1.close()
f2.close()

print "==========================================="
print "File #1 length: ", len(f1_data)
print "File #2 length: ", len(f2_data)
print "File #1 and #2 differ at lines (1-indexed): "

min_length = min(len(f1_data), len(f2_data))
count = 0
for idx in range(0, min_length):
  if f1_data[idx] != f2_data[idx]:
    count += 1
    print f1_data[idx], " differs from ", f2_data[idx], " at line ", idx


print "Differ in ", count, " places"
print "=========================================="
