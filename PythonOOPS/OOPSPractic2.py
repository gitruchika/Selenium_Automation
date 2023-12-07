#from PythonOOPS.OOPSPractice import ABC
from PythonOOPS.OOPSPractice import *


obj = ABC(500, 600)
obj.call_all()
obj.get_city_name()
obj.show_country_name()
print(obj.__module__)


obj_pqr = PQR(400, 700)
obj_pqr.addition()
