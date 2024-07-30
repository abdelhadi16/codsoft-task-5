import tkinter as tk
from tkinter import messagebox , simpledialog

class Contactapp:
    def __init__(self, start):
        self.start = start
        self.start.title("Contact  book")
        self.contacts = []
        self.selected_index = None

        #widgets phone and  mail and name ......
        self.store_name = tk.Entry(start, width=30)
        self.store_name.grid(row=0, column=1, padx=10, pady=5)
        self.phone_number = tk.Entry(start, width=30)
        self.phone_number.grid(row=1, column=1, padx=10, pady=5)
        self.address = tk.Entry(start, width=30)
        self.address.grid(row=2, column=1, padx=10, pady=5)
        self.email = tk.Entry(start, width=30)
        self.email.grid(row=3, column=1, padx=10, pady=5)

        # Labels
        tk.Label(start, text="Store Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(start, text="Phone Number").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(start, text="Address").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(start, text="email").grid(row=3, column=0, padx=10, pady=5)

        # Buttons
        tk.Button(start, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(start, text="Delete Contact", command=self.delete_contact).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(start, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(start, text="Update Contact", command=self.load_contact_for_update).grid(row=7, column=0, columnspan=2, pady=5)

        # List
        self.contact_listbox = tk.Listbox(start, width=50, height=20)
        self.contact_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.store_name.get()
        phone = self.phone_number.get()
        address = self.address.get()
        email = self.email.get()
        if name and phone and address and email:
            self.contacts.append({'store_name': name, 'phone': phone, 'address': address , 'email': email})
            self.update_list()
            self.clear()
            messagebox.showinfo("contact added", f"contact '{name}' added .")
        else:
            messagebox.showwarning("input ERROR", "please fill in all fields")

    def delete_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            contact = self.contacts.pop(selected_index)
            self.update_list()
            messagebox.showinfo("contact Deleted", f"contact '{contact['store_name']}' deleted .")
        except IndexError:
            messagebox.showwarning("selection Error", "please select a contact to delete.")

    def search_contact(self):
        search = tk.simpledialog.askstring("search contact", "enter  name or phone number:")
        if search:
            results = [contact for contact in self.contacts if search in contact['store_name'] or search in contact['phone']]
            if results:
                self.contact_listbox.delete(0, tk.END)
                for contact in results:
                    self.contact_listbox.insert(tk.END, f"{contact['store_name']} - {contact['phone']} - {contact['address']} - {contact['email']}")
            else:
                messagebox.showinfo("Search Result", "no contacts found.")
        else:
            messagebox.showwarning("input ERROR", "please enter a search query")
    def load_contact_for_update(self):
        try:
            self.selected_index = self.contact_listbox.curselection()[0]
            contact = self.contacts[self.selected_index]
            self.store_name.delete(0, tk.END)
            self.store_name.insert(0, contact['store_name'])
            self.phone_number.delete(0, tk.END)
            self.phone_number.insert(0, contact['phone'])
            self.address.delete(0, tk.END)
            self.address.insert(0, contact['address'])
            self.email.delete(0, tk.END)
            self.email.insert(0, contact['email'])
        except IndexError:
            messagebox.showwarning("selection Error", "please select a contact to update")

    def update_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['store_name']} - {contact['phone']} - {contact['address']} - {contact['email']}")

    def clear(self):
        self.store_name.delete(0, tk.END)
        self.phone_number.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.email.delete(0,tk.END)

if __name__ == "__main__":
    start = tk.Tk()
    app = Contactapp(start)
    start.mainloop()

