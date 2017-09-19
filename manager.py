class Contact:
    name = ""
    number = ""


def menu_choices():
    print("1. Add new contact")
    print("2. Print all contacts")
    print("3. Delete contact")
    print("4. Search contact")
    return input("Please enter your choice (1-5): ")


def add_contact():
    contact = Contact()
    contact.name = input("Enter contact name: ")
    contact.number = input("Enter contact number: ")
    contactList.append(contact)
    print("Contact added.")


def print_contacts():
    print("Printing contacts...")
    for itm in contactList:
        print(itm.name + ", " + itm.number),
    print()


def search_contacts(name):
    for itm in contactList:
        if itm.name == name:
            print(itm.name + ", " + itm.number),
    print()


def delete_contacts(name):
    for index, itm in enumerate(contactList):
        if itm.name == name:
            del contactList[index]
            print("contact deleted")
        else:
            print("contact not found")
    print()


contactList = []
choice = menu_choices()
while choice != "5":
    if choice == "1":
        add_contact()
    elif choice == "2":
        print_contacts()
    elif choice == "4":
        search_contacts(input("input name to search:"))
    elif choice == "3":
        delete_contacts(input("input contact name to be deleted:"))
    choice = menu_choices()
print()
print()
