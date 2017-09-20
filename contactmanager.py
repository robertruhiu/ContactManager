import csv


class Contact :  # we use the object Contact to store the class attributes name and number
    name = ""
    number = ""

    def __init__ ( self , name , number ) :
        pass


def menu_choices ( ) :  # initiating an instance of menu choices to loop in the cli
    print ( "1. Add new contact" )
    print ( "2. Print all contacts" )
    print ( "3. Delete contact" )
    print ( "4. Search contact" )
    return input ( "Please enter your choice (1-4): " )


def add_contact ( ) :  # add a new contact using this function
    contact = Contact ( )
    contact.name = input ( "Enter contact name: " )
    contact.number = input ( "Enter contact number: " )
    contactList.append ( contact )
    print ( "Contact added." )


def print_contact ( ) :  # allows for seeing contacts stored
    print ( "Printing contacts..." )
    for items in contactList :
        print ( items.name + ", " + items.number ) ,


def search_contact ( name ) :  # search for contact stored in the list in object
    for items in contactList :  # using items to loop in the list using name
        if items.name == name :
            print ( items.name + ", " + items.number ) ,
    print ( )


def delete_contact ( name ) :  # function to delete an item in contact list
    for index , items in enumerate ( contactList ) :  # Iterates over (index(name), item(number)) pairs, for all items
        if items.name == name :  # in iterable.
            del contactList [ index ]
            print ( "contact deleted" )
        else :
            print ( "contact not found" )
    print ( )


f = open ( 'let.txt' , 'r' )
x = f.readlines ( )
contactList = x  # to store the values of the contact infomation
choice = menu_choices ( )
while choice != "5" :
    if choice == "1" :
        add_contact ( )
    elif choice == "2" :
        print_contact ( )
    elif choice == "4" :
        search_contact ( input ( "input name to search:" ) )
    elif choice == "3" :
        delete_contact ( input ( "input contact name to be deleted:" ) )
    elif choice != ("1" , "2" , "3" , "4") :
        print ( "enter a valid number between 1-4" )
    choice = menu_choices ( )
