def user_name(name=input("Enter your name:\n")):
    global user_name
    print("Hello",name,"welcome to Emmanuella mini calculator")
    print("This mini-calculator only performs the 7 arithemetic operators:\nAddition +\nSubration -\nDivision /\nMultiplication *\nPower(exponential) **\nFloor divison //\nSquare root\n")
    print("The symbol for the Square-root arithmetic operator is: \"**1/ your second value\"")
user_name()
def addition(value1,value2):
    return value1+value2

def subraction(value1,value2):
    return value1-value2

def division(value1,value2):
    return value1/value2

def multiplication(value1,value2):
    return value1/value2

def floor_division(value1,value2):
    return value1//value2

def exponential(value1,value2):
    return value1**value2

def squareroot(value,rootvalue):
    return value**(1/rootvalue)

def calculate():
    firstvalue=float(input("Pls enter your first value:\n"))
    secondvalue=float(input("Pls enter your second value:\n"))
    operators=input("pls choose the operators you will like to perform on: (+,-,/,*,**,//,squareroot)\n")
    if operators=="+":
        print("The addition of the two value is",addition(value1=firstvalue,value2=secondvalue))
    elif operators=="-":
        print("The subtraction of the two value is",subraction(value1=firstvalue,value2=secondvalue))
    elif operators=="/":
        print("The division of the two value is:",division(value1=firstvalue,value2=secondvalue))
    elif operators=="*":
        print("The multiplication of the two value is:",multiplication(value1=firstvalue,value2=secondvalue))
    elif operators=="**":
        print("The exponential of the two value is:",exponential(value1=firstvalue,value2=secondvalue))
    elif operators=="//":
        print("The floor division of the two values is:",floor_division(value1=firstvalue,value2=secondvalue))
    elif operators=="squareroot":
        print("The squareroot of the value is:",squareroot(value=firstvalue,rootvalue=secondvalue))
    else:
        print("Dear...",user_name,"pls enter a valid operator")
    print("Thank for using Emmnauella mini calculator")
calculate()

