from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("EmployeeManagementSystem")

        # Variables to store input from the input fields
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

        # Title Label
        LabelTitle = Label(self.root, text="Employee Management System", font=("times new roman", 37, 'bold'), fg="darkblue", bg="white")
        LabelTitle.place(x=0, y=0, width=1366, height=65)

        # Main frame
        MainFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        MainFrame.place(x=10, y=70, width=1346, height=625)

        # Upper frame for the employee data form
        UpperFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Data Form", font=("times new roman", 11, 'bold'), fg="red")
        UpperFrame.place(x=10, y=10, width=1320, height=225)

        # Frame inside the upper frame to hold form elements
        FormFrame = Frame(UpperFrame, bd=2, relief=RIDGE, bg="white")
        FormFrame.place(x=10, y=0, width=1080, height=195)

        # Label and entry for Department
        LabelDepartment = Label(FormFrame, text="Department", font=("arial", 11, 'bold'), bg="white")
        LabelDepartment.grid(row=0, column=0, padx=9, sticky=W)
        ComboDepartment = ttk.Combobox(FormFrame, textvariable=self.DepartmentVariable, font=("arial", 11), width=25, state="readonly")
        ComboDepartment["value"] = ('Select Department', 'HR', 'Software', 'Engineering', 'R&D', 'Management')
        ComboDepartment.current(0)
        ComboDepartment.grid(row=0, column=1, padx=9, pady=10, sticky=W)

        # Label and entry for Employee Name
        LabelName = Label(FormFrame, font=("arial", 11, 'bold'), text="Name:", bg="white")
        LabelName.grid(row=0, column=2, sticky=W, padx=9, pady=7)
        TextName = ttk.Entry(FormFrame, textvariable=self.NameVariable, width=25, font=("arial", 11))
        TextName.grid(row=0, column=3, padx=9, pady=7)

        # Label and entry for Designation
        LabelDesignition = Label(FormFrame, font=("arial", 11, 'bold'), text="Designation:", bg="white")
        LabelDesignition.grid(row=1, column=0, sticky=W, padx=9, pady=7)
        TextDesignition = ttk.Entry(FormFrame, textvariable=self.DesignationVariable, width=25, font=("arial", 11))
        TextDesignition.grid(row=1, column=1, padx=9, pady=7)

        # Label and entry for Email
        LabelEmail = Label(FormFrame, font=("arial", 11, 'bold'), text="Email:", bg="white")
        LabelEmail.grid(row=1, column=2, sticky=W, padx=9, pady=7)
        TextEmail = ttk.Entry(FormFrame, textvariable=self.EmailVariable, width=25, font=("arial", 11))
        TextEmail.grid(row=1, column=3, padx=9, pady=7)

        # Label and entry for Address
        LabelAddress = Label(FormFrame, font=("arial", 11, 'bold'), text="Address:", bg="white")
        LabelAddress.grid(row=2, column=0, sticky=W, padx=9, pady=7)
        TextAddress = ttk.Entry(FormFrame, textvariable=self.AddressVariable, width=25, font=("arial", 11))
        TextAddress.grid(row=2, column=1, padx=9, pady=7)

        # Label and combobox for Marital Status
        LabelMaritalStatus = Label(FormFrame, font=("arial", 11, 'bold'), text="Marital Status:", bg="white")
        LabelMaritalStatus.grid(row=2, column=2, sticky=W, padx=9, pady=7)
        ComboMaritalStatus = ttk.Combobox(FormFrame, textvariable=self.MarriedVariable, font=("arial", 11), width=25, state="readonly")
        ComboMaritalStatus["value"] = ('Married', 'Unmarried')
        ComboMaritalStatus.current(0)
        ComboMaritalStatus.grid(row=2, column=3, padx=9, pady=10, sticky=W)

        # Label and entry for Date of Birth
        LabelDateOfBirth = Label(FormFrame, font=("arial", 11, 'bold'), text="Date of birth:", bg="white")
        LabelDateOfBirth.grid(row=3, column=0, sticky=W, padx=9, pady=7)
        TextDateOfBirth = ttk.Entry(FormFrame, textvariable=self.DOBVariable, width=25, font=("arial", 11))
        TextDateOfBirth.grid(row=3, column=1, padx=9, pady=7)

        # Label and entry for Date of Joining
        LabelDateOfJoining = Label(FormFrame, font=("arial", 11, 'bold'), text="Date of Joining:", bg="white")
        LabelDateOfJoining.grid(row=3, column=2, sticky=W, padx=9, pady=7)
        TextDateOfJoining = ttk.Entry(FormFrame, textvariable=self.DOJVariable, width=25, font=("arial", 11))
        TextDateOfJoining.grid(row=3, column=3, padx=9, pady=7)

        # Combobox for ID Proof Type
        ComboIDProof = ttk.Combobox(FormFrame, textvariable=self.IDProofComboVariable, font=("arial", 11), width=15, state="readonly")
        ComboIDProof["value"] = ('Select ID Proof', 'PAN CARD', 'ADHAR CARD', 'DRIVING LICENSE')
        ComboIDProof.current(0)
        ComboIDProof.grid(row=4, column=0, padx=9, pady=10, sticky=W)

        # Label and entry for ID Proof
        TextIDProof = ttk.Entry(FormFrame, textvariable=self.IDProofVariable, width=25, font=("arial", 11))
        TextIDProof.grid(row=4, column=1, padx=9, pady=7)

        # Label and combobox for Gender
        LabelGender = Label(FormFrame, font=("arial", 11, 'bold'), text="Gender:", bg="white")
        LabelGender.grid(row=4, column=2, sticky=W, padx=9, pady=7)
        ComboGender = ttk.Combobox(FormFrame, textvariable=self.GenderVariable, font=("arial", 11), width=25, state="readonly")
        ComboGender["value"] = ('Male', 'Female', 'Other')
        ComboGender.current(0)
        ComboGender.grid(row=4, column=3, padx=9, pady=10, sticky=W)

        # Label and entry for Phone Number
        LabelPhoneNumber = Label(FormFrame, font=("arial", 11, 'bold'), text="Phone No:", bg="white")
        LabelPhoneNumber.grid(row=0, column=4, sticky=W, padx=9, pady=7)
        TextPhoneNumber = ttk.Entry(FormFrame, textvariable=self.PhoneVariable, width=25, font=("arial", 11))
        TextPhoneNumber.grid(row=0, column=5, padx=9, pady=7)

        # Label and entry for Country
        LabelCountry = Label(FormFrame, font=("arial", 11, 'bold'), text="Country:", bg="white")
        LabelCountry.grid(row=1, column=4, sticky=W, padx=9, pady=7)
        TextCountry = ttk.Entry(FormFrame, textvariable=self.CountryVariable, width=25, font=("arial", 11))
        TextCountry.grid(row=1, column=5, padx=9, pady=7)

        # Label and entry for CTC (Salary)
        LabelCTC = Label(FormFrame, font=("arial", 11, 'bold'), text="CTC:", bg="white")
        LabelCTC.grid(row=2, column=4, sticky=W, padx=9, pady=7)
        TextCTC = ttk.Entry(FormFrame, textvariable=self.SalaryVariable, width=25, font=("arial", 11))
        TextCTC.grid(row=2, column=5, padx=9, pady=7)

        # Button frame
        ButtonFrame = Frame(UpperFrame, bd=2, relief=RIDGE, bg="white")
        ButtonFrame.place(x=1090, y=10, width=210, height=205)

        # Add button
        ButtonAdd = Button(ButtonFrame, text="Save", command=self.add_data, font=("arial", 15, "bold"), width=13, fg="white", bg="blue")
        ButtonAdd.grid(row=0, column=0, padx=1, pady=5)

        # Update button
        ButtonUpdate = Button(ButtonFrame, text="Update", command=self.update_data, font=("arial", 15, "bold"), width=13, fg="white", bg="blue")
        ButtonUpdate.grid(row=1, column=0, padx=1, pady=5)

        # Delete button
        ButtonDelete = Button(ButtonFrame, text="Delete", command=self.delete_data, font=("arial", 15, "bold"), width=13, fg="white", bg="blue")
        ButtonDelete.grid(row=2, column=0, padx=1, pady=5)

        # Clear button
        ButtonClear = Button(ButtonFrame, text="Clear", command=self.reset_data, font=("arial", 15, "bold"), width=13, fg="white", bg="blue")
        ButtonClear.grid(row=3, column=0, padx=1, pady=5)

        # Lower frame for employee information table
        LowerFrame = LabelFrame(MainFrame, bd=2, relief=RIDGE, bg="white", text="Employee Information Table", font=("times new roman", 11, 'bold'), fg="red")
        LowerFrame.place(x=10, y=240, width=1320, height=375)

        # Search frame within lower frame
        SearchFrame = Frame(LowerFrame, bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=10, y=0, width=1290, height=50)

        # Search label
        LabelSearchBy = Label(SearchFrame, font=("arial", 11, 'bold'), text="Search By:", fg="white", bg="red")
        LabelSearchBy.grid(row=0, column=0, sticky=W, padx=5)

        # Combobox for search options
        self.SearchBy = StringVar()
        ComboSearchBy = ttk.Combobox(SearchFrame, textvariable=self.SearchBy, font=("arial", 12), width=18, state="readonly")
        ComboSearchBy["value"] = ("Select Option", "Phone", "IDProof")
        ComboSearchBy.current(0)
        ComboSearchBy.grid(row=0, column=1, sticky=W, padx=5)

        # Entry field for search text
        self.SearchTxt = StringVar()
        TextSearch = ttk.Entry(SearchFrame, textvariable=self.SearchTxt, width=22, font=("arial", 11))
        TextSearch.grid(row=0, column=2, sticky=W, padx=5)

        # Search button
        ButtonSearch = Button(SearchFrame, command=self.search_data, text="Search", font=("arial", 12, "bold"), width=14, fg="white", bg="blue")
        ButtonSearch.grid(row=0, column=3, padx=5)

        # Show All button
        ButtonShowAll = Button(SearchFrame, command=self.fetch_data, text="Show All", font=("arial", 12, "bold"), width=14, fg="white", bg="blue")
        ButtonShowAll.grid(row=0, column=4, padx=5)

        # Table frame
        TableFrame = Frame(LowerFrame, bd=3, relief=RIDGE)
        TableFrame.place(x=0, y=50, width=1290, height=295)

        # Scrollbars for the table
        ScrollX = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        ScrollY = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        # Treeview widget for displaying employee data
        self.employee_table = ttk.Treeview(TableFrame, column=("Department", "Name", "Designition", "Email", "Address", "Married",
                                                               "DOB", "DOJ", "IDProofCombo", "IDProof", "Gender", "Phone", "Country", "Salary"),
                                           xscrollcommand=ScrollX.set, yscrollcommand=ScrollY.set)

        ScrollX.pack(side=BOTTOM, fill=X)
        ScrollY.pack(side=RIGHT, fill=Y)
        ScrollX.config(command=self.employee_table.xview)
        ScrollY.config(command=self.employee_table.yview)

        # Defining headings for each column
        self.employee_table.heading("Department", text="Department")
        self.employee_table.heading("Name", text="Name")
        self.employee_table.heading("Designition", text="Designation")
        self.employee_table.heading("Email", text="Email")
        self.employee_table.heading("Address", text="Address")
        self.employee_table.heading("Married", text="Marital Status")
        self.employee_table.heading("DOB", text="DOB")
        self.employee_table.heading("DOJ", text="DOJ")
        self.employee_table.heading("IDProofCombo", text="ID Proof Type")
        self.employee_table.heading("IDProof", text="ID Proof")
        self.employee_table.heading("Gender", text="Gender")
        self.employee_table.heading("Phone", text="Phone")
        self.employee_table.heading("Country", text="Country")
        self.employee_table.heading("Salary", text="CTC")

        self.employee_table["show"] = "headings"

        # Setting column widths
        self.employee_table.column("Department", width=100)
        self.employee_table.column("Name", width=100)
        self.employee_table.column("Designition", width=100)
        self.employee_table.column("Email", width=100)
        self.employee_table.column("Address", width=100)
        self.employee_table.column("Married", width=100)
        self.employee_table.column("DOB", width=100)
        self.employee_table.column("DOJ", width=100)
        self.employee_table.column("IDProofCombo", width=100)
        self.employee_table.column("IDProof", width=100)
        self.employee_table.column("Gender", width=100)
        self.employee_table.column("Phone", width=100)
        self.employee_table.column("Country", width=100)
        self.employee_table.column("Salary", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

        # Fetch data to display in the table
        self.fetch_data()

        # Bind the treeview to the get_cursor method to show selected row data in the form fields
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)

    # Function to add new employee data
    def add_data(self):
        if self.DepartmentVariable.get() == "" or self.NameVariable.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="employee_db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.DepartmentVariable.get(),
                    self.NameVariable.get(),
                    self.DesignationVariable.get(),
                    self.EmailVariable.get(),
                    self.AddressVariable.get(),
                    self.MarriedVariable.get(),
                    self.DOBVariable.get(),
                    self.DOJVariable.get(),
                    self.IDProofComboVariable.get(),
                    self.IDProofVariable.get(),
                    self.GenderVariable.get(),
                    self.PhoneVariable.get(),
                    self.CountryVariable.get(),
                    self.SalaryVariable.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee has been added")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    # Function to display data in the table
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="employee_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in rows:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Function to display selected row data in the form fields
    def get_cursor(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        row = content["values"]

        self.DepartmentVariable.set(row[0])
        self.NameVariable.set(row[1])
        self.DesignationVariable.set(row[2])
        self.EmailVariable.set(row[3])
        self.AddressVariable.set(row[4])
        self.MarriedVariable.set(row[5])
        self.DOBVariable.set(row[6])
        self.DOJVariable.set(row[7])
        self.IDProofComboVariable.set(row[8])
        self.IDProofVariable.set(row[9])
        self.GenderVariable.set(row[10])
        self.PhoneVariable.set(row[11])
        self.CountryVariable.set(row[12])
        self.SalaryVariable.set(row[13])

    # Function to update existing employee data
    def update_data(self):
        if self.DepartmentVariable.get() == "" or self.NameVariable.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                Update = messagebox.askyesno("Update", "Are you sure you want to update this employee data?")
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="employee_db")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employee set Department=%s, Name=%s, Designition=%s, Email=%s, Address=%s, Married=%s, DOB=%s, DOJ=%s, IDProofCombo=%s, IDProof=%s, Gender=%s, Country=%s, Salary=%s where Phone=%s", (
                        self.DepartmentVariable.get(),
                        self.NameVariable.get(),
                        self.DesignationVariable.get(),
                        self.EmailVariable.get(),
                        self.AddressVariable.get(),
                        self.MarriedVariable.get(),
                        self.DOBVariable.get(),
                        self.DOJVariable.get(),
                        self.IDProofComboVariable.get(),
                        self.IDProofVariable.get(),
                        self.GenderVariable.get(),
                        self.CountryVariable.get(),
                        self.SalaryVariable.get(),
                        self.PhoneVariable.get()
                    ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee Successfully Updated")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    # Function to delete employee data
    def delete_data(self):
        if self.PhoneVariable.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                Delete = messagebox.askyesno("Delete", "Are you sure you want to delete this employee data?")
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="employee_db")
                    my_cursor = conn.cursor()
                    sql = "delete from employee where Phone=%s"
                    value = (self.PhoneVariable.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Employee Successfully Deleted")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")

    # Function to clear the form fields
    def reset_data(self):
        self.DepartmentVariable.set("")
        self.NameVariable.set("")
        self.DesignationVariable.set("")
        self.EmailVariable.set("")
        self.AddressVariable.set("")
        self.MarriedVariable.set("")
        self.DOBVariable.set("")
        self.DOJVariable.set("")
        self.IDProofComboVariable.set("")
        self.IDProofVariable.set("")
        self.GenderVariable.set("")
        self.PhoneVariable.set("")
        self.CountryVariable.set("")
        self.SalaryVariable.set("")

    # Function to search employee data based on Phone or ID Proof
    def search_data(self):
        if self.SearchBy.get() == "" or self.SearchTxt.get() == "":
            messagebox.showerror("Error", "Please select option and enter data")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="employee_db")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from employee where " + str(self.SearchBy.get()) + " LIKE '%" + str(self.SearchTxt.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}")


# Main block to run the Tkinter application
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
