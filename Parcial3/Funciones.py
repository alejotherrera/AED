


from tkinter import *
from tkinter import messagebox as MessageBox

def test():
    MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

root = Tk()

Button(root, text = "Puto toca aca", command=test).pack()

root.mainloop()