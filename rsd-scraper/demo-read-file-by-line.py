# Using readlines()

# files of the RSD8 Symposium
# https://rsdsymposium.org/category/rsd8/
#

filename = 'rsd8-file-list.txt'


file = open('rsd8-file-list.txt', 'r')
lines = file.readlines()

count = 0
# Strips the newline character
for line in lines:
    count += 1
    print("Line {}: {}".format(count, line.strip()))
    print(line)    
    
    
