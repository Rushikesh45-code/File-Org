import os

folder = input("Enter file path :- ")

# files = os.listdir(folder)

for root, subfolder, files in os.walk(folder):
    print(f"Current folder is {root}")
    
    for file in files:
        print(f"File -> {file}")
    
    for name in subfolder:
        print(f"Folder -> {name}")
