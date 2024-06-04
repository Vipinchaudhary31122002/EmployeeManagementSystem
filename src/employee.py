from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("EmployeeManagementSystem")

        # text variable which store input taken through input fields
        self.DepartmentVariable = StringVar()
        self.NameVariable = StringVar()
        self.DesignationVariable = StringVar()
        self.EmailVariable = StringVar()
        self.AddressVariable = StringVar()
        self.MarriedVariable = StringVar()
        self.DOBVariable = StringVar()
        self.DOJVariable = StringVar()
        self.IDProofVariable = StringVar()
        self.IDProofComboVariable = StringVar()
        self.GenderVariable = StringVar()
        self.PhoneVariable = StringVar()
        self.CountryVariable = StringVar()
        self.SalaryVariable = StringVar()
        
        # Label
        LabelTitle = Label(self.root, text="Employee Management System", font=("times new roman", 37, 'bold'), fg="darkblue", bg="white")
        LabelTitle.place(x=0, y=0, width=1366, height=65)

        # Main frame
        MainFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        MainFrame.place(x=10, y=70, width=1346, height=625)

        # Upper frame
        UpperFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Data Form", font=("times new roman", 11, 'bold'), fg="red")
        UpperFrame.place(x=10, y=10, width=1320, height=225)

        # Form from
        FormFrame = Frame(UpperFrame, bd=2, relief=RIDGE, bg="white")
        FormFrame.place(x=10, y=0, width=1080, height=195)

        # Label and Entry field in Upper frame
        # Department Name
        LabelDepartment = Label(FormFrame,text="Department", font=("arial", 11, 'bold'), bg="white")
        LabelDepartment.grid(row=0, column=0, padx=9, sticky=W)
        ComboDepartment = ttk.Combobox(FormFrame, textvariable = self.DepartmentVariable, font=("arial", 11), width=25, state="readonly")
        ComboDepartment["value"] = ('Select Department', 'HR', 'Software', 'Engineering', 'R&D', 'Management')
        ComboDepartment.current(0)
        ComboDepartment.grid(row=0, column =1, padx=9, pady=10, sticky=W)
        # Employee Name
        LabelName = Label(FormFrame, font=("arial", 11, 'bold'), text="Name:", bg="white")
        LabelName.grid(row=0, column=2, sticky=W, padx=9, pady=7)
        TextName=ttk.Entry(FormFrame, textvariable = self.NameVariable, width=25, font=("arial", 11))
        TextName.grid(row=0, column=3, padx=9, pady=7)
        # Designition
        LabelDesignition = Label(FormFrame, font=("arial", 11, 'bold'), text="Designition:", bg="white")
        LabelDesignition.grid(row=1, column=0, sticky=W, padx=9, pady=7)
        TextDesignition=ttk.Entry(FormFrame, textvariable = self.DesignationVariable, width=25, font=("arial", 11))
        TextDesignition.grid(row=1, column=1, padx=9, pady=7)
        # Email
        LabelEmail = Label(FormFrame, font=("arial", 11, 'bold'), text="Email:", bg="white")
        LabelEmail.grid(row=1, column=2, sticky=W, padx=9, pady=7)
        TextEmail=ttk.Entry(FormFrame, textvariable = self.EmailVariable, width=25, font=("arial", 11))
        TextEmail.grid(row=1, column=3, padx=9, pady=7)
        # Address
        LabelAddress = Label(FormFrame, font=("arial", 11, 'bold'), text="Address:", bg="white")
        LabelAddress.grid(row=2, column=0, sticky=W, padx=9, pady=7)
        TextAddress=ttk.Entry(FormFrame, textvariable = self.AddressVariable, width=25, font=("arial", 11))
        TextAddress.grid(row=2, column=1, padx=9, pady=7)
        # MaritalStatus
        LabelMaritalStatus = Label(FormFrame, font=("arial", 11, 'bold'), text="Marital Status:", bg="white")
        LabelMaritalStatus.grid(row=2, column=2, sticky=W, padx=9, pady=7)
        ComboMaritalStatus = ttk.Combobox(FormFrame, textvariable = self.MarriedVariable, font=("arial", 11), width=25, state="readonly")
        ComboMaritalStatus["value"] = ('Married','Unmarried')
        ComboMaritalStatus.current(0)
        ComboMaritalStatus.grid(row=2, column=3, padx=9, pady=10, sticky=W)
        # Date of Birth
        LabelDateOfBirth = Label(FormFrame, font=("arial", 11, 'bold'), text="Date of birth:", bg="white")
        LabelDateOfBirth.grid(row=3, column=0, sticky=W, padx=9, pady=7)
        TextDateOfBirth=ttk.Entry(FormFrame, textvariable = self.DOBVariable, width=25, font=("arial", 11))
        TextDateOfBirth.grid(row=3, column=1, padx=9, pady=7)
        # Date of joining
        LabelDateOfJoining = Label(FormFrame, font=("arial", 11, 'bold'), text="Date of Joining:", bg="white")
        LabelDateOfJoining.grid(row=3, column=2, sticky=W, padx=9, pady=7)
        TextDateOfJoining=ttk.Entry(FormFrame, textvariable = self.DOJVariable, width=25, font=("arial", 11))
        TextDateOfJoining.grid(row=3, column=3, padx=9, pady=7)
        # ID Proof
        ComboIDProof = ttk.Combobox(FormFrame, textvariable = self.IDProofComboVariable, font=("arial", 11), width=15, state="readonly")
        ComboIDProof["value"] = ('Select ID Proof','PAN CARD', 'ADHAR CARD', 'DRIVING LICENSE')
        ComboIDProof.current(0)
        ComboIDProof.grid(row=4, column=0, padx=9, pady=10, sticky=W)
        TextIDProof=ttk.Entry(FormFrame, textvariable = self.IDProofVariable, width=25, font=("arial", 11))
        TextIDProof.grid(row=4, column=1, padx=9, pady=7)
        # Gender
        LabelGender = Label(FormFrame, font=("arial", 11, 'bold'), text="Gender:", bg="white")
        LabelGender.grid(row=4, column=2, sticky=W, padx=9, pady=7)
        ComboGender = ttk.Combobox(FormFrame,textvariable = self.GenderVariable, font=("arial", 11), width=25, state="readonly")
        ComboGender["value"] = ('Male','Female', 'Other')
        ComboGender.current(0)
        ComboGender.grid(row=4, column=3, padx=9, pady=10, sticky=W)
        # Phone number
        LabelPhoneNumber = Label(FormFrame, font=("arial", 11, 'bold'), text="Phone No:", bg="white")
        LabelPhoneNumber.grid(row=0, column=4, sticky=W, padx=9, pady=7)
        TextPhoneNumber=ttk.Entry(FormFrame, textvariable = self.PhoneVariable, width=25, font=("arial", 11))
        TextPhoneNumber.grid(row=0, column=5, padx=9, pady=7)
        # Country
        LabelCountry = Label(FormFrame, font=("arial", 11, 'bold'), text="Country:", bg="white")
        LabelCountry.grid(row=1, column=4, sticky=W, padx=9, pady=7)
        TextCountry=ttk.Entry(FormFrame, textvariable = self.CountryVariable, width=25, font=("arial", 11))
        TextCountry.grid(row=1, column=5, padx=9, pady=7)
        # CTC
        LabelCTC = Label(FormFrame, font=("arial", 11, 'bold'), text="CTC:", bg="white")
        LabelCTC.grid(row=2, column=4, sticky=W, padx=9, pady=7)
        TextCTC=ttk.Entry(FormFrame, textvariable = self.SalaryVariable, width=25, font=("arial", 11))
        TextCTC.grid(row=2, column=5, padx=9, pady=7)

        # Button frame
        ButtonFrame = Frame(UpperFrame, bd=2, relief=RIDGE, bg="white")
        ButtonFrame.place(x=1100, y=0, width=205, height=195)

        AddBtn = Button(ButtonFrame, text="Save", command = self.AddData, font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        AddBtn.grid(row=0, column=0, padx=5, pady=5)
        UpdateBtn = Button(ButtonFrame, text="Update", font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        UpdateBtn.grid(row=1, column=0, padx=5, pady=5)
        DeleteBtn = Button(ButtonFrame, text="Delete", font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        DeleteBtn.grid(row=2, column=0, padx=5, pady=5)
        ResetBtn = Button(ButtonFrame, text="Reset", font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        ResetBtn.grid(row=3, column=0, padx=5, pady=5)

        # Lower frame
        LowerFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Information Table", font=("times new roman", 11, 'bold'), fg="red")
        LowerFrame.place(x=10, y=240, width=1320, height=370)
        # search frame
        SearchFrame = Frame(LowerFrame, bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=10, y=0, width=1300, height=40)
        SearchBy = Label(SearchFrame, font=("arial", 11, "bold"), text="Search By:", fg="black", bg="white")
        SearchBy.grid(row=0, column=0, sticky=W, padx=10, pady=3)
        # search combobox
        ComboSearch = ttk.Combobox(SearchFrame, font=("arial", 11), width=21, state="readonly")
        ComboSearch["value"] = ('Select Option','Phone no', 'id_proof')
        ComboSearch.current(0)
        ComboSearch.grid(row=0, column=1, padx=10, sticky=W, pady=3)
        # search entry field
        SearchEntry = ttk.Entry(SearchFrame, width=50, font=("arial", 11, "bold"))
        SearchEntry.grid(row=0, column=2, padx=10, pady=3)
        # Search button
        SearchButton = Button(SearchFrame, text="Search", width=30, font=("arial", 11, "bold"), fg="white", bg="red")
        SearchButton.grid(row=0, column=3, padx=10 , pady=3)
        # Showall button
        ShowAllButton = Button(SearchFrame, text="Show all", width=30, font=("arial", 11, "bold"), fg="white", bg="red")
        ShowAllButton.grid(row=0, column=4, padx=10 , pady=3)

        # Employee Table
        EmployeeTableFrame = Frame(LowerFrame, bd=3, relief=RIDGE, bg="white")
        EmployeeTableFrame.place(x=10, y=45, width=1300, height=300)
        ScrollX = ttk.Scrollbar(EmployeeTableFrame, orient=HORIZONTAL)
        ScrollY = ttk.Scrollbar(EmployeeTableFrame, orient=VERTICAL)
        self.EmployeeTable = ttk.Treeview(EmployeeTableFrame, columns=("Dep", "Name", "Desig", "Email", "Add", "Married", "DOB", "DOJ", "IDProof", "IDProofNo", "Gender", "Phone", "Country", "Salary",), xscrollcommand=ScrollX.set, yscrollcommand=ScrollY.set)
        ScrollX.pack(side=BOTTOM, fill=X)
        ScrollY.pack(side=RIGHT, fill=Y)
        ScrollX.config(command=self.EmployeeTable.xview)
        ScrollY.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("Dep", text="Department Name")
        self.EmployeeTable.heading("Name", text="Employee Name")
        self.EmployeeTable.heading("Desig", text="Designation")
        self.EmployeeTable.heading("Email", text="Email")
        self.EmployeeTable.heading("Add", text="Address")
        self.EmployeeTable.heading("Married", text="Marital Status")
        self.EmployeeTable.heading("DOB", text="Date of Birth")
        self.EmployeeTable.heading("DOJ", text="Date of Joining")
        self.EmployeeTable.heading("IDProof", text="ID Proof")
        self.EmployeeTable.heading("IDProofNo", text="ID Proof Number")
        self.EmployeeTable.heading("Gender", text="Gender")
        self.EmployeeTable.heading("Phone", text="Phone number")
        self.EmployeeTable.heading("Country", text="Country")
        self.EmployeeTable.heading("Salary", text="Salary")
        
        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.column("Dep", width=150)
        self.EmployeeTable.column("Name", width=150)
        self.EmployeeTable.column("Desig", width=150)
        self.EmployeeTable.column("Email", width=150)
        self.EmployeeTable.column("Add", width=150)
        self.EmployeeTable.column("Married", width=150)
        self.EmployeeTable.column("DOB", width=150)
        self.EmployeeTable.column("DOJ", width=150)
        self.EmployeeTable.column("IDProof", width=150)
        self.EmployeeTable.column("IDProofNo", width=150)
        self.EmployeeTable.column("Gender", width=150)
        self.EmployeeTable.column("Phone", width=150)
        self.EmployeeTable.column("Country", width=150)
        self.EmployeeTable.column("Salary", width=150)
        self.EmployeeTable.pack(fill=BOTH, expand=1)

    # function declaration for create, update, clear and delete data
    def AddData(self):
        if self.IDProofComboVariable.get() == "" or self.IDProofVariable.get() == "" or self.NameVariable.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="EMS")
                with conn.cursor() as cursor:
                    sql = """
                        INSERT INTO EMS (Department, Name, Designation, Email, Address, MarriedStatus, DOB, DOJ, ID_Proof, ID_Proof_Type, Gender, Phone, Country, Salary) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, (
                        self.DepartmentVariable.get(), self.NameVariable.get(), self.DesignationVariable.get(),
                        self.EmailVariable.get(), self.AddressVariable.get(), self.MarriedVariable.get(),
                        self.DOBVariable.get(), self.DOJVariable.get(), self.IDProofVariable.get(),
                        self.IDProofComboVariable.get(), self.GenderVariable.get(), self.PhoneVariable.get(),
                        self.CountryVariable.get(), self.SalaryVariable.get()
                    ))
                    conn.commit()
                messagebox.showinfo("Success", "Employee data has been added", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)
            finally:
                conn.close()


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

