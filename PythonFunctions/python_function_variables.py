"""
global variable : The variable we declare outside the functions, then it is known as global variable
#                  Scope of global variable is across the module.
local variable : The variable we declare inside the function, then it is known as local variable
#                Scope of local variable is limited to function only.
non local variable :
"""
# global variable
varp = 1000

def function1():
    global varp
    varq = 700 # local variable
    varp = 1200 # local variable
    print("varq local:", varq)
    print("varp global :", varp)


def function2():
    vars = 600 # local variable
    print("vars local:", vars)
    print("varp global :", varp)


function2()
print("_"*50)
function1()
print("_"*50)
function2()


# non local variable

varx = 1234 # global variable

def outer_function():
    vary = 1600 # non-local variable

    def inner_function():
        print("_______Inner Function1________")
        nonlocal vary
        vary = 2000
        varz = 1000 # local variable
        print("global varx :", varx)
        print("non local vary :", vary)
        print("local varx :", varz)

    def inner_function2():
        print("_______Inner Function2________")
        varu = 999  # local variable
        print("global varx :", varx)
        print("non local vary :", vary)
        print("local varx :", varu)

    inner_function2()
    print("_"*50)
    inner_function()
    print("_" * 50)
    inner_function2()

outer_function()