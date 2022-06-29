import locations

print("Welcome to Ride World!!")
print()
locations.services()
while True:
    nationality=input("Please enter your nationality").lower()
    Passport_id=None
    if nationality=='native':
        print("You are native")
        pass
    elif nationality=='foreign':
        print("You are foreign")
        Passport_id=input('Please enter your passport ID ')
    operation=input("Enter your choice")
    if operation=='1':
        print("kookucabs is India’s largest mobility platform and \n"
          "one of the world’s largest ride-hailing  companies,\n"
          "serving 150+ cities across India & USA.The Kookucabs\n"
          "app offers mobility solutions by connecting customers\n "
          "to drivers and  enabling convenience and transparency\n"
          "for hundreds of millions of consumers and over\n "
          "1.5 million driver-partners.\n")

    elif operation=='2':
        print()
        locations.get_info()
        drop_location = input("Enter your drop location\n").lower()
        if locations.get_list().__contains__(drop_location):
            print("There are trips available for ",drop_location)
        else:
            print("Sorry :( there are no trips avaliable for ",drop_location)
    elif operation=='3':
        print()
        print("Welcome to Rental Ride !!")
        locations.get_info()
        print("Thank you for the details!!")
        print("Which package would you like to choose")
        print("1.1hr=15km\n"
              "2.2hr=30km\n"
              "3.4hr=40km\n"
              "4.6hr=60km\n"
              "5.8hr=80km\n")
        choice=int(input())
        print("Booking confirmed !! Happy Journey....")
    elif operation=='4':
        break
def get_list():
    location=['tnagar','marinabeach','vellankani shrine','guindy national park','meenabakkam','saidapet','adyar',
    'ashoknagar','Teynampet']
    return location
def get_info():
    name = input("Enter your name\n")
    phn_no = int(input("Enter your mobile number\n"))
    pickup_location = input("Enter your pickup location \n").lower()
    pickup_time = input("Enter pickup time\n")
    pets = input("Do you need to carry your pets yes/no\n").lower()
    luggage = input("Do you carry any luggages with you yes/no\n").lower()
    if (luggage == 'yes'):
        luggage_count = input("Please specify the count of luggages (1-20)\n")
    passengers = int(input("How many members do you travel(1-20)\n"))
def services():
    print('1.About us\n'
          '2.Find Ride\n'
          '3.Rental Ride\n'
          '4.Quit\n')
