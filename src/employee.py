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
        LabelDepartment = Label(FormFrame, text="Department", font=("arial", 11, 'bold'), bg="white")
        LabelDepartment.grid(row=0, column=0, padx=9, sticky=W)
        ComboDepartment = ttk.Combobox(FormFrame, textvariable=self.DepartmentVariable, font=("arial", 11), width=25, state="readonly")
        ComboDepartment["value"] = ('Select Department', 'HR', 'Software', 'Engineering', 'R&D', 'Management')
        ComboDepartment.current(0)
        ComboDepartment.grid(row=0, column=1, padx=9, pady=10, sticky=W)
        # Employee Name
        LabelName = Label(FormFrame, font=("arial", 11, 'bold'), text="Name:", bg="white")
        LabelName.grid(row=0, column=2, sticky=W, padx=9, pady=7)
        TextName = ttk.Entry(FormFrame, textvariable=self.NameVariable, width=25, font=("arial", 11))
        TextName.grid(row=0, column=3, padx=9, pady=7)
        # Designition
        LabelDesignition = Label(FormFrame, font=("arial", 11, 'bold'), text="Designition:", bg="white")
        LabelDesignition.grid(row=1, column=0, sticky=W, padx=9, pady=7)
        TextDesignition = ttk.Entry(FormFrame, textvariable=self.DesignationVariable, width=25, font=("arial", 11))
        TextDesignition.grid(row=1, column=1, padx=9, pady=7)
        # Email
        LabelEmail = Label(FormFrame, font=("arial", 11, 'bold'), text="Email:", bg="white")
        LabelEmail.grid(row=1, column=2, sticky=W, padx=9, pady=7)
        TextEmail = ttk.Entry(FormFrame, textvariable=self.EmailVariable, width=25, font=("arial", 11))
        TextEmail.grid(row=1, column=3, padx=9, pady=7)
        # Address
        LabelAddress = Label(FormFrame, font=("arial", 11, 'bold'), text="Address:", bg="white")
        LabelAddress.grid(row=2, column=0, sticky=W, padx=9, pady=7)
        TextAddress = ttk.Entry(FormFrame, textvariable=self.AddressVariable, width=25, font=("arial", 11))
        TextAddress.grid(row=2, column=1, padx=9, pady=7)
        # MaritalStatus
        LabelMaritalStatus = Label(FormFrame, font=("arial", 11, 'bold'), text="Marital Status:", bg="white")
        LabelMaritalStatus.grid(row=2, column=2, sticky=W, padx=9, pady=7)
        ComboMaritalStatus = ttk.Combobox(FormFrame, textvariable=self.MarriedVariable, font=("arial", 11), width=25, state="readonly")
        ComboMaritalStatus["value"] = ('Married', 'Unmarried')
        ComboMaritalStatus.current(0)
        ComboMaritalStatus.grid(row=2, column=3, padx=9, pady=10, sticky=W)
        # Date of Birth
        LabelDateOfBirth = Label(FormFrame, font=("arial", 11, 'bold'), text="Date of birth:", bg="white")
        LabelDateOfBirth.grid(row=3, column=0, sticky=W, padx=9, pady=7)
        TextDateOfBirth = ttk.Entry(FormFrame, textvariable=self.DOBVariable, width=25, font=("arial", 11))
        TextDateOfBirth.grid(row=3, column=1, padx=9, pady=7)
        # Date of joining
        LabelDateOfJoining = Label(FormFrame, font=("arial", 11, 'bold'), text="Date of Joining:", bg="white")
        LabelDateOfJoining.grid(row=3, column=2, sticky=W, padx=9, pady=7)
        TextDateOfJoining = ttk.Entry(FormFrame, textvariable=self.DOJVariable, width=25, font=("arial", 11))
        TextDateOfJoining.grid(row=3, column=3, padx=9, pady=7)
        # ID Proof
        ComboIDProof = ttk.Combobox(FormFrame, textvariable=self.IDProofComboVariable, font=("arial", 11), width=15, state="readonly")
        ComboIDProof["value"] = ('Select ID Proof', 'PAN CARD', 'ADHAR CARD', 'DRIVING LICENSE')
        ComboIDProof.current(0)
        ComboIDProof.grid(row=4, column=0, padx=9, pady=10, sticky=W)
        TextIDProof = ttk.Entry(FormFrame, textvariable=self.IDProofVariable, width=25, font=("arial", 11))
        TextIDProof.grid(row=4, column=1, padx=9, pady=7)
        # Gender
        LabelGender = Label(FormFrame, font=("arial", 11, 'bold'), text="Gender:", bg="white")
        LabelGender.grid(row=4, column=2, sticky=W, padx=9, pady=7)
        ComboGender = ttk.Combobox(FormFrame, textvariable=self.GenderVariable, font=("arial", 11), width=25, state="readonly")
        ComboGender["value"] = ('Male', 'Female', 'Other')
        ComboGender.current(0)
        ComboGender.grid(row=4, column=3, padx=9, pady=10, sticky=W)
        # Phone number
        LabelPhoneNumber = Label(FormFrame, font=("arial", 11, 'bold'), text="Phone No:", bg="white")
        LabelPhoneNumber.grid(row=0, column=4, sticky=W, padx=9, pady=7)
        TextPhoneNumber = ttk.Entry(FormFrame, textvariable=self.PhoneVariable, width=25, font=("arial", 11))
        TextPhoneNumber.grid(row=0, column=5, padx=9, pady=7)
        # Country
        LabelCountry = Label(FormFrame, font=("arial", 11, 'bold'), text="Country:", bg="white")
        LabelCountry.grid(row=1, column=4, sticky=W, padx=9, pady=7)
        TextCountry = ttk.Entry(FormFrame, textvariable=self.CountryVariable, width=25, font=("arial", 11))
        TextCountry.grid(row=1, column=5, padx=9, pady=7)
        # CTC
        LabelCTC = Label(FormFrame, font=("arial", 11, 'bold'), text="CTC:", bg="white")
        LabelCTC.grid(row=2, column=4, sticky=W, padx=9, pady=7)
        TextCTC = ttk.Entry(FormFrame, textvariable=self.SalaryVariable, width=25, font=("arial", 11))
        TextCTC.grid(row=2, column=5, padx=9, pady=7)

        # Button frame
        ButtonFrame = Frame(UpperFrame, bd=2, relief=RIDGE, bg="white")
        ButtonFrame.place(x=1100, y=0, width=205, height=195)

        SaveBtn = Button(ButtonFrame, text="Save", command=self.AddData, font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        SaveBtn.grid(row=0, column=0, padx=5, pady=5)
        UpdateBtn = Button(ButtonFrame, text="Update", command=self.UpdateData, font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        UpdateBtn.grid(row=1, column=0, padx=5, pady=5)
        DeleteBtn = Button(ButtonFrame, text="Delete", command=self.DeleteData, font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        DeleteBtn.grid(row=2, column=0, padx=5, pady=5)
        ResetBtn = Button(ButtonFrame, text="Reset", command=self.ResetFields, font=("arial", 15, 'bold'), width=15, bg="blue", fg="white")
        ResetBtn.grid(row=3, column=0, padx=5, pady=5)

        # Lower frame
        LowerFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Information Table", font=("times new roman", 11, 'bold'), fg="red")
        LowerFrame.place(x=10, y=245, width=1320, height=360)

        SearchFrame = Frame(LowerFrame, bd=0, relief=RIDGE, bg="white")
        SearchFrame.place(x=10, y=0, width=1300, height=40)
        SearchByLabel = Label(SearchFrame, font=("arial", 11, 'bold'), text="Search by:", fg="white", bg="white")
        SearchByLabel.grid(row=0, column=0, sticky=W, padx=1)
        self.SearchByVariable = StringVar()
        SearchComboBox = ttk.Combobox(SearchFrame, textvariable=self.SearchByVariable, font=("arial", 11, 'bold'), width=21, state="readonly")
        SearchComboBox["value"] = ("Select Option", "Phone", "ID_Proof")
        SearchComboBox.current(0)
        SearchComboBox.grid(row=0, column=1, padx=5, pady=1, sticky=W)
        self.SearchTextVariable = StringVar()
        SearchTextBox = ttk.Entry(SearchFrame, textvariable=self.SearchTextVariable, width=50, font=("arial", 11, 'bold'))
        SearchTextBox.grid(row=0, column=2, padx=5, pady=1, sticky=W)
        SearchBtn = Button(SearchFrame, text="Search", command=self.SearchData, font=("arial", 11, 'bold'), width=30, bg="blue", fg="white")
        SearchBtn.grid(row=0, column=3, padx=10, pady=1)
        ShowAllBtn = Button(SearchFrame, text="Show All", command=self.FetchData, font=("arial", 11, 'bold'), width=30, bg="blue", fg="white")
        ShowAllBtn.grid(row=0, column=4, padx=10, pady=1)

        # Employee Table frame
        TableFrame = Frame(LowerFrame, bd=3, relief=RIDGE)
        TableFrame.place(x=10, y=40, width=1300, height=290)

        ScrollX = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        ScrollY = ttk.Scrollbar(TableFrame, orient=VERTICAL)
        self.EmployeeTable = ttk.Treeview(TableFrame, column=("dep", "name", "degi", "email", "address", "marriedstatus", "dob", "doj", "idproofcomb", "idproof", "gender", "phone", "country", "salary"), xscrollcommand=ScrollX.set, yscrollcommand=ScrollY.set)
        ScrollX.pack(side=BOTTOM, fill=X)
        ScrollY.pack(side=RIGHT, fill=Y)
        ScrollX.config(command=self.EmployeeTable.xview)
        ScrollY.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("dep", text="Department")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("degi", text="Designation")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("marriedstatus", text="Marital Status")
        self.EmployeeTable.heading("dob", text="DOB")
        self.EmployeeTable.heading("doj", text="DOJ")
        self.EmployeeTable.heading("idproofcomb", text="ID Proof Type")
        self.EmployeeTable.heading("idproof", text="ID Proof")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("phone", text="Phone")
        self.EmployeeTable.heading("country", text="Country")
        self.EmployeeTable.heading("salary", text="Salary")
        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("dep", width=150)
        self.EmployeeTable.column("name", width=150)
        self.EmployeeTable.column("degi", width=150)
        self.EmployeeTable.column("email", width=150)
        self.EmployeeTable.column("address", width=150)
        self.EmployeeTable.column("marriedstatus", width=150)
        self.EmployeeTable.column("dob", width=150)
        self.EmployeeTable.column("doj", width=150)
        self.EmployeeTable.column("idproofcomb", width=150)
        self.EmployeeTable.column("idproof", width=150)
        self.EmployeeTable.column("gender", width=150)
        self.EmployeeTable.column("phone", width=150)
        self.EmployeeTable.column("country", width=150)
        self.EmployeeTable.column("salary", width=150)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        
        self.EmployeeTable.bind("<ButtonRelease>", self.GetCursor)
        
        self.FetchData()

    # AddData method to add data to the database
    def AddData(self):
        if self.IDProofComboVariable.get() == "" or self.IDProofVariable.get() == "" or self.NameVariable.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="EMS")
                with conn.cursor() as cursor:
                    sql = """
                        INSERT INTO EMS (Department, Name, Designation, Email, Address, MarriedStatus, DOB, DOJ, ID_Proof_Type, ID_Proof, Gender, Phone, Country, Salary)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, (
                        self.DepartmentVariable.get(), self.NameVariable.get(), self.DesignationVariable.get(),
                        self.EmailVariable.get(), self.AddressVariable.get(), self.MarriedVariable.get(),
                        self.DOBVariable.get(), self.DOJVariable.get(), self.IDProofComboVariable.get(),
                        self.IDProofVariable.get(), self.GenderVariable.get(), self.PhoneVariable.get(),
                        self.CountryVariable.get(), self.SalaryVariable.get()
                    ))
                    conn.commit()
                messagebox.showinfo("Success", "Employee has been added", parent=self.root)
                self.FetchData()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)
            finally:
                conn.close()

    # FetchData method to fetch data from the database and display it in the table
    def FetchData(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="EMS")
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM EMS")
                rows = cursor.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                    conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)
        finally:
            conn.close()

    # GetCursor method to get data from the table when a row is clicked
    def GetCursor(self, event=""):
        cursor_row = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(cursor_row)
        data = content['values']
        self.DepartmentVariable.set(data[0])
        self.NameVariable.set(data[1])
        self.DesignationVariable.set(data[2])
        self.EmailVariable.set(data[3])
        self.AddressVariable.set(data[4])
        self.MarriedVariable.set(data[5])
        self.DOBVariable.set(data[6])
        self.DOJVariable.set(data[7])
        self.IDProofComboVariable.set(data[8])
        self.IDProofVariable.set(data[9])
        self.GenderVariable.set(data[10])
        self.PhoneVariable.set(data[11])
        self.CountryVariable.set(data[12])
        self.SalaryVariable.set(data[13])

    # UpdateData method to update data in the database
    def UpdateData(self):
        if self.IDProofComboVariable.get() == "" or self.IDProofVariable.get() == "" or self.NameVariable.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="EMS")
                with conn.cursor() as cursor:
                    sql = """
                        UPDATE EMS
                        SET Department=%s, Name=%s, Designation=%s, Email=%s, Address=%s, MarriedStatus=%s, DOB=%s, DOJ=%s, ID_Proof_Type=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s
                        WHERE ID_Proof=%s
                    """
                    cursor.execute(sql, (
                        self.DepartmentVariable.get(), self.NameVariable.get(), self.DesignationVariable.get(),
                        self.EmailVariable.get(), self.AddressVariable.get(), self.MarriedVariable.get(),
                        self.DOBVariable.get(), self.DOJVariable.get(), self.IDProofComboVariable.get(),
                        self.GenderVariable.get(), self.PhoneVariable.get(), self.CountryVariable.get(),
                        self.SalaryVariable.get(), self.IDProofVariable.get()
                    ))
                    conn.commit()
                messagebox.showinfo("Success", "Employee details have been updated", parent=self.root)
                self.FetchData()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)
            finally:
                conn.close()

    # DeleteData method to delete data from the database
    def DeleteData(self):
        if self.IDProofVariable.get() == "":
            messagebox.showerror("Error", "ID Proof is required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="EMS")
                with conn.cursor() as cursor:
                    sql = "DELETE FROM EMS WHERE ID_Proof=%s"
                    cursor.execute(sql, (self.IDProofVariable.get(),))
                    conn.commit()
                messagebox.showinfo("Success", "Employee details have been deleted", parent=self.root)
                self.FetchData()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)
            finally:
                conn.close()

    # ResetFields method to clear all input fields
    def ResetFields(self):
        self.DepartmentVariable.set("")
        self.NameVariable.set("")
        self.DesignationVariable.set("")
        self.EmailVariable.set("")
        self.AddressVariable.set("")
        self.MarriedVariable.set("")
        self.DOBVariable.set("")
        self.DOJVariable.set("")
        self.IDProofVariable.set("")
        self.IDProofComboVariable.set("")
        self.GenderVariable.set("")
        self.PhoneVariable.set("")
        self.CountryVariable.set("")
        self.SalaryVariable.set("")

    # SearchData method to search data in the database
    def SearchData(self):
        if self.SearchByVariable.get() == "Select Option" or self.SearchTextVariable.get() == "":
            messagebox.showerror("Error", "Select a search option and enter search text")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="EMS")
                with conn.cursor() as cursor:
                    sql = f"SELECT * FROM EMS WHERE {self.SearchByVariable.get()} LIKE %s"
                    cursor.execute(sql, (f"%{self.SearchTextVariable.get()}%",))
                    rows = cursor.fetchall()
                    if len(rows) != 0:
                        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                        for row in rows:
                            self.EmployeeTable.insert('', END, values=row)
                        conn.commit()
                    else:
                        messagebox.showinfo("Info", "No matching records found", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)
            finally:
                conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
