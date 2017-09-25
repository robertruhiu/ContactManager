import csv

with open('emails.csv', mode = 'r') as infile:
    reader = csv.reader(infile)
    mydict = { rows [ 0 ]:rows [ 1 ] for rows in reader }


def menu_choices ( ):  # initiating an instance of menu choices to loop in the cli
    print("1. Add new guest")
    print("2. Search contact")
    return input("Please enter your choice (1-2): ")


def add_guest (x, y):
    mydict [ x ] = y


def search_email (name):
    if mydict.get(name) != None:
        print("{}:: {}".format(name, mydict.get(name)))
    else:
        print("Email not found")


print(mydict)
choice = menu_choices()
while choice != "3":
    if choice == "1":
        add_guest(x = input("Enter guest to be added:"), y = input("Enter Guest email address:"))
    elif choice == "2":
        search_email(name = input("Guest name to be searched:"))
    elif choice != ("1", "2"):
        print("enter a valid number between 1-2")
    choice = menu_choices()

