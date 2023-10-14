#This is a python code that calculates users leftovers by deducting the monthly salary from the tax percentage
name=input("pls......Enter your name:\n")
print("HELLO!....",name ) 
print("Welcome to Emmanuella's mini-calculator for Private tax calculator")
print("This mini-calculator calculates your private tax , tax percentage and your leftovers for the month ")

#asking the user to input the monthly income
Monthly_income=float(input("pls input your monthly income:\n"))
#constants percentage for tax
Tax_percentage=10
Tax_percentage_int=int(Tax_percentage)
#multiplying the user monthly salary with the tax percentage
Tax_deduction= Monthly_income*(Tax_percentage/100)
#now deducting the tax from the user monthly income
Left_over=Monthly_income-Tax_deduction

#print out the leftover
print("Hi!",name,"The tax percentage is:",Tax_deduction,"\nAnd the leftover for your monthly income is:", Left_over)
print("Thank you for using Emmanuella's mini-calculator for Private tax_calculation :), Wish you all the best.....have a great day;)", name)
