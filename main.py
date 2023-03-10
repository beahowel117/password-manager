from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        #message box to make sure the user wants to save particular email and pw
        #is_ok = messagebox.askokcancel(title=website, message=f"These are teh details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save? ")
        #if is_ok:
        try:
            with open("data.json", "r") as data_file:
                #for text usage
                #data_file.write(f"{website} | {email} | {password} \n")
                #read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            # once data is loaded into a dictionary, can update with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #write back into json file/save updated
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No details for the website exists")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry()
website_input.grid(column=1, row=1, sticky="EW")
#start cursor here
website_input.focus()

email_input = Entry()
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
#END puts cursor at end of email and 0 beginning
email_input.insert(0, "beth@gmail.com")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")


generate_pw = Button(text="Generate Password", command=generate_password)
generate_pw.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)






window.mainloop()