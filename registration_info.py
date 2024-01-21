from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

BACKGROUND = "#EEF0E5"

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pass_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    pass_ints = [random.choice(numbers) for _ in range(random.randint(2,4))]

    pass_list = pass_letters +pass_ints + pass_symbols

    random.shuffle(pass_list)

    password = "".join(pass_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)
    messagebox.showinfo(title="Copy",message="Password copied to the clipboard")



def add():
    web = website_entry.get()
    mail = email_entry.get()
    passw = password_entry.get()
    if len(web) == 0 or len(mail) == 0 or len(passw) == 0:
        messagebox.showerror(title="Error", message="Fields cannot be blank!")
    else:
        is_sure = messagebox.askokcancel(title="Are you sure?", message=f"These are the information you entered: \nWebsite: {web} \nEmail: {mail} \nPassword: {passw}")
        if is_sure:
            data_dict = {
                web:{
                    "email": mail,
                    "password": passw,
                }
            }
            try:
                with open("password_data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(data_dict)

                with open("password_data.json", mode= "w") as file:
                    json.dump(data, file, indent= 4)

            except FileNotFoundError:
                with open("password_data.json", mode="w") as file:
                    json.dump(data_dict, file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Added", message="Information has been successfully added.")

def search():
    website = website_entry.get()
    try:
        with open("password_data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data found!")
    else:
        if website in data:
            mail = data[website]["email"]
            passw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email: {mail}\npassword: {passw}")
        else:
            messagebox.showinfo(title="Error", message=f"No data found for {website}.")


window = Tk()
window.minsize(width=400, height=300)
window.config(padx=50, pady=50, bg=BACKGROUND)
window.title("Save Your Registration Info")

canvas = Canvas(width=200, height=200,highlightthickness=0, bg=BACKGROUND)
img = PhotoImage(file="psApp.png")
canvas.create_image(100, 100, image= img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website: ", font=("Calibri", 12), bg= BACKGROUND)
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column= 1)

search_button = Button(text="Search",command=search ,font=("Calibri", 12, "bold"), bg="#5FB6A2",width=17)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/username: ",font=("Calibri", 12), bg= BACKGROUND)
email_label.grid(row=2, column=0)

email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", font=("Calibri", 12), bg= BACKGROUND)
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row= 3, column=1)

generate_button = Button(text="Generate Password!", font=("Calibri", 12, "bold"),command=generate_password, bg ="#5FB6A2")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add,  font=("Calibri", 12, "bold"), bg="#5FB6A2", width=60)
add_button.grid(row=4, column=0, columnspan=3)

window.mainloop()
