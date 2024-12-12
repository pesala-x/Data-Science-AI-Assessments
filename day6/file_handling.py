# file1 = open("day6\my_file.txt")

file1 = open("day6\my_file.txt", "r")

content = file1.read()

print(content,type(content))

file1.close()
