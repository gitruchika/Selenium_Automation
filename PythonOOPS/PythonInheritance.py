"""
Inheritance : Inheritance means aquaire the properties attribute of class into another.
Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Hierarchical Inheritance
"""
# single Inheritance
# father -> Son
"""
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


class son(father):
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
    obj = son('Aditya', 'Rohan', 'Construction Business', '4BHK Bangalore')

    obj.show_father_business()
    obj.show_family_details()
"""

# multi level Inheritance.

# Class A -> CLass B->  Class C


class grand_father:
    def __init__(self, gfname, land):
        self.gname = gfname
        self.land = land

    def show_grandfahter_details(self):
        print("grand")
class father(grand_father):
    def __init__(self, fname, fbusiness, fhouse, gfname, land):
        super().__init__(gfname, land)
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"My father name is : {self.fname}")

    def show_father_business(self):
        print(f"Father owns : {self.fbusiness}")

    def show_father_house(self):
        print(f"My father has : {self.fhouse}")


class son(father):
    def __init__(self, sname, fname, fbusiness, fhouse, gfname, land):
        self.sname = sname
        super().__init__(fname, fbusiness, fhouse, gfname, land)

    def show_son_name(self):
        print(f"The son name is : {self.sname}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()


if __name__ == '__main__':
    obj = son(sname='john', fname='Henney', fbusiness='fasion', fhouse='4BHK',
              gfname='Rajesh', land='400Acr' )
    obj.show_family_details()
    print(obj.land)
    obj.show_grandfahter_details()
