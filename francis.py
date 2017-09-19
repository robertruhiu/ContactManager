class Person:
    def __init__(self, name, gender):
        if name == "Francis":
            raise ValueError("What kind parent")
        else:
            self.__name = name
            self.__gender = gender

    def __repr__(self):
        return "This person is a {} named {}".format(self.__name, self.__gender)


totally_not_francis = Person("Frank", "M")
totally_not_francis.__name = "Francis"
print(totally_not_francis.__dict__)
