#This is a python code that calculates a users public tax ,tax percentage,and leftover for the month.
#Get the user name
name=input("pls......Enter your name:\n")
#Welcome the user
print("HELLO!....",name) 
print("Welcome to Emmanuella's mini-calculator for Public tax calculator")
print("This mini-calculator calculates your public tax , tax percentage and your leftovers for the month ")
#Get the monthly income.
Monthly_income=float(input("pls input your monthly income:"))
#Constant tax percentage
Tax_percentage=0.08
#Calculate the public tax 
public_tax= Monthly_income*Tax_percentage
#Calculate the tax percentage
tax_percentage=public_tax/Monthly_income
#Calculate the leftover for the month.
Left_over=Monthly_income-public_tax

#Print the user's public tax,tax percentage,and leftover for the month
print("Hi!",name,"The leftover for your monthly income is:", Left_over,"\nThe public tax is:",public_tax,"\nThe tax percentage is:",tax_percentage)
print("Thank you for using Emmanuella's mini-calculator for Private tax_calculation :), Wish you all the best.....have a great day;)", name)