#create an algorthm to solve this equation: Y=L-F*W[S*L/F+(20/F)*N]/20*W+F**0.5
#START                                   #STEP 1
V_L=int(input("Enter the value for L:")) #STEP 2
V_F=int(input("Enter the value for F:")) #STEP 3
V_S=int(input("Enter the valu for S:"))  #STEP 4
V_w=int(input("Enter the value for w:")) #STEP 5
V_n=int(input("Enter the value for n:")) #STEP 6

#square the value for "F" with the value for "w"
value_1=V_F**V_w                         #STEP 7

#multiply the value for "S" with the value for "L" , and then divide it with the value for "F"
value_2=V_S*V_L                          #STEP 8
value_3=value_2/V_F                      #STEP 9

#divide 20 with the value for for "F" ,and then square it with the value for "n"
value_4=20/V_F                           #STEP 10
value_5=value_4**V_n                     #STEP 11

#add the solution from step 9 and step 11 together and then multiply it with the solution from step 7
value_6=value_3+value_5                  #STEP 12
value_7=value_1*value_6                  #STEP 13

#calculate the first part of the denominator "20**w"
value_8=20**V_w                          #STEP 14
#then square the value for F
value_9=V_F**0.5                         #STEP 15

#add the solution gotten from step 14 and step 15
value_10=value_8+value_9                 #STEP 16

#divide the solution gotten from step 13 by step 16
division=value_7/value_10                #STEP 17

#multiply step 7 by step 17
multiply=value_1*division                #STEP 18


#subtract the value of "L" from step 18
SOLUTION=V_L-multiply                    #STEP 19

#assign the solution from step 19 to a variable "Y"
Y=SOLUTION                               #STEP 20
print("The solution to the equation is:", Y) #STEP 21

#END 