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
