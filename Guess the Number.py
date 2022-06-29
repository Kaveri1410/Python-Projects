import random
def Guess_Number():
    n=5
    k=0
    v=random.randint(6,100)
    while (n != 0):
        n-=1
        k+=1
        print("Enter A Number Between 1 and 100")
        num=int(input())
        differnce=abs(num-v)
        highnum=v+5
        lownum=v-5
        if num>highnum:
            print("Your Guess Is Too High :(")
        elif num<lownum:
            print("Your Guess Is Too Low :(")
        elif differnce<10 and differnce>=1:
            print("Your Guess Is Nearer But Try Again :|")
        else:
            print("Your Guess Is Correct :)")
            break
    print("The Answer is ", v)
    return k
def Grade(k):
    if k==1:
        print("Grade A Excellent :)")
    elif k==2:
        print("Grade B Very Good")
    elif k==3:
        print("Grade C Good")
    elif k==4:
        print("Grade D Can Do Better ")
    else:
        print("Chances Over :( \n"
                      "Better Luck Next Time")

if __name__=="__main__":
    print("Welcome To The Game!!")
    print("___________________________________________________")
    print("Rules: The System Will Keep A Number In Its Mind\n"
          " And You Need To Find It Within 5 Guesses \n"
          "Clues Will Be Provided After The First Guess \n"
          "Grade Will Also Be Displayed \n")
    print("___________________________________________________")
    print("To Continue Type Y/N")
    yesorno=str(input()).upper()
    l=Guess_Number()
    Grade(l)
