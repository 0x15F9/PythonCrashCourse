with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("-"*20)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())

print("-"*20)

list = []
with open('learning_python.txt') as file_object:
    for line in file_object:
        list.append(line)

for line in list:
    print(line.strip())