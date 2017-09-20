import csv
class School:
    def __init__(self,eits,fellows):
        self.eits=eits
        self.fellows=fellows


class Person:
    def __init__(self,name,nationality):
        self.name=name
        self.nationality=nationality


class Eit(Person):
    def __init__(self,name,fact,nationality):
        super().__init__(name,nationality)
        self.fact=fact

    def nationality_checker(self):
        with open('eits-2018.csv', 'rt') as f:
            reader = csv.DictReader(f)
            for eit in reader:
                if eit.get("nationality") != ["kenya","south africa","ghana","nigeria","ivory coast"]:
                    return None
                else:
                    raise MemoryError("Country not represented")
    def fun_fact(self,fact):
        return self.fact


class Fellow(Person):
    def __init__(self,name,nationality,happiness_level):
        super().__init__(name,nationality)
        self.happiness_level=happiness_level

    def eat(self,happiness_level):
        self.happiness_level +=1


    def teach(self):
        self.happiness_level -=1
eit=Eit("name","fact","nationality")
eit.nationality_checker()
