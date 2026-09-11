inputfile=open("C:\\Users\\jsapn\\Desktop\\PythonAutomation_swapna\\myfile\\inputFile.txt","r")
#print(inputfile.read())
for line in inputfile:
    linesplit=line.split()
    if len(linesplit) > 2 and linesplit[2] == "P":
        print(line)
inputfile.close()

print("******************")
#my version using with functionality
"""
filepath='C:\\Users\\jsapn\\Desktop\\PythonAutomation_swapna\\myfile\\DOCUMENTS\\inputFile.txt'
with open(filepath,'r') as file:
    #data =file.read()
    for line in file:
        linesplit=line.split()
        if len(linesplit) > 2 and linesplit[2] == "P":
            print(line)
"""



         