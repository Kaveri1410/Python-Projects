def Hangman(count):
    if count==1:
        print(" --- \n"
              " |  |\n"
              " |   \n"
              " |   \n"
              " |   \n")
    if count==2:
        print(" --- \n"
              " |  |\n"
              " |  o\n"
              " |   \n"
              " |   \n")
    if count==3:
        print(" --- \n"
              " |  |\n"
              " |  o\n"
              " |  |\n"
              " |  |\n")
    if count==4:
        print(" --- \n"
              " |  |\n"
              " |  o\n"
              " | /|\\\n"
              " |  |\n")
    if count==5:
        print(" --- \n"
              " |  |\n"
              " |  o\n"
              " | /|\\\n"
              " | /|\\\n")
print("Your Chances are over :(.....You Are Dead:(")

if __name__ == '__main__':
    print("WELCOME TO THE HANGMAN aGAME !! :)")
    print("********************************************************")
    print("RULES: You will be given a topic \n "
          "under which, a word will be given whose count will also be given as dashes \n"
          "and you need guess the word by, one by one letters\n"
          "you will be given only 5 chances!!")
    print("********************************************************")
    print("Lets Start The Game:)")
    import random
    topics=["fruits","animals","actors","actress","sportsname","food"]
    topic=random.choice(topics)
    print("Your Topic Is: ",topic)
    if topic=="fruits":
        words=["pomegranate","plums","pineapple","banana","watermelon","blueberry"]
        word=random.choice(words)
    if topic=="animals":
        words=["tiger","hippopotamus","elephant","giraffe","kangaroo","gorilla"]
        word = random.choice(words)
    if topic=="actors":
        words=["kamalhaasan","rajinikanth","shivajiganesan","sivakarthikeyan","vikram","ajithkumar"]
        word = random.choice(words)
    if topic=="actress":
        words=["shruthihaasan","keethysuresh","sridevi","saipallavi","nayanthara","hanshikamotwani"]
        word = random.choice(words)
    if topic=="sportsname":
        words=["cricket","hockey","tennis","throwball","shuttlecock","basketball"]
        word = random.choice(words)
    if topic=="food":
        words=["paneerbuttermasala","parotta","chappathi","friedrice","panipuri","sandwich"]
    word = random.choice(words)
    length_of_word=len(word)
    print("******************************")
    print("Dashes Count are:")
    print("_"*length_of_word)
    dashes="_" * length_of_word
    st=list(dashes)
    print("The word is made up of ",length_of_word,"letters")
    print("You Can Start Your Guesses:)")
    print()
    n=5
    count=0
    indices=[]
    while n!=0:
        n-=1
        count+=1
        guess = input("Enter a letter")
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    st[i]=guess
            print(*st)
            print()
            print("Correct guess!!Did You Find The Word ??")
            yesorno=input("Type yes/no").lower()
            print("********************************************************")
            if yesorno=='yes':
                print("Enter The Word (No space in between)")
                correct=input().lower()
                if correct==word:
                    print("********************************************************")
                    print("           Hurrah!!Your Guess Is Correct:)")
                    print("********************************************************")
                    break
                else:
                    print("OOPS!!,Your Guess Is Wrong:( ")
                    print("****************************************")
                    Hangman(count)   
            else:
                print("You Have Only Few More Chances Left :|")
                print("********************************************************")
        else:
            print("OOPS!!,Your Guess Is Wrong:( ")
            print("********************************************************")
            Hangman(count)
