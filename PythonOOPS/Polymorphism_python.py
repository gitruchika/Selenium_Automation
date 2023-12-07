"""
Polymorphism : Polymorphism mean one method performing multiple task

->Method Overriding: When two class have same method name, performing different task, then it is known
                    as method overriding, parent class method will be overide by child class method
-> Method Overloading : When one class has two method with same name and different behavior is known as
                        method overloading, but python does not support method overloading
                        If we defined two methods with same name, then latest or last defined method
                        will be considered.

-> Operator overloading :


"""

class TATA:
    def __init__(self, car_name, tata_car_price):
        self.car_name = car_name
        self.tata_car_price = tata_car_price

    def show_car_name(self):
        print(f"The car name is : {self.car_name}")

    def show_car_price(self):
        print(f"The TATA car price is : {self.tata_car_price}")

class Nexon(TATA):

    def __init__(self, company_name, car_price, car_name, tata_car_price):
        self.cop_name = company_name
        self.car_price  = car_price
        super().__init__(car_name, tata_car_price)

    def show_car_price(self):
        print(f"The nexon car price is : {self.car_price}")

    def show_com_name(self):
        print(f"The car company name : ", self.cop_name)

    def show_com_name(self, comp_name):
        print(f"The car company name is : {comp_name}")

# if __name__ == "__main__":
#     obj = Nexon('TATA Motor', "9.5 Lac", "Nexon Car", "9 Lac")
#     obj.show_car_price()
#     # Here show_car_price() method override the same method name from parent class.
#     obj.show_com_name()


# Operator Overloading
num1 = 30
num2 = 50
print(num1 + num2)

result = num1.__add__(num2)
print("result :", result)

str1 = "Hello"
str2 = "Good Morning"
print(str1 + str2)

result2 = str1.__add__(str2)
print("result 2:", result2)

print(dir(int))
print(dir(str))
print(dir(list))

#### Mutiplication Operator

print("integer :", num1* num2)
print("integer :", num1.__mul__(num2))

print("string :", str1*2)
print("string :", str1.__mul__(2))

list1 = [3, 6, 7]
print("list :", list1*3)
print("list :", list1.__mul__(3))
