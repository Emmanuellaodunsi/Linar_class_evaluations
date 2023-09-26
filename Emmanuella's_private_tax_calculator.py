#This is a python code that calculates users private tax
name=input("pls......what is your name?")
print("HELLO!....",name ) 
print("Welcome to Emmanuella's mini-calculator for Private tax calculator")
print("This Emmanuella's mini-calculator calculates your private tax , tax percentage and your leftovers for the month ")

#asking the user to input the monthly income
Monthly_income=float(input("pls input your monthly income:"))
#contants percentage for tax
Tax_percentage=10
Tax_percentage_int=int(Tax_percentage)
Tax_deduction= Monthly_income*(Tax_percentage/100)
Left_over=Tax_deduction-Monthly_income


print("Hi!",name,"The leftover for your monthly income is:", Left_over)
print("Thank you for using Emmanuella's mini-calculator for Private tax_calculation :), Wish you all the best.....have a great day;)", name)