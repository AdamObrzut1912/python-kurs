import os
print("current workind directory", os.getcwd())

files = os.listdir()
print(files)

files = os.listdir(".")
print(files)

files = os.listdir("./chalanges")
print(files)


files = os.listdir("../egzaminy wszystkie")
print(files)