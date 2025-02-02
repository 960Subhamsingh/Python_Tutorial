from tkinter import *

root = Tk()
root.title("Change Background Color On Click Using Python Source Code")
width = 600
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================METHODS========================================
def changeToRed():
    root.config(bg="red")
    Form.config(bg='red')

def changeToBlue():
    root.config(bg="blue")
    Form.config(bg='blue')

def changeToGreen():
    root.config(bg="green")
    Form.config(bg='green')

#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text="Change Background Color On Click Using Python Source Code", font=('arial', 15))
lbl_title.pack(fill=X)



#==============================BUTTON WIDGETS=================================
btn_red = Button(Form, text="Red", font=('arial', 20),command=changeToRed)
btn_red.grid(pady=0, row=0, column=0)
btn_blue = Button(Form, text="Blue", font=('arial', 20),command=changeToBlue)
btn_blue.grid(pady=0,  padx=10 ,row=0, column=1)
btn_green = Button(Form, text="Green", font=('arial', 20),command=changeToGreen)
btn_green.grid(pady=0,  padx=10 ,row=0, column=2)






