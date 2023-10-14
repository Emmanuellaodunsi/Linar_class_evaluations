print("Welcome to Emmanuella age calculator...\nThis calculator calculates your age and and classify you base on your age\n")
def age_calculator(name,present_year,birth_year):            
    """the age_calculator() function calculates age and and classify the user base on your age /
    it take 3 parameter
    name=str, pyear = present year, byear = birth year"""
    
    #calculating the age
    age = int(present_year) - int(birth_year)
    #giving conditions to classify a person base on their age
    if age >0 and age<6:
        print("Hello :)",name,"you are",age,"year old and you are a kid")
    elif age >6 and age<13:
        print("Hello :)",name,"you are",age,"year old and you are a kid") 
    elif age >13 and age<20:
        print("Hello :)",name,"you are",age,"year old and you are a teenage")
    elif age >20 and age<35:
        print("Hello :)",name,"you are",age,"year old and you are a young adult")
    elif age >35 and age<100:
        print("Hello :)",name,"you are",age,"year old and you are a adult")
    else:    
        print("pls enter a valid age")
age_calculator(name =input("Enter your name:\n"),present_year =input("Enter the present year:\n"),birth_year =input("Enter your birth year:\n"))
