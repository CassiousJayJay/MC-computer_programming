from tkinter import Tk
from ui import AddressBookUl

#entry point of the application
if __name__=="__main__":
    #create the Tkinter root window
    root = Tk()
    root.title("Address Book")

    #create an instance of the AddressBookUI
    address_book_ui = AddressBookUI(root)

    #start the Tkinter event loop
    root.mainloop()
