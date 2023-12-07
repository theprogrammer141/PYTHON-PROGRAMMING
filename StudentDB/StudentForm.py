from tkinter import *
import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\abdul\OneDrive\Desktop\StudentDB\studentform.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")

except pyodbc.Error as e:
    print("Error in Connection", e)

#ClearRecord function
def ClearRecord():
    #Write your Clear Record Code Here
    sNameValue.set("")
    fNameValue.set("")
    cnicValue.set("")
    cityValue.set("")
    marksValue.set("")
    message.config(text="Record Cleared",fg="green")
    print("Clear Record")

#FirstRecord function
def FirstRecord():
    # Write your First Record Code Here
    try:
        curr=conn.cursor()
        curr.execute('SELECT TOP 1 * FROM Student ORDER BY cnic')
        first_record=curr.fetchone()
        if first_record:
            sNameEntry.delete(0,'end')
            sNameEntry.insert(0,first_record.sname)
            fNameEntry.delete(0,'end')
            fNameEntry.insert(0,first_record.fname)
            cnicEntry.delete(0,'end')
            cnicEntry.insert(0,first_record.cnic)
            cityEntry.delete(0,'end')
            cityEntry.insert(0,first_record.city)
            marksEntry.delete(0,'end')
            marksEntry.insert(0,first_record.marks)
            message.config(text="FIRST RECORD RETRIEVED",fg="green")
        else:
            message.config(text="NO RECORDS FOUND",fg="red")
    except pyodbc.Error as e:
        message.config(text="ERROR RETRIEVING RECORD: " + str(e),fg="red")
    print("First Record")

#NextRecord function
def NextRecord():
    #Write your Next Record Code Here
    try:
        curr=conn.cursor()
        curr.execute('SELECT TOP 1 * FROM Student WHERE cnic > ? ORDER BY cnic',cnicValue.get())
        next_record=curr.fetchone()
        if next_record:
            sNameEntry.delete(0,'end')
            sNameEntry.insert(0,next_record.sname)
            fNameEntry.delete(0, 'end')
            fNameEntry.insert(0, next_record.fname)
            cnicEntry.delete(0, 'end')
            cnicEntry.insert(0, next_record.cnic)
            cityEntry.delete(0, 'end')
            cityEntry.insert(0, next_record.city)
            marksEntry.delete(0, 'end')
            marksEntry.insert(0, next_record.marks)
            message.config(text="NEXT RECORD RETRIEVED", fg="green")
        else:
            message.config(text="NO NEXT RECORD FOUND",fg="red")
    except pyodbc.Error as e:
        message.config(text="ERROR RETRIEVING NEXT RECORD: " + str(e),fg="red")

        print("Next Record")

#PreviousRecord function
def PreviousRecord():
    # Write your Previous Record Code Here
    try:
        curr=conn.cursor()
        curr.execute('SELECT TOP 1 * FROM Student WHERE cnic < ? ORDER BY cnic DESC',cnicValue.get())
        previous_record=curr.fetchone()
        if previous_record:
            sNameValue.set(previous_record.sname)
            fNameValue.set(previous_record.fname)
            cnicValue.set(previous_record.cnic)
            cityValue.set(previous_record.city)
            marksValue.set(previous_record.marks)
            message.config(text="PREVIOUS RECORD RETRIEVED",fg="green")
        else:
            message.config(text="PREVIOUS RECORD NOT FOUND",fg="red")
    except pyodbc.Error as e:
        message.config(text="ERROR RETRIEVING PREVIOUS RECORD",fg="red")
    print("Previous Record")

#LastRecord function
def LastRecord():
    # Write your Last Record Code Here
    try:
        curr=conn.cursor()
        curr.execute('SELECT TOP 1 * FROM Student ORDER BY cnic DESC')
        last_record=curr.fetchone()
        if last_record:
            sNameValue.set(last_record.sname)
            fNameValue.set(last_record.fname)
            cnicValue.set(last_record.cnic)
            cityValue.set(last_record.city)
            marksValue.set(last_record.marks)
            message.config(text="LAST RECORD RETRIEVED",fg="green")
        else:
            message.config(text="LAST RECORD NOT FOUND",fg="red")
    except pyodbc.Error as e:
        message.config(text="ERROR RETRIEVING LAST RECORD" + str(e),fg="red")
    print("Last Record")

#InsertRecord function
def InsertRecord():
    # Write your Insert Record Code Here
    try:
        curr=conn.cursor()
        cnic=cnicValue.get()
        curr.execute('SELECT * FROM STUDENT WHERE cnic=?',(cnic,))
        existing_record=curr.fetchone()
        if existing_record:
            message.config(text="CNIC ALREADY SAVED!ENTER ANOTHER",fg="red")
        else:
            sname=sNameValue.get()
            fname=fNameValue.get()
            cnic=cnicValue.get()
            city=cityValue.get()
            marks=marksValue.get()
            curr.execute('INSERT INTO Student(sname,fname,cnic,city,marks)VALUES(?,?,?,?,?)',(sname,fname,cnic,city,marks))
            curr.commit()
            message.config(text="RECORD INSERTED SUCCESSFULLY!",fg="green")
    except pyodbc as e:
        message.config(text="ERROR INSERTING RECORD: " + str(e),fg="red")
    print("Insert Record")

