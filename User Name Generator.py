import random
print('Welcome to username generator')
print("\U0001f600 \U0001f600 \U0001f600 \U0001f600 ")
mail_id=input("Enter Your Mail Id\n")
index1=mail_id.index("@")
number=random.randint(100,1000)
print("Your User Name Is ",mail_id[:index1]+str(number))
