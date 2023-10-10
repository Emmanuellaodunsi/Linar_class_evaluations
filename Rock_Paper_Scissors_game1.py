import random
import time
def play_game(name=input("Enter your name:\n")):
    print(f"Wow",name,"Well played!...That was really fun.....\nYou have got some Rock-paper-scissors skills!")


def instruction():
    return '''Welcome
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

    
    
def get_computer_gesture():
    random.shuffle(Possible_gesture)
    computer_gesture=Possible_gesture[0]
    print("Computer choose :::",computer_gesture)
    return computer_gesture
def determine_winner(user_gesture,computer_gesture):
    if user_gesture==computer_gesture:
        return "It's a tie!"
    elif((user_gesture=="Rock" and computer_gesture=="Scissors") or
         (user_gesture=="Scissors" and computer_gesture=="Paper") or
         (user_gesture=="Paper" and computer_gesture=="Rock")):
        return "You win!"
    else:
        return "Computer win!"
Possible_gesture=["Rock","Paper","Scissors"]
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

instruction_question=input("Are you a new player?,Will you like to get the game instuctions?....Enter just \"yes\" or \"no\"\n")
if instruction_question.lower()=="yes":
    print(instruction())
else:
    pass

time.sleep(5)
print("Lets start!!!")
time.sleep(1)
print("Rock Paper Scissors")
time.sleep(1.5)
print("Rock Paper Scissors")
time.sleep(1.5)
print("Rock Paper Scissors")
time.sleep(1.5)

    
user_score=0
computer_score=0
while True:
    user_gesture=get_users_gesture()
    computer_gesture=get_computer_gesture()
    result=determine_winner(user_gesture,computer_gesture)
    print(result)
    if result=="You win!":
        user_score+=1
    elif result=="Computer win!":
        computer_score+=1
        print(f"You :::{user_score}\nComputer_score :::{computer_score}")
        play_again=input("Do you want to play another round?(yes/no)\n")
        if play_again!="yes":
            print(f"final score is:\nYou :::{user_score}\nComputer :::{computer_score}")
            break
play_game()