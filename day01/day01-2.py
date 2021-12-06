count = 0
with open('input.txt') as file:
    lines = file.readlines()
    for (index, value) in enumerate(lines):
        if index < 3:
            continue
        if (int(value) > int(lines[index - 3])):
            count = count + 1
        
print(count)
        
        