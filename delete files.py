import os
folderPath=input("input folder path ")
files=os.listdir((folderPath))

folderPath2=input("enter second folder path from which u want files to be deleted")
files2=os.listdir((folderPath2))

for file in files:
    if file in files2:
        commonfile=os.path.join(folderPath2,file)
        os.remove(commonfile)
    
    

