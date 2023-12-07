"""
DataHiding/Enpsulation : Data hiding means to hide the class attribute and variable to access outside of the
class.

Datahiding can achieved by declaring variable/methods with single and double underscore as prefix.

-> IF we defined any method or variable with single or double underscore as prefix, then those variable
   and methods will show in suggestion list, after creating the object of the class

->  IF we want to access any  variable/method with single underscore then we can directly access it.

-> If we want to access any variable/method with double underscore then can have to call the class first
   with given example   _<classname>__<variable/method>


"""

class TATA:
    car_color = "Blue"
    _location = "Bangalore"
    __country = "India"

    def __init__(self, car_name, tata_car_price, milege):
        self.car_name = car_name
        self._tata_car_price = tata_car_price
        self.__milege = milege


    def show_car_name(self):
        print(f"The car name is : {self.car_name}")

    def _show_car_price(self):
        print(f"The TATA car price is : {self._tata_car_price}")

    def __show_car_milege(self):
        print(f"The car milege is : {self.__milege}")


if __name__ == '__main__':
    obj = TATA('Harrier', '25 Lac', '15Km/l')
    obj._show_car_price()
    print(obj._location)

    #obj.__show_car_milege()
    obj._TATA__show_car_milege()

"""
Home Work.
Create a class structure of data hiding with School Institute
__Fee
__Result
_Teacher_name
school_name
school_name
"""

str1 = "Good morning"
print(str1.upper())