class GPA_calculator:
    def __init__(self,total_credits):
        self.total_credits=total_credits
    def summation(self,grade_point,credits):
        grade_point=grade_point*credits
        return grade_point
print("\033[0;31;23m Welcome To The GPA Calculator")
print()
print("\U0001f600 \U0001f600 \U0001f600")
total_credits=int(input("\033[0;32;23m Enter the total number of credits\n "))
obj=GPA_calculator(total_credits)
no_of_courses=int(input("Enter the number of courses\n"))
print("\033[0;35;23m If your score of each subject is between the\n"
      "below marks, choose grade points accordingly \n")
print("10     90-100\n"
        "9      80-89\n"
        "8      70-79\n"
        "7      60-69\n"
        "6      50-59\n"
        "0      0-49\n"
        "0      withdraw\n")
s=0
while(no_of_courses!=0):
    no_of_courses-=1
    grade_point=int(input("\033[0;36;23mEnter the Grade Point of Your course\n"))
    credits=int(input("Enter the Credit of the above course\n"))
    GPA=obj.summation(grade_point,credits)
    s=s+GPA
print("Your GPA For This Semester Is ",s/total_credits)
