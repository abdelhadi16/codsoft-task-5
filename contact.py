
class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

# function to create a contact
def create_contact():
    store_name = input("Enter store name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(store_name, phone_number, email, address)

#  the function to print contact details 
def printe(contact_list):
    for contact in contact_list:
        print(f"Store Name: {contact.store_name}")
        print(f"Phone Number: {contact.phone_number}")
        """print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")"""
        print()  # New line for better readability


# the function to search for a contact
def search(contact_list,nph):
    for contact in contact_list :
        if (contact.store_name == nph) or (contact.phone_number == int(nph)):
             print("contact found this hes informations :")
             print(f"Store Name: {contact.store_name}")
             print(f"Phone Number: {contact.phone_number}")
             print(f"Email: {contact.email}")
             print(f"Address: {contact.address}")
             return contact
    print("contact not found in the list")
    return None
            

# Function to search for a contact
def search(contact_list, nph):
    for contact in contact_list:
        if (contact.store_name == nph) or (contact.phone_number == nph):
            print("Contact found with the following information:")
            print(f"Store Name: {contact.store_name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            return contact
    print("Contact not found in the list")
    return None

# function to update a contact
def update(contact_list):
    printe(contact_list)
    index = int(input("enter the index (starting from 1) of the contact you want to update: "))
    if 0 < index < len(contact_list):
        contact = contact_list[index - 1]
        print("updating contact details  press enter to keep current value.")
        store_name = input(f"enter new store name (current: {contact.store_name}): ") or contact.store_name
        phone_number = input(f"enter new phone number (current: {contact.phone_number}): ") or contact.phone_number
        email = input(f"enter new email (current: {contact.email}): ") or contact.email
        address = input(f"enter new address (current: {contact.address}): ") or contact.address
        contact.store_name = store_name
        contact.phone_number = phone_number
        contact.email = email
        contact.address = address
        print("contact updated successfully.")
    else:
        print("invalid index  no contact updated.")
def delete(contact_list):
    printe(contact_list)
    index = int(input("enter the index (starting from 1) of the contact you want to delete: "))
    if 0 < index < len(contact_list):
        contact_list.pop(index - 1)
    else:
        print("invalid index  no contact deleted.")

        

# Create a list of contacts

contact_list = []
print("welcome to contact Book application ")
while True:
    print("-------------------------------------")
    print("choise one of a option :")
    print("1. add new contact to the contacts list ")
    print("2. View contact List") 
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Quit")
    choise = int(input("enter youre choise :"))
    while choise not in [1,2,3,4] :
        choise = int(input("enter youre choise :"))
    if choise == 1 : 
        contact = create_contact()
        contact_list.append(contact)
        print("contact added successfully")
    elif choise == 2 :
        printe(contact_list)
    elif choise == 3 :
        nph = input("enter the phone number or the name of the store :")
        search(contact_list,nph)
    elif choise == 4 :
        update(contact_list)
    elif choise == 5 :
        delete(contact_list)
    elif choise == 6 :
        break
    else:
        print("Invalid choice. Please try again.")

     
        
