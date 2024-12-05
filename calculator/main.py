
from tkinter import * 

def click_button(number):
  global equation_text
  equation_text=equation_text+str(number)
  equation_label.set(equation_text)
  
def equal():
  try:
    global equation_text
    total=str(eval(equation_text))
    equation_label.set(total)

    equation_text=total

  except ZeroDivisionError:
    equation_label.set("arithmetic error")
    equation_text=""  
  except SyntaxError:
    equation_label.set("syntax error")
    equation_text=""  

def clear():
  global equation_text
  equation_label.set("")
  equation_text=""

window= Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""
equation_label=StringVar()

label= Label(window,textvariable=equation_label,font=("consolas",20),bg="white",width=24,height=2)
label.pack()
frame=Frame(window)
frame.pack()
# fg="black",
button1=Button(frame,text="1",bg="white",width=9,height=4, font=35,command=lambda:click_button(1))
button1.grid(row=0,column=0)

button2=Button(frame,text="2",bg="white",width=9,height=4, font=35,command=lambda:click_button(2))
button2.grid(row=0,column=1)

button3=Button(frame,text="3",bg="white",width=9,height=4, font=35,command=lambda:click_button(3))
button3.grid(row=0,column=2)

button4=Button(frame,text="4",bg="white",width=9,height=4, font=35,command=lambda:click_button(4))
button4.grid(row=1,column=0)

button5=Button(frame,text="5",bg="white",width=9,height=4, font=35,command=lambda:click_button(5))
button5.grid(row=1,column=1)

button6=Button(frame,text="6",bg="white",width=9,height=4, font=35,command=lambda:click_button(6))
button6.grid(row=1,column=2)

button7=Button(frame,text="7",bg="white",width=9,height=4, font=35,command=lambda:click_button(7))
button7.grid(row=2,column=0)

button8=Button(frame,text="8",bg="white",width=9,height=4, font=35,command=lambda:click_button(8))
button8.grid(row=2,column=1)

button9=Button(frame,text="9",bg="white",width=9,height=4, font=35,command=lambda:click_button(9))
button9.grid(row=2,column=2)

button0=Button(frame,text="0",bg="white",width=9,height=4, font=35,command=lambda:click_button(0))
button0.grid(row=3,column=0)

plus=Button(frame,text="+",bg="white",width=9,height=4, font=35,command=lambda:click_button('+'))
plus.grid(row=0,column=3)

sub=Button(frame,text="-",bg="white",width=9,height=4, font=35,command=lambda:click_button('-'))
sub.grid(row=1,column=3)

mul=Button(frame,text="x",bg="white",width=9,height=4, font=35,command=lambda:click_button('*'))
mul.grid(row=2,column=3)

devide=Button(frame,text="/",bg="white",width=9,height=4, font=35,command=lambda:click_button('/'))
devide.grid(row=3,column=3)

equal=Button(frame,text="=",bg="white",width=9,height=4, font=35,command=equal)
equal.grid(row=3,column=2)

decimal=Button(frame,text=".",bg="white",width=9,height=4, font=35,command=lambda:click_button('.'))
decimal.grid(row=3,column=1)

clear=Button(window,text="clear",bg="white",width=12,height=4, font=35,command=clear)
clear.pack()

window.mainloop()