#UpdateRecord function
def UpdateRecord():
    # Write your Update Record Code Here
    try:
        curr=conn.cursor()
        cnic=cnicValue.get()
        curr.execute("SELECT * FROM Student WHERE cnic=?",cnic)
        existing_record=curr.fetchall()
        if existing_record:
                sname=sNameValue.get()
                fname=fNameValue.get()
                cnic=cnicValue.get()
                city=cityValue.get()
                marks=marksValue.get()
                curr.execute('UPDATE Student SET sname=?,fname=?,city=?,marks=? WHERE cnic=?',(sname,fname,city,marks,cnic))
                curr.commit()
                message.config(text="RECORD UPDATED SUCCESSFULLY!",fg="green")
        else:
            if cnic:
                message.config(text="PLEASE ENTER CORRECT CNIC# TO UPDATE!",fg="red")
            else:
                message.config(text="PLEASE ENTER CNIC# FIRST!",fg="red")
    except pyodbc.Error as e:
        message.config(text="ERROR UPDATING RECORD: " + str(e),fg="red")
    print("Update Record")

#DeleteRecord function
def DeleteRecord():
    # Write your Delete Record Code Here
    try:
        curr=conn.cursor()
        cnic=cnicValue.get()
        if not cnic:
            message.config(text="PLEASE ENTER CNIC# TO DELETE!",fg="red")
        else:
            curr.execute('DELETE FROM Student WHERE cnic=?',(cnic,))
            if curr.rowcount==0:
                message.config(text="NO RECORD FOUND TO DELETE!",fg="red")
            else:
                conn.commit()
                message.config(text="RECORD DELETED SUCCESSFULLY!",fg="green")
    except pyodbc.Error as e:
        message.config(text="ERROR DELETING RECORD: " + str(e),fg="red")
    print("Delete Record")

#SearchRecord function
def SearchRecord():
    # Write your Search Record Code Here
    try:
        search_cnic=cnicValue.get()
        if not search_cnic:
            message.config(text="PLEASE ENTER CNIC# TO SEARCH!",fg="red")
        else:
            curr=conn.cursor()
            curr.execute("SELECT * FROM Student WHERE cnic=?",search_cnic)
            found_cnic=curr.fetchone()
            if found_cnic:
                sNameValue.set(found_cnic.sname)
                fNameValue.set(found_cnic.fname)
                cnicValue.set(found_cnic.cnic)
                cityValue.set(found_cnic.city)
                marksValue.set(found_cnic.marks)
                message.config(text="RECORD FOUND!",fg="green")
            else:
                message.config(text="NO RECORD FOUND CNIC#!",fg="red")
    except pyodbc.Error as e:
        message.config(text="ERROR FINDING RECORD: " + str(e),fg="red")
    print("Search Record")



#Design the Student Database Form
root = Tk()
root.geometry("600x400")

#
Label(root, text = "Student Database Form", font="Arial 12 bold", foreground='blue').grid(row=0, column=0)
message = Label(root, text = "Message Will Appear Here!",foreground='red')
sname = Label(root,text='Student Name', font="ar 10 bold")
fname = Label(root,text='Father Name',font="ar 10 bold")
cnic = Label(root,text='CNIC# (P.Key)',font="ar 10 bold")
search = Label(root,text='Search Record',font="ar 10 bold")
city = Label(root,text='City',font="ar 10 bold")
marks = Label(root,text='Marks',font="ar 10 bold")

message.grid(row=0,column=1)
sname.grid(row=2,column=0)
fname.grid(row=3,column=0)
cnic.grid(row=4,column=0)
search.grid(row=4,column=2)
city.grid(row=5,column=0)
marks.grid(row=6,column=0)

sNameValue = StringVar()
fNameValue = StringVar()
cnicValue = StringVar()
cityValue = StringVar()
marksValue = IntVar()

sNameEntry = Entry(root, textvariable=sNameValue,width='30',font='ar 12 bold')
fNameEntry = Entry(root, textvariable=fNameValue,width='30',font='ar 12 bold')
cnicEntry = Entry(root, textvariable=cnicValue,width='30',font='ar 12 bold')
cityEntry = Entry(root, textvariable=cityValue,width='30',font='ar 12 bold')
marksEntry = Entry(root, textvariable=marksValue,width='30',font='ar 12 bold')

sNameEntry.grid(row=2,column=1,pady=15)
fNameEntry.grid(row=3,column=1,pady=15)
cnicEntry.grid(row=4,column=1,pady=15)
cityEntry.grid(row=5,column=1,pady=15)
marksEntry.grid(row=6,column=1,pady=15)

Button(text="CLEAR",command=ClearRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=0)
Button(text="FIRST",command=FirstRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=1)
Button(text="NEXT",command=NextRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=2)
Button(text="PREVIOUS",command=PreviousRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=0)
Button(text="LAST",command=LastRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=1)
Button(text="INSERT",command=InsertRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=2)
Button(text="UPDATE",command=UpdateRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=0)
Button(text="DELETE",command=DeleteRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=1)
Button(text="SEARCH",command=SearchRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=2)

root.mainloop()
