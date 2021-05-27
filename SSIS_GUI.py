"""AIKO MARIELLE C. BERNARDO"""

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
import csv


class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information System")
        self.root.geometry("1285x440")
        self.root.config(bg="light slate gray")
        self.root.resizable(False, False)
        self.data = dict()
        self.temp = dict()
        self.filename = 'studinfo.csv'

        StudentIDNumber = StringVar()
        StudentName = StringVar()
        Course = StringVar()
        YearLevel = StringVar()
        Gender = StringVar()
        Search = StringVar()

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w') as csv_file:
                fieldnames = ["ID Number", "Name", "Gender", "Course", "Year Level"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

        else:
            with open(self.filename, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["ID Number"]] = {'Name': row["Name"],
                                                   'Gender': row["Gender"],
                                                   'Course': row["Course"],
                                                   'Year Level': row["Year Level"]}
            self.temp = self.data.copy()

        def searchstud():
            self.Search.get()
            search = []
            for i in self.Search.get():
                search.append(i)
            if "-" in search:
                searchsplitted = self.Search.get().split("-")
                y = searchsplitted[0]
                n = searchsplitted[1]
                if y.isdigit() == False or n.isdigit() == False:
                    tkinter.messagebox.showerror("SSIS", "Sorry but this is an invalid ID")
                else:
                    if self.Search.get() in self.data:
                        vals = list(self.data[self.Search.get()].values())
                        tree.delete(*tree.get_children())
                        tree.insert("", 0, values=(self.Search.get(), vals[0], vals[1], vals[2], vals[3]))
                    elif self.Search.get() == "":
                        displayStudent()
                    else:
                        tkinter.messagebox.showerror("SSIS", "Sorry But Student Not Found.")
                        return
            elif self.Search.get() == "":
                tkinter.messagebox.showerror("SSIS", "Sorry But Student Not Found..")
            else:
                tkinter.messagebox.showerror("SSIS", "Sorry But Student Not Found.")

        def selectstud():
            if tree.focus() == "":
                tkinter.messagebox.showerror("SSIS", "Sorry Please Select a Student.")
                return
            values = tree.item(tree.focus(), "values")
            StudentIDNumber.set(values[0])
            StudentName.set(values[1])
            Gender.set(values[2])
            Course.set(values[3])
            YearLevel.set(values[4])

        def displayStudent():
            tree.delete(*tree.get_children())
            with open(self.filename) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    studentid = row['ID Number']
                    Name = row['Name']
                    Gender = row['Gender']
                    Course = row['Course']
                    YearLevel = row['Year Level']
                    tree.insert("", END, values=(studentid, Name, Gender, Course, YearLevel))

        def addstud():
            with open(self.filename, "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentIDNumber.get() == "" or StudentName.get() == "" or YearLevel.get() == "" or Course.get() == "" or Gender.get() == "":
                    tkinter.messagebox.showinfo("SSIS", "Please Fill In the Box")
                else:
                    StudentIDNumber.get()
                    StudentIDNumber_list = []
                    for i in StudentIDNumber.get():
                        StudentIDNumber_list.append(i)
                    if "-" in StudentIDNumber_list:
                        x = StudentIDNumber.get().split("-")
                        y = x[0]
                        n = x[1]
                        if y.isdigit() == False or n.isdigit() == False:
                            tkinter.messagebox.showerror("SSIS", "Sorry but this is an Invalid ID")
                        else:
                            if StudentIDNumber.get() in self.data:
                                tkinter.messagebox.showinfo("SSIS", "Sorry But Student Already Exist")
                            else:
                                self.data[StudentIDNumber.get()] = {'Name': StudentName.get(), 'Gender': Gender.get(),
                                                                    'Course': Course.get(),
                                                                    'Year Level': YearLevel.get()}
                                self.saveData()
                                tkinter.messagebox.showinfo("SSIS", "Student's Data has been saved successfully!")
                                Clear()
                    else:
                        tkinter.messagebox.showerror("SSIS", "Sorry but this is an Invalid ID")
                    displayStudent()

        def updatestud():
            sel = tree.focus()
            sel_id = tree.item(sel, "values")[0]

            with open(self.filename, "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentIDNumber.get() == "" or StudentName.get() == "" or YearLevel.get() == "" or Course.get() == "" or Gender.get() == "":
                    tkinter.messagebox.showinfo("SSIS", "Please Fill In the Box")
                elif sel_id == StudentIDNumber.get():
                    self.data[StudentIDNumber.get()] = {'Name': StudentName.get(),
                                                        'Gender': Gender.get(),
                                                        'Course': Course.get(),
                                                        'Year Level': YearLevel.get()}
                else:
                    self.data.pop(sel_id, None)
                    self.data[StudentIDNumber.get()] = {'Name': StudentName.get(),
                                                        'Gender': Gender.get(),
                                                        'Course': Course.get(),
                                                        'Year Level': YearLevel.get()}

                result = tkinter.messagebox.askquestion("SSIS", "Are you sure to update this record?")
                if result == "yes":
                    self.data.pop(csvfile, None)
                    self.saveData()
                    tkinter.messagebox.showinfo("SIS", "Student Has Been Updated Successfully")
                    Clear()
                displayStudent()

        def deletestud():
            x = tree.focus()
            if x == "":
                tkinter.messagebox.showerror("SSIS", "Sorry, Please Select A Student to delete.")
                return
            id_no = tree.item(x, "values")[0]

            result = tkinter.messagebox.askquestion("SSIS", "Are you sure to delete this record?")
            if result == "yes":
                self.data.pop(id_no, None)
                self.saveData()
                tree.delete(x)
                tkinter.messagebox.showinfo("SSIS", "Student's Record has been deleted successfully")
                Clear()
            else:
                pass

        def Clear():
            StudentIDNumber.set("")
            StudentName.set("")
            YearLevel.set("")
            Gender.set("")
            Course.set("")
            Search.set("")

        def Exit():
            iExit = tkinter.messagebox.askyesno("SSIS", "Are you sure you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        '''''''''FRAMES'''''''''

        TitleFrame = Frame(self.root, bd=5, width=1000, bg="light gray", height=90,
                           relief=RIDGE)
        TitleFrame.pack(side=TOP)

        LeftFrame = Frame(self.root, bg="light slate gray", bd=5, width=600,
                          height=250, padx=2, pady=4)
        LeftFrame.pack(side=LEFT, padx=0, pady=0)

        '''''''''TITLE'''''''''

        self.lblTitle = Label(TitleFrame, font=('cochin', 35, 'italic', 'bold'),
                              text="STUDENT INFORMATION SYSTEM", bg="light gray",
                              fg="skyblue4", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)

        '''''''''LABELS AND ENTRY WIDGET'''''''''

        self.lblSearch = Label(LeftFrame, font=('cochin', 13, 'bold'),
                               text="Search ID Num:", fg="honeydew2",
                               bg="light slate gray", bd=10, anchor=W)
        self.lblSearch.grid(row=0, column=0, sticky=W)
        self.Search = Entry(self.root, font=("cochin", 10, "italic", "bold"),
                            fg="skyblue4", textvariable=Search, width=27, bd=10)
        self.Search.place(x=155, y=120)
        self.Search.insert(0, '')

        self.lblStudentID = Label(LeftFrame, font=('cochin', 13, 'bold'),
                                  text="ID Number:", fg="honeydew2",
                                  bg="light slate gray", bd=10, anchor=W)
        self.lblStudentID.grid(row=1, column=0, sticky=W)
        self.lblStudentID = Entry(LeftFrame, font=('cochin', 10, 'bold'), bd=10,
                                  width=47, justify='left', textvariable=StudentIDNumber,
                                  fg="skyblue4")
        self.lblStudentID.grid(row=1, column=1)

        self.lblFullName = Label(LeftFrame, font=('cochin', 13, 'bold'), text="Full Name:",
                                 fg="honeydew2", bg="light slate gray", bd=10, anchor=W)
        self.lblFullName.grid(row=2, column=0, sticky=W)
        self.lblFullName = Label(LeftFrame, font=('cochin', 10, 'italic', 'bold'),
                                 text="Firstname                         MI                         Lastname",
                                 bg="light slate gray", fg="honeydew2", bd=10, anchor=W)
        self.lblFullName.grid(row=3, column=1, sticky=W)
        self.lblFullName = Entry(LeftFrame, font=('cochin', 10, 'bold'), bd=10, width=47,
                                 textvariable=StudentName, fg="skyblue4")
        self.lblFullName.grid(row=2, column=1)

        self.lblCourse = Label(LeftFrame, font=('cochin', 13, 'bold'), text="Course:",
                               fg="honeydew2", bg="light slate gray", bd=10, anchor=W)
        self.lblCourse.grid(row=4, column=0, sticky=W)
        self.lblCourse = Entry(LeftFrame, font=('cochin', 10, 'bold'), bd=10,
                               width=47, justify='left', textvariable=Course, fg="skyblue4")
        self.lblCourse.grid(row=4, column=1)

        self.lblYearLevel = Label(LeftFrame, font=('cochin', 13, 'bold'), text="Year Level:",
                                  fg="honeydew2", bg="light slate gray", bd=10, anchor=W)
        self.lblYearLevel.grid(row=5, column=0, sticky=W)
        self.lblYearLevel = ttk.Combobox(LeftFrame, font=('cochin', 10, 'bold'),
                                         state='readonly', width=47, textvariable=YearLevel)
        self.lblYearLevel['values'] = ('', '1st Year', '2nd Year', '3rd Year', '4th Year')
        self.lblYearLevel.current(0)
        self.lblYearLevel.grid(row=5, column=1)

        self.lblGender = Label(LeftFrame, font=('cochin', 13, 'bold'), text="Gender:",
                               fg="honeydew2", bg="light slate gray", bd=10, anchor=W)
        self.lblGender.grid(row=6, column=0, sticky=W)
        self.lblGender = ttk.Combobox(LeftFrame, font=('cochin', 10, 'bold'),
                                      state='readonly', width=47, textvariable=Gender)
        self.lblGender['values'] = ('', 'Female', 'Male')
        self.lblGender.current(0)
        self.lblGender.grid(row=6, column=1)

        ''''''''' BUTTONS '''''''''

        self.btnSearch = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                                padx=24, width=8, text='SEARCH', fg="skyblue4", command=searchstud)
        self.btnSearch.place(x=378, y=123)

        self.btnSelect = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                                padx=24, width=8, text='SELECT', fg="skyblue4", command=selectstud)
        self.btnSelect.place(x=513, y=123)

        self.btnShow = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                              padx=24, width=8, text='VIEW STUDENTS', fg="skyblue4", command=displayStudent)
        self.btnShow.place(x=513, y=163)

        self.btnAddNew = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                                padx=24, width=8, text='ADD', fg="skyblue4", command=addstud)
        self.btnAddNew.place(x=513, y=203)

        self.btnUpdate = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                                padx=24, width=8, text='UPDATE', fg="skyblue4", command=updatestud)
        self.btnUpdate.place(x=513, y=243)

        self.btnDelete = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                                padx=24, width=8, text='DELETE', fg="skyblue4", command=deletestud)
        self.btnDelete.place(x=513, y=283)

        self.btnClear = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                               padx=24, width=8, text='CLEAR', fg="skyblue4", command=Clear)
        self.btnClear.place(x=513, y=323)

        self.btnExit = Button(self.root, pady=1, bd=4, font=('cochin', 10, 'bold'),
                              padx=24, width=8, text='EXIT', fg="skyblue4", command=Exit)
        self.btnExit.place(x=513, y=363)

        '''''''''TREEVIEW'''''''''

        scroll_y = Scrollbar(self.root, orient=VERTICAL)
        tree = ttk.Treeview(self.root, height=15, columns=("ID Number", "Name",
                                                           "Gender", "Course", "Year Level"),
                            yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.place(x=1260, y=100, height=328)

        tree.heading("ID Number", text="ID Number")
        tree.heading("Name", text="Name")
        tree.heading("Course", text="Course")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Gender", text="Gender")
        tree['show'] = 'headings'
        tree.column("ID Number", width=90)
        tree.column("Name", width=184)
        tree.column("Course", width=150)
        tree.column("Year Level", width=99)
        tree.column("Gender", width=93)
        scroll_y.config(command=tree.yview)
        tree.pack(fill=BOTH, expand=1)
        tree.place(x=642, y=100)

        displayStudent()

    def saveData(self):
        datalist = []
        with open(self.filename, "w", newline='') as update:
            fieldnames = ["ID Number", "Name", "Gender", "Course", "Year Level"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp = {"ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                datalist.append(temp)
            writer.writerows(datalist)


if __name__ == '__main__':
    root = Tk()
    application = student(root)
    root.mainloop()
