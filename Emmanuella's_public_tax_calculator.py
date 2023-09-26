#this is a python code that 
NAME=input("pls......what is your name?")
print("HELLO!....",NAME ) 
print("Welcome to Emmanuella's mini-calculator for Public tax calculator")
print("This Emmanuella's mini-calculator calculates your public tax , tax percentage and your leftovers for the month ")


Monthly_income=float(input("pls input your monthly income:"))
Tax_percentage=8
Tax_percentage_int=int(Tax_percentage)
Tax_deduction= Monthly_income*(Tax_percentage/100)
Left_over=Monthly_income-Tax_deduction


print("Hi!",NAME,"The leftover for your monthly income is:", Left_over)
print("Thank you for using Emmanuella's mini-calculator for Private tax_calculation :), Wish you all the best.....have a great day;)", NAME)