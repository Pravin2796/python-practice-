class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare 
        self.seats = seats
    def getDetails(self):
        print(f"name of the train is {self.name}")
        print(f"seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"the price of the ticket is :{self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! your seat no is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full! kindly try in tatkal")
intercity = Train("Intercity :",30,300)
intercity.getDetails()
intercity.fareInfo()
intercity.bookTicket()
intercity.getDetails()  
