from tkinter import *
from Self_Destruct_Function import SelfDestruct

window = Tk()
window.title = "The button"

button = Button(window,
                text="Self Destruct",
                command=SelfDestruct)



window.mainloop()