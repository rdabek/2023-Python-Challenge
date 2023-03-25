def createFile(filePath: str, content: str):
    with open(filePath, 'w') as file:
        file.write(content)

def toUpperCaseInFile(filePath: str, chars: list[str]):
    with open(filePath, 'r') as file:
        fileData = file.read()
    
    def toUpper(c: chr):
        if ord(c) > ord('z') or ord(c) < ord('a'):
            raise ValueError("Invalid input")
        return chr(ord(c) + (ord('A')-ord('a')))

    for c in chars:
        fileData = fileData.replace(c, toUpper(c))
    
    with open(filePath, 'w') as file:
        file.write(fileData)