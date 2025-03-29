# Open a file in read mode
with open("example.txt", "r+") as file:
    file.write("Hello, this is a test file.")
    content = file.read()
    
    print(content)