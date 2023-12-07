"""
Class : Class is blueprint of the object is being created.
Object : Object is entity through which we can access all the properties
         attribute of the class.
Method : Function definition which belong the class known as method.
         -> Object/instance method
         -> Class method
         -> static method.
Constructor : Constructor which initialize the memory of the object.
           -> Default constructor
           -> Parameterize constructor

Variables : -> Instance Variable
            -> Class variable

Inheritance
Polymorphism
Data Hiding
Abstraction.
"""


# class
class PQR:
    # constructor
    def __init__(self, var1, var2):
        print("The object is successfully created")
        self.var1_val = var1  # instance variable
        self.var2_val = var2  # instance variable

    def greeting(self):  # method
        print("Hello Good Morning")

    def addition(self):  # instance method
        print("addition of variable values :", self.var1_val + self.var2_val)

    def square(self, num):
        print("Square of num :", num ** 2)

    def call_all(self):
        self.greeting()
        self.addition()
        self.square(40)


# object
#obj = ABC(30, 40)
#obj.greeting()
#print(obj.__class__)
#print(obj.__module__)
# obj.addition()
# obj.square(4)
#obj.call_all()

"""
Home work,
1. Create class with name car, with parameter car_name, car_company, car_price
    -> show_car_name()
    -> show_car_price()
    -> show_car_company()
    
2. Create class with name fruits with fruit_name, fruit_price, fruit_color
   -> show_fruit_name()
   -> show_fruit_price()
   -> show_fruit_color()
   -> show_fruit_details()
"""

# What is self?
# self is nothing but a object of the class is being created.
"""
class xyz:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Value of name variable :", self.name)

    def greeting(self):
        print("Very good morning")
        self.show_name()

obj = xyz('John')
obj.greeting()

xyz.greeting(obj)
"""

################################################

class ABC:
    city = "Mumbai" # class variable
    Country = "India" # class variable

    # constructor
    def __init__(self, var1, var2):
        print("The object is successfully created")
        self.var1_val = var1  # instance variable
        self.var2_val = var2  # instance variable

    def greeting(self):  # method
        print("Hello Good Morning")

    def addition(self):  # instance method
        print("addition of variable values :", self.var1_val + self.var2_val)

    def square(self, num):
        print("Square of num :", num ** 2)

    def get_city_name(self):
        print("city name :", self.city)

    def show_country_name(self):
        print("Country Name :", self.Country)

    def call_all(self):
        self.greeting()
        self.addition()
        self.square(40)


if __name__ == '__main__':
    print("_"*50)
    obj = ABC(100, 300)
    obj.get_city_name()
    obj.show_country_name()
    obj.Country = "USA"
    obj.city = "Bangalore"
    obj.show_country_name()
    obj.get_city_name()
    print(__name__)
    print(obj.__module__)
    print("_"*50)

