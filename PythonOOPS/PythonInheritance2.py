"""
Inheritance : Inheritance means aquaire the properties attribute of class into another.
Single Inheritance
Multilevel Inheritance
Multiple Inheritance
Hierarchical Inheritance
"""
# Multiple Instance:
# A -> B, C->B

class mother:

    def __init__(self, mname, mbusiness):
        self.mname = mname
        self.mbusiness= mbusiness

    def show_mother_details(self):
        print("Mother name :", self.mname)
        print("Mother Business :", self.mbusiness)

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
class son(father, mother):
    def __init__(self, sname, fname, fbusiness, fhouse, mname, mbusiness):
        self.sname = sname
        super().__init__(fname, fbusiness, fhouse)
        self.mobj = mother(mname, mbusiness)

    def show_son_name(self):
        print(f"The son name is : {self.sname}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()


if __name__ == '__main__':
    obj = son('Aditya', 'Rohan', 'Construction Business', '4BHK Bangalore',
              'Pooja', 'Fashion')

    obj.show_father_business()
    obj.show_family_details()
    obj.mobj.show_mother_details()
