from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("New User Registration")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False, False)

def register():
    username = user.get()
    password = code.get()
    admincode = adminaccess.get()

    if admincode == "2024":
        if (username == "" or username == "UserID") or (password == "" or password == "Password"):
            messagebox.showerror("Enter error!", "Type username or password !!!")
        else:
            try:
                # Connect to MySQL server
                mydb = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Frankboy123@'
                )
                mycursor = mydb.cursor()
                print("Connection Established!!")
                
                # Create the database
                try:
                    mycursor.execute("CREATE DATABASE IF NOT EXISTS StudentRegistration")
                    print("Database created or already exists.")
                except Error as e:
                    print(f"Error creating database: {e}")
                
                # Connect to the new database
                mydb = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Frankboy123@',
                    database='StudentRegistration'
                )
                mycursor = mydb.cursor()
                
                # Create the table
                try:
                    mycursor.execute("""
                        CREATE TABLE IF NOT EXISTS login (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            Username VARCHAR(50),
                            Password VARCHAR(100)
                        )
                    """)
                    print("Table created or already exists.")
                except Error as e:
                    print(f"Error creating table: {e}")
                
                # Insert the new user
                command = "INSERT INTO login (Username, Password) VALUES (%s, %s)"
                mycursor.execute(command, (username, password))
                mydb.commit()
                print("User added successfully.")
                messagebox.showinfo("Register", "New User added Successfully")
                
            except Error as e:
                messagebox.showerror("Connection", f"Database connection not established !! Error: {e}")
            finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()
                    print("MySQL connection is closed")
    else:
        messagebox.showerror("Admin code!", "Input Correct Admin code to add new user!!")

def login():
    root.destroy()  # to close the current window
    import Login

# icon image
image_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False, image_icon)

# background image
frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="images/register.png")
Label(frame, image=backgroundimage).pack()

adminaccess = Entry(frame, width=15, fg="#000", border=0, bg="#e8ecf7", font=("Arial Bold", 20), show="*")
adminaccess.focus()
adminaccess.place(x=550, y=280)

######### User entry
def user_enter(e):
    user.delete(0, 'end')

def user_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "UserID")

user = Entry(frame, width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold", 20))
user.insert(0, "UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=380)

######### Password entry
def password_enter(e):
    code.delete(0, 'end')

def password_leave(e):
    if code.get() == '':
        code.insert(0, "Password")

code = Entry(frame, width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold", 20))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500, y=470)

####################################
button_mode = True

def hide():
    global button_mode

    if button_mode:
        eyeButton.config(image=closeeye, activebackground="white")
        code.config(show="*")
        button_mode = False
    else:
        eyeButton.config(image=openeye, activebackground="white")
        code.config(show="")
        button_mode = True

openeye = PhotoImage(file="images/openeye.png")
closeeye = PhotoImage(file="images/close eye.png")

eyeButton = Button(root, image=openeye, bg="#375174", bd=0, command=hide)
eyeButton.place(x=780, y=470)

#####################################

regis_button = Button(root, text="ADD NEW USER", bg="#455c88", fg="white", width=13, height=1, font=("Arial", 16, "bold"), bd=0, command=register)
regis_button.place(x=530, y=600)

backbuttoimage = PhotoImage(file="images/backbutton.png")
Backbutton = Button(root, image=backbuttoimage, fg="#deeefb", command=login)
Backbutton.place(x=20, y=15)

root.mainloop()
