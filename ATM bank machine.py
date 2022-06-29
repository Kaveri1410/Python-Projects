class ATM:
    def __init__(self,bal=0):
        self.bal=bal
    def balance(self):
        return self.bal
    def withdraw(self,money):
        self.bal-=money
        if self.bal<0:
            self.bal=0
            return 0
        return self.bal
    def deposit(self,money1):
        self.bal+=money1
        return self.bal

obj=ATM()
print("\033[0;35;23m   WELCOME TO THE ATM    ")
print("\U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600 \U0001f600")
print()
print("Please insert your ATM card properly")
print()
print("Enter Your PIN")
pin_number=int(input())
print("Your PIN number is correct....Your can proceed now!!")
n=1
while(n!=0):
    print("        Your choices are:     ")
    print("\n")
    print("1)        Balance")
    print("2)        Withdraw")
    print("3)        Deposit")
    print("4)        Quit")
    print("\n")
    print()
    print("Enter Option: ")
    choice=int(input())
    bal=100000
    if choice==1:
        print("----------------------------------------------------------------")
        print()
        print("Your Balance is : ",obj.balance())
        print()
        print("----------------------------------------------------------------")
    elif choice==2:
        money=int(input("Enter money to withdraw "))
        if money>bal:
            print("----------------------------------------------------------------")
            print()
            print("Sorry your money exceed your bank balance")
            print()
            print("----------------------------------------------------------------")
            print()
            print("Your bank balance is: ",obj.balance())
            print()
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print()
            print("Your current balance is: ",obj.withdraw(money))
            print()
            print("----------------------------------------------------------------")
    elif choice==3:
        money1=int(input("Enter money to deposit "))
        print("----------------------------------------------------------------")
        print()
        print("Your current balance is: ", obj.deposit(money1))
        print()
        print("----------------------------------------------------------------")
    elif choice==4:
        print("Have A Good Day :)")
        break
    else:
        print("Invalid choice")
