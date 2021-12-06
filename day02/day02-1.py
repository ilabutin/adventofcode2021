position = 0
depth = 0
with open('input.txt') as file:
    for line in file:
        if line[0] == 'f':
            position += int(line[8:])
        if line[0] == 'u':
            depth -= int(line[3:])
        if line[0] == 'd':
            depth += int(line[5:])
           
print(position * depth)
