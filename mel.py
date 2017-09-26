import csv
import os.path
import smtplib


mydict = {}

with open('contacts.csv', mode = 'r') as infile:
    reader = csv.reader(infile)
    mydict = { rows [ 0 ]:rows [ 1 ] for rows in reader }


def menu_choices ( ):  # initiating an instance of menu choices to loop in the cli
    print("1. Add new guest")
    print("2. Search contact")
    return input("Please enter your choice (1-2): ")


def add_guest (name, email):
    mydict [ name ] = email


def search_email (name):
    if mydict.get(name)==mydict.get(name) != None:
        print("{}:: {}".format(name, mydict.get(name)))
    else:
        print("Email not found")

x = mydict.values()
for k in x:
    print (k)

TO=k
SUBJECT='Unwise quotes through smtplib '
TEXT='Creativity is when a stupid clever soul gets up from bed and does amazing things that makes the world think he is wise.'
user = 'robertruhiu@gmail.com'
password = '***********'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user, password)

BODY = '\r\n'.join([
    'To: %s' % TO,
    'From: %s'% user,
    'Subject: %s'% SUBJECT,
    '',
    TEXT
    ])
try:
    server.sendmail(user,[TO],BODY)
    print('email sent')
except:
    print('error sending email')

choice = menu_choices()
while choice != "3":
    if choice == "1":
        name = input('Your name: ')
        email = input('Your email: ')
        file_exist = os.path.exists('contacts.csv')
        with open('contacts.csv', 'a') as csv_file:
            headers = [ 'name', 'email' ]
            writer = csv.DictWriter(csv_file, headers)

            if not file_exist:
                writer.writeheader()

            writer.writerow({ 'name':name, 'email':email })
    elif choice == "2":
        search_email(name = input("Guest name to be searched:"))
    elif choice != ("1", "2"):
        print("enter a valid number between 1-2")


    print(mydict.values())
    choice = menu_choices()
