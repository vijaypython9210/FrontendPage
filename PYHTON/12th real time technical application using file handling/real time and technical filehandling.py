from shutil import copyfile
sourcefile = input("Enter source file name: ")
destinationfile = input("Enter destination file name: ")
copyfile(sourcefile, destinationfile)
print("File copied successfully!")
c = open("destinationfile.txt", "r")
print(c.read())
c.close()
print()
print()
