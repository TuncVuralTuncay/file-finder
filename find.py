import os

rootdir = "."
skip_dirs = []
def findViaExtensionName():
    ext = str(input("Enter extension name : "))

    print("Finding please wait.....")
    os.system("cd /")
    for subdir, dirs, files in os.walk(rootdir, topdown=True):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if file.endswith(ext):
                filepath = subdir + os.sep + file
                try:
                    print()
                    print(f"{filepath}")
                except UnicodeDecodeError as e:
                    print(f"Error: {e} in {filepath}")
def findViaFileName():
    name = str(input("Enter file name : "))

    print("Finding please wait.....")
    os.system("cd /")
    for subdir, dirs, files in os.walk(rootdir, topdown=True):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for file in files:
            if name in file :
                filepath = subdir + os.sep + file
                print()
                print(f"{filepath}")
            else:
                """nothing"""
a = int(input("Find file via extension name : 1 \nFind file via name : 2 \nWaiting your command : "))

if(a == 1):
    findViaExtensionName()
if(a == 2):
    findViaFileName()
else:
    exit()

