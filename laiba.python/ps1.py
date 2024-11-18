# problem no 1
print('''
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')
# problem no 2
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# problem no 3
import os

# Specify the directory path; use '.' for the current directory
directory_path = '.'

# List all files and folders in the specified directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
