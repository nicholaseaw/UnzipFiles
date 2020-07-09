import os, zipfile

dir_name = r"C:\Users\Desktop\"
extension = ".zip"

# change directory from working dir to dir with files
os.chdir(dir_name) 

#loop through items in dir
for item in os.listdir(dir_name):

#check for ".zip" extension
    if item.endswith(extension):
#get full path of files
        file_name = os.path.abspath(item) 
#create zipfile object
        zip_ref = zipfile.ZipFile(file_name)
#extract file to dir 
        zip_ref.extractall(dir_name)
 #close file
        zip_ref.close()
