position = 0
depth = 0
aim = 0
with open('input.txt') as file:
    for line in file:
        if line[0] == 'f':
            position += int(line[8:])
            depth += aim * int(line[8:])
        if line[0] == 'u':
            aim -= int(line[3:])
        if line[0] == 'd':
            aim += int(line[5:])
           
print(position * depth)
