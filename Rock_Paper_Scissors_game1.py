import random
import time
#imports the 'random' and 'time' modules and 
#prints the initial message to introduce the game"""
print("Rock......Paper......Scissors game")
def play_game(name=input("Hello....pls enter your name:\n")):
    print(f"Wow",name,"Well played!...That was really fun.....\nYou have got some Rock-paper-scissors skills!")




"""Creating an instruction function,
 which returns the game's instructions as a multi-line string."""
def instruction():
    return '''Welcome to Rock Paper Scissors game!
            In this game ,you will play against another player(computer).
            Each player will choose one of the followng gestures:
            Rock.....Paper......or scissors.
            The rules are simple:
            Rock beats Scissors,
            Scissors beats paper,
            and Paper beats Rock.
            If both player choose the same gesture,it is a tie!
            You will play multiply rounds,and we will track of your scores.
            The first player to reach a certain score wins the game.
            Now lets get started and have some fun....'''


    
"""Creating the get_computer_gesture function.....It randomly shuffles the list
of Possible_gesture, selects a gesture for the computer,
 and prints the computer's choice"""
def get_computer_gesture():
    random.shuffle(Possible_gesture)
    computer_gesture=Possible_gesture[0]
    print("Computer choose :::",computer_gesture)
    return computer_gesture


"""Creating a function which determines the winner of a round based on the user's and computer's gestures, 
following the rock-paper-scissors rules"""
def determine_winner(user_gesture,computer_gesture):
    if user_gesture==computer_gesture:
        return "It's a tie!"
    elif((user_gesture=="Rock" and computer_gesture=="Scissors") or
         (user_gesture=="Scissors" and computer_gesture=="Paper") or
         (user_gesture=="Paper" and computer_gesture=="Rock")):
        return "You win!"
    else:
        return "Computer win!"
    
"""Creating a list called Possible_gesture with the possible choices for both the user and the computer"""
Possible_gesture=["Rock","Paper","Scissors"]

"""Defines the get_users_gesture function,which takes input from the user to choose a gestureand provides the result based on their choice"""
def get_users_gesture():
    user_gesture=int(input("Now choose your gesture\nInput 1 for Rock\nInput 2 for Paper\nInput 3 for Scissors\n"))
    if user_gesture==1:
        print("You choose ::: Rock")
        return 'Rock'
    elif user_gesture==2:
        print("You choose ::: Paper")
        return 'Paper'
    elif user_gesture==3:
        print("You choose ::: Scissors")
        return 'Scissors'
    else:
        print("Pls choose a valid input....you can only choose between 1 to 3\n1 for Rock\n2 for Paper\n3 for Scissors")
        return user_gesture
    

"""Asks the user if they are a new player and if they want to read the game instructions.
If the response is "yes," it prints the instructions, if "no" it moves to the next step"""
instruction_question=input("Are you a new player?,Will you like to get the game instuctions?....Enter just \"yes\" or \"no\"\n")
if instruction_question.lower()=="yes":
    print(instruction())
else:
    pass

"""This line of code introduces a countdown before the game starts using time.sleep."""
time.sleep(5)
print("Lets start!!!")
time.sleep(1)
print("Rock Paper Scissors")
time.sleep(1.5)
print("Rock Paper Scissors")
time.sleep(1.5)
print("Rock Paper Scissors")
time.sleep(1.5)

"""Creating variables to keep track of the user and computer scores"""   
user_score=0
time.sleep(1)
computer_score=0

"""This is the main game loop....It repeatedly asks the user for their gesture,generates the computer's gesture, and determines the winner....
It then updates the scores and asks if the user wants to play another round...The loop continues until the user decides not to play again."""
while True:
    user_gesture=get_users_gesture()
    computer_gesture=get_computer_gesture()
    result=determine_winner(user_gesture,computer_gesture)
    print(result)
    if result=="You win!":
        user_score+=1
    elif result=="Computer win!":
        computer_score+=1
        print(f"Your score :::{user_score}\nComputer_score :::{computer_score}")
        play_again=input("Do you want to play another round?(yes/no)\n").lower()
    
        if play_again!="yes":
            print(f"final score is:\nYou :::{user_score}\nComputer :::{computer_score}")
            break
"""Calling the play_game function, which prints a concluding message based on the user's name provided at the beginning"""
play_game()
