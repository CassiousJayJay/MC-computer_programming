import tkinter as tk
from tkinter import messagebox
from functools import partial

#import the CRUD function
from contacts_manager import create_contact, get_all_contacts, update_contact, delete_contact

#create the main application window
window = tk.Tk()
window.title("Address Book")

#create labels and entry fields
label_name = tk.Label(window,text="Name")
entry_name = tk.Entry(window)

label_email = tk.Label(window, text="Email")
entry_email = tk.Entry(window)

label_phone = tk.Label(window, text="phone")
entry_phone = tk.Label(window)

#create a listbox to display contacts
contact_listbox = tk.Listbox(window, width=50)

#function to populate the listbox with contacts
def load_contacts():
    contact_listbox.delete(0, tk.END)
    contacts = get_all_contacts()
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['email']} - {contact['phone']}")

#function to add a new contact
def add_contact():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    create_contact(name, email, phone)
    load_contacts()
    messagebox.showinfo("Success", "contact added successfully")

#functions to update a contact
def update_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contact_id = selected_index[0] + 1
        name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        update_contact(contact_id, name, email, phone)
        load_contacts()
        messagebox.showinfo("Success", "Contact update successfully")
    else:
            messagebox.showerror("Error", "No contact selected.")

#function to delete a contact
def delete_selected_contact():
     selected_index = contact_listbox.curselection()
     if selected_index:
        contact_id = selected_index[0] + 1
        delete_contact(contact_id)
        load_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully")
     else:
        messagebox.showerror("Error", "No contact selected")

#set the layout of the UI element
label_name.pack()
entry_name.pack()

label_email.pack()
entry_email.pack()

label_phone.pack()
entry_phone.pack()

contact_listbox.pack()

button_add = tk.Button(window, text="Add contact", command=add_contact)
button_update = tk.Button(window, text="Update contact", command=update_selected_contact)
button_delete = tk.Button(window, text="Delete contact", command=delete_selected_contact)

button_add.pack()
button_update.pack()
button_delete.pack()

#load contacts on application startup
load_contacts()

#start the main event loop
window.mainloop()





        