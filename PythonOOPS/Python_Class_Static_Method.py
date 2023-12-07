class Car:
    city = "Mumbai" # class variable
    Area = "Bandra" # class variable

    def __init__(self, car_name, car_price, car_comp):
        self.car_name = car_name # Instance variable
        self.car_price = car_price # Instance variable
        self.car_comp = car_comp # Instance variable


    # instance method/ object method
    def show_car_details(self):
        print("Car name :", self.car_name)
        print("Car price :", self.car_price)
        print("Car Company :", self.car_comp)

    # class method
    @classmethod
    def show_car_dealer(cls):
        print("Dealer city :", cls.city)
        print("City Area :", cls.Area)


    @staticmethod
    def show_car_milege(milege):
        print(f"The car milege is :{milege}")



if __name__ == '__main__':
    # obj = Car('Harrier', '30 Lac', 'TATA')
    # obj.show_car_details()
    # obj.show_car_dealer()
    # obj.show_car_milege("20 KM/L")

    #We can call the static method, without creating the object of the class.
    Car.show_car_milege("25 MK/L")

    Car.show_car_dealer()
