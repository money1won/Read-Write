# Brief showing of how a file reads, writes, and appends

file = open("test.txt","w")

file.write("Hello World")
file.write("This is our new text file")
file.write("New line")
file.write("This is our new text file")

file.close

# Reads the entire file
# file = open("test.txt", "r")
# print(file.read())

# Reads only the line selected
file = open("test.txt", "r")
print(file.readline())

file.close

# Will add onto the end of the file currently existing
file = open("test.txt","a")
file.write("END")
file.close()

file = open("test.txt", "r")
print(file.read())