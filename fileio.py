str = "I am Java Developer, learning Python"

# Ist way to write file
# with open("test.txt", "w") as f:
#     f.write(str)

# IInd way to write file
# f = open("test.txt", "w")
# f.write(str)
# f.close() 


# Appending to a file
with open("test.txt", "a") as f:
    f.write("\nPython has multiple libraries to work with")

# Reading a file
with open("test.txt", "r") as f:
    s = f.read()
    print(s)