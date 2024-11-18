#problem no 1
name=input("Enter your name :")
print(f"Good Mening ,{ name }")
#problem no 2
letter='''Dear <|name|>,
you are selected!
date:<|date|>'''
name=input("Enter your name :")
date=input("Enter date :")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)
#problem no 3
names="He is a good boy"
print(names.find("a"))
# problem no 3
names="He is a  good  boy"
print(names.replace ("  "," "))
#problem no 4
letter="Dear Laiba,\n\tThis python course is nice.\nThanks!"
print(letter)