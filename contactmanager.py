class Contact:  # we use the object Contact to store the variable name and number
    name = ""
    number = ""


def menu_choices():  # initiating an instance of menu choices to loop in the cli
    print("1. Add new contact")
    print("2. Print all contacts")
    print("3. Delete contact")
    print("4. Search contact")
    return input("Please enter your choice (1-4): ")


def add_contact():
    pass


def print_contact():
    pass


def search_contact():
    pass


def delete_contact():
    pass


contactList = []
choice = menu_choices()
while choice < "5":
    if choice == "1":
        add_contact()
    elif choice == "2":
        print_contact()
    elif choice == "4":
        search_contact(input("input name to search:"))
    elif choice == "3":
        delete_contact(input("input contact name to be deleted:"))
    choice = menu_choices()
