class Fellows:
    fellows_created = 0                 #static field

    def __init__ (self, name, nationality):             #class calls this constructor to initiate instances to be used by the object
        if Fellows.fellows_created == 4:                #condition to be met to raise error
            raise Exception("we cannot afford to pay this fellow {} from {}".format(name, nationality))
        else:
            self.name = name
            self.nationality = nationality
            Fellows.fellows_created += 1                #counter to enable the loop

    def __str__ (self):                                         #overides string representation of the class
        return "{}, {}".format(self.name, self.nationality)


fellow1 = Fellows("Pascal", "Congo")
print(fellow1)
fellow2 = Fellows("Francis", "Ghana")
print(fellow2)
fellow3 = Fellows("Andrew", "USA")
print(fellow3)
fellow4 = Fellows("Simphiwe", "South africa")
print(fellow4)
fellow5 = Fellows("Dennis", "Mongolio")
print(fellow5)
