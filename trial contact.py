class Contact:
    name = ""
    number = ""


def add_contact():
    contact = Contact()
    contact.name = input("Input user name:")
    contactList.append(contact)
    print("Contact added")


contactList = []
add_contact()
