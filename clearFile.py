#Clear file
import os

fileList = os.listdir(os.getcwd())

file_name = raw_input("Enter file name (including proper capitalization and file extension): ")
if file_name in fileList:
    writeFile = open(file_name, 'w+')

    for item in writeFile:
        writeFile.write("")
    writeFile.close()
    print "All data in %s has been cleared......." %(file_name)
else:
    print "File not found........."
