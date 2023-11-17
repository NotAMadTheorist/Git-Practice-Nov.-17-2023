from tkinter import *

window = Tk()
window.title = "The button"
window.geometry("800x800")

answer = "yes"


def SelfDestruct():
    if answer == "yes":
        print("Boom!")
        label.config(text="Boom!")
    else:
        return
    

button = Button(window,
                text="Self Destruct",
                command=SelfDestruct)

label = Label(window,
              text=f"Please don't.")


button.pack()
label.pack()

window.mainloop()