class Fellows:
    fellows_created=0

    def __init__(self,name,nationality):
        self.name=name
        self.nationality=nationality
        if Fellows.fellows_created==4:
            raise Exception("we cannot afford to hire {} from {}".format(name,nationality))
        Fellows.fellows_created+=1

    def add_fellows(self,name,nationality):
        self.name=input("enter your name:")
        self.nationality=input("enter your country:")


fellow1=Fellows("dennis","usa")
print(fellow1)

fellow2=Fellows("dennis","usa")
print(fellow2)

fellow3=Fellows("dennis","usa")
print(fellow3)

fellow4=Fellows("dennis","usa")
print(fellow4)

fellow5=Fellows("dennis","usa")
print(fellow5)
