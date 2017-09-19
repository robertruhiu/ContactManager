class ContactManager:
    def __init__(self, name, phone_number, gender, email_address, postal_address):
        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.email_address = email_address
        self.postal_address = postal_address

    def contact_info(self):
        return self.name, self.phone_number, self.gender, self.email_address, self.postal_address


name = input("What is your name:")
phone_number = int(input("What is your phone number:"))
gender = input("What is your gender:")
email_address = input("What is your email address:")
postal_address = input("What is your postal address:")

new_contact = ContactManager(name, phone_number, gender, email_address, postal_address)
print(new_contact.contact_info())
