class School:
    def __init__(self,eits,fellows):
        self.eits=eits
        self.fellows=fellows


class Person:
    def __init__(self,name=None,nationality=None):
        name=[]
        self.name=name
        nationality=[]
        self.nationality=nationality


class Eit(Person):
    def __init__(self,name,fact,nationality):
        super().__init__(name,nationality)
        self.fact=fact
        for eit in self.nationality:
            if nationality in nationality == nationality["Kenya","Nigeria","Ghana","South afica","Ivory coast"]:
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
        return self.happiness_level


    def teach(self,happiness_level):
        return self.happiness_level
