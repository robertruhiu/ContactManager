class Driver:
    def __init__(self,name,license_check):
        self.name=name
        self.license_check=license_check


class Student:
    def __init__(self,name):
        self.name=name

class SchoolBus:
    def __init__(self):
        self.student_list=[]
        self.driver_list=[]

    def add_students(self,stu):
        self.student_list.append(stu)

    def add_driver(self,wheel):
        self.driver_list.append(wheel)

    def drive(self):
        if len(self.student_list)==10 and len(self.driver_list)==1:
            print("bus can go")
        else:
            print("bus is not to capacity cannot leave")


if __name__ == "__main__":
    school_bus=SchoolBus()
    for _ in range(10):
        school_bus.add_students(Student("Tom"))
    school_bus.add_driver(Driver("Nana",True))
    school_bus.drive()