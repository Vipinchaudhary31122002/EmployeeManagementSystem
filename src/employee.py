from tkinter import *
from tkinter import ttk

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("EmployeeManagementSystem")
        
        # Label
        LabelTitle = Label(self.root, text="Employee Management System", font=("times new roman", 37, 'bold'), fg="darkblue", bg="white")
        LabelTitle.place(x=0, y=0, width=1366, height=65)

        # Main frame
        MainFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        MainFrame.place(x=10, y=70, width=1346, height=625)

        # Upper frame
        UpperFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Data Form", font=("times new roman", 11, 'bold'), fg="red")
        UpperFrame.place(x=10, y=10, width=1320, height=270)

        # Label and Entry field in Upper frame
        # Department Name
        LabelDepartment = Label(UpperFrame, text="Department", font=("arial", 11, 'bold'), bg="white")
        LabelDepartment.grid(row=0, column=0, padx=2, sticky=W)
        ComboDepartment = ttk.Combobox(UpperFrame, font=("arial", 11), width=21, state="readonly")
        ComboDepartment["value"] = ('Select Department', 'HR', 'Software', 'Engineering', 'R&D', 'Management')
        ComboDepartment.current(0)
        ComboDepartment.grid(row=0, column =1, padx=2, pady=10, sticky=W)
        # Employee Name
        LabelName = Label(UpperFrame, font=("arial", 11, 'bold'), text="Name:", bg="white")
        LabelName.grid(row=0, column=2, sticky=W, padx=2, pady=7)
        TextName=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextName.grid(row=0, column=3, padx=2, pady=7)
        # Designition
        LabelDesignition = Label(UpperFrame, font=("arial", 11, 'bold'), text="Designition:", bg="white")
        LabelDesignition.grid(row=1, column=0, sticky=W, padx=2, pady=7)
        TextDesignition=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextDesignition.grid(row=1, column=1, padx=2, pady=7)
        # Email
        LabelEmail = Label(UpperFrame, font=("arial", 11, 'bold'), text="Email:", bg="white")
        LabelEmail.grid(row=1, column=2, sticky=W, padx=2, pady=7)
        TextEmail=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextEmail.grid(row=1, column=3, padx=2, pady=7)
        # Address
        LabelAddress = Label(UpperFrame, font=("arial", 11, 'bold'), text="Address:", bg="white")
        LabelAddress.grid(row=2, column=0, sticky=W, padx=2, pady=7)
        TextAddress=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextAddress.grid(row=2, column=1, padx=2, pady=7)
        # MaritalStatus
        LabelMaritalStatus = Label(UpperFrame, font=("arial", 11, 'bold'), text="Marital Status:", bg="white")
        LabelMaritalStatus.grid(row=2, column=2, sticky=W, padx=2, pady=7)
        ComboMaritalStatus = ttk.Combobox(UpperFrame, font=("arial", 11), width=21, state="readonly")
        ComboMaritalStatus["value"] = ('Married','Unmarried')
        ComboMaritalStatus.current(0)
        ComboMaritalStatus.grid(row=2, column=3, padx=2, pady=10, sticky=W)
        # Date of Birth
        LabelDateOfBirth = Label(UpperFrame, font=("arial", 11, 'bold'), text="Date of birth:", bg="white")
        LabelDateOfBirth.grid(row=3, column=0, sticky=W, padx=2, pady=7)
        TextDateOfBirth=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextDateOfBirth.grid(row=3, column=1, padx=2, pady=7)
        # Date of joining
        LabelDateOfJoining = Label(UpperFrame, font=("arial", 11, 'bold'), text="Date of Joining:", bg="white")
        LabelDateOfJoining.grid(row=3, column=2, sticky=W, padx=2, pady=7)
        TextDateOfJoining=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextDateOfJoining.grid(row=3, column=3, padx=2, pady=7)
        # ID Proof
        ComboIDProof = ttk.Combobox(UpperFrame, font=("arial", 11), width=15, state="readonly")
        ComboIDProof["value"] = ('Select ID Proof','PAN CARD', 'ADHAR CARD', 'DRIVING LICENSE')
        ComboIDProof.current(0)
        ComboIDProof.grid(row=4, column=0, padx=2, pady=10, sticky=W)
        TextIDProof=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextIDProof.grid(row=4, column=1, padx=2, pady=7)
        # Gender
        LabelGender = Label(UpperFrame, font=("arial", 11, 'bold'), text="Gender:", bg="white")
        LabelGender.grid(row=4, column=2, sticky=W, padx=2, pady=7)
        ComboGender = ttk.Combobox(UpperFrame, font=("arial", 11), width=21, state="readonly")
        ComboGender["value"] = ('Male','Female', 'Other')
        ComboGender.current(0)
        ComboGender.grid(row=4, column=3, padx=2, pady=10, sticky=W)
        # Phone number
        LabelPhoneNumber = Label(UpperFrame, font=("arial", 11, 'bold'), text="Phone No:", bg="white")
        LabelPhoneNumber.grid(row=0, column=4, sticky=W, padx=2, pady=7)
        TextPhoneNumber=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextPhoneNumber.grid(row=0, column=5, padx=2, pady=7)
        # Country
        LabelCountry = Label(UpperFrame, font=("arial", 11, 'bold'), text="Country:", bg="white")
        LabelCountry.grid(row=1, column=4, sticky=W, padx=2, pady=7)
        TextCountry=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextCountry.grid(row=1, column=5, padx=2, pady=7)
        # CTC
        LabelCTC = Label(UpperFrame, font=("arial", 11, 'bold'), text="CTC:", bg="white")
        LabelCTC.grid(row=2, column=4, sticky=W, padx=2, pady=7)
        TextCTC=ttk.Entry(UpperFrame, width=22, font=("arial", 11))
        TextCTC.grid(row=2, column=5, padx=2, pady=7)

        # Button frame
        ButtonFrame = Frame(UpperFrame, bd=2, relief=RIDGE, bg="white")
        ButtonFrame.place(x=1000, y=20, width=185, height=195)

        AddBtn = Button(ButtonFrame, text="Save", font=("arial", 15, 'bold'), width=13, bg="blue", fg="white")
        AddBtn.grid(row=0, column=0, padx=5, pady=5)
        UpdateBtn = Button(ButtonFrame, text="Update", font=("arial", 15, 'bold'), width=13, bg="blue", fg="white")
        UpdateBtn.grid(row=1, column=0, padx=5, pady=5)
        DeleteBtn = Button(ButtonFrame, text="Delete", font=("arial", 15, 'bold'), width=13, bg="blue", fg="white")
        DeleteBtn.grid(row=2, column=0, padx=5, pady=5)
        ResetBtn = Button(ButtonFrame, text="Reset", font=("arial", 15, 'bold'), width=13, bg="blue", fg="white")
        ResetBtn.grid(row=3, column=0, padx=5, pady=5)

        # Lower frame
        LowerFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Information Table", font=("times new roman", 11, 'bold'), fg="red")
        LowerFrame.place(x=10, y=285, width=1320, height=325)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    # root.resizable(True, True) 
    root.mainloop()

