"""
Inheritance : Inheritance means aquaire the properties attribute of class into another.
Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Hierarchical Inheritance
"""


# Hierarchical Instance:
# A -> B,  A -> C

class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"My father name is : {self.fname}")

    def show_father_business(self):
        print(f"Father owns : {self.fbusiness}")

    def show_father_house(self):
        print(f"My father has : {self.fhouse}")


# MRO : Method resolution order
class Child1(father):
    def __init__(self, sname, fname, fbusiness, fhouse):
        self.sname = sname
        super().__init__(fname, fbusiness, fhouse)

    def show_son_name(self):
        print(f"The son name is : {self.sname}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()


class Child2(father):
    def __init__(self, sname, fname, fbusiness, fhouse):
        self.sname = sname
        super().__init__(fname, fbusiness, fhouse)

    def show_son_name(self):
        print(f"The son name is : {self.sname}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()


if __name__ == '__main__':
    obj1 = Child1('Aditya', 'Rohan', 'Construction Business', '4BHK Bangalore')

    obj1.show_father_business()
    obj1.show_family_details()
    print("_" * 50)
    obj2 = Child2('Rahul', 'GuptaJi', 'Cloth Brand', 'Bangalow')
    obj2.show_father_house()
    obj2.show_family_details()
