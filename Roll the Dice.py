import random
def Dice_Roll():
    v=random.randint(1,6)
    print("Your Dice Value  ", v)
    print("------------------------------")
    print("Do You Want To Continue yes/no")
    yesorno=str(input()).lower()
    if yesorno=="yes":
        Dice_Roll()
    else:
        print("---------------------------")
        print("   |     Thank You     |")
        print("   | Have A Nice Day:) |")
        print("----------------------------")

if __name__ == '__main__':
    print("Welcome To The Game!!")
    print("Type Yes To Roll Your Dice")
    s=input().split()
    Dice_Roll()
