from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x700+0+0")
        self.root.title("EmployeeManagementSystem")
        
        # Label
        lbl_title = Label(self.root, text="Employee Management System", font=("times new roman", 37, 'bold'), fg="darkblue", bg="white")
        lbl_title.place(x=0, y=0, width=1500, height=50)

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
