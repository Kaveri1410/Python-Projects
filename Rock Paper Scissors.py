print("Welcome To The Game")
print()
print("Rules: You Need To Enter Your Choice Either Rock/Paper/Scissors \n"
      "       And Then Computer Will Choose One Among Them.....If Either You or Computer win\n"
      "       Both of Your Final Scores Will Be Displayed And The Winner Will Be displayed...:) \n ")
import random
choices=["ROCK","PAPER","SCISSORS"]
n=10
computer=0
human=0
while(n!=0):
    n-=1
    choices2 = random.choice(choices)
    print("Game Starts!! Enter Your Choice")
    choice1=input()
    user_choice=choice1.upper()
    print("computer:", choices2)
    print()
    if user_choice=="ROCK" and choices2=="PAPER" or user_choice=="PAPER" and choices2=="SCISSORS" or user_choice=="SCISSORS" and choices2=="ROCK":
        print("------------------------")
        print("Computer Wins!!")
        print("------------------------")
        computer+=1
    elif user_choice=="PAPER" and choices2=="ROCK" or user_choice=="SCISSORS" and choices2=="PAPER" or user_choice=="ROCK" and choices2=="SCISSORS":
        print("------------------------")
        print("You Have Won!! :)")
        print("------------------------")
        human+=1
    else:
        print("------------------------")
        print("Match Draw!!!")
        print("------------------------")
        computer+=1
        human+=1
    print("Your Score: ",human)
    print("Computer Score: ",computer)
    if computer>human:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print()
        print("   You Have Lost :(...Better Luck Next Time")
        print()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    elif computer<human:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print()
        print("   Hurrah!! You Have Won The Match :)...!!")
        print()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    else:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print()
        print("              Match Draw !!.....")
        print()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
computer=0
human=0
