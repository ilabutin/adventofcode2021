import sys

previous = sys.maxsize
count = 0
with open('input.txt') as file:
    for line in file:
        current = int(line)
        if current > previous:
            count = count + 1
        previous = current
        
print(count)
        
        