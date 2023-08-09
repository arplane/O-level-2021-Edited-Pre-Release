# TRAIN TIMES

"""
9:00 -> 10:00
11:00 -> 12:00
13:00 -> 14:00
15:00 -> 16:00
"""

# NOTE: LAST TRAIN HAS TWO EXTRA COACHES
# Define Variables
COACHES = 6
seatsPerCoach = 60
costOfTicket = 50
totalSeats1 = seatsPerCoach * COACHES
totalSeats2 = seatsPerCoach * COACHES
totalSeats3 = seatsPerCoach * COACHES
totalSeats4 = seatsPerCoach * COACHES

trainTime = [["9:00", "11:00", "13:00", "15:00"],
             ["10:00", "12:00", "14:00", "16:00"]]

seatsAvailable = [totalSeats1, totalSeats2, totalSeats3, totalSeats4]

totalRevenue = 0

def train1():
    trainNo = 1
    print("How many tickets would you like to book? ")
    tickets = int(input("Enter: "))
    if tickets > seatsAvailable[trainNo]:
        print("Sorry we dont have enough tickets")
        print("Try lowering the ammount of tickets you wanna buy")
    if tickets <= seatsAvailable[trainNo]:
        ticketCost = tickets*costOfTicket
        print("Your tickets have been booked!")
        print("Cost of tickets", ticketCost)
        seatsAvailable[trainNo] - tickets
        print("--------SAFE TRAVELS---------")
        if tickets >= 10:
            freeT = int(tickets/10)
            discount = (freeT*costOfTicket)
            print("Since your group is larger or equal to 10")
            print("Every tenth passenger travels for free")
            finalPrice = ticketCost-discount
            totalRevenue = finalPrice
            print("Your cost will be", finalPrice)
            print("--------SAFE TRAVELS---------")
            
def train2():
    trainNo = 2
    print("How many tickets would you like to book? ")
    tickets = int(input("Enter: "))
    if tickets > seatsAvailable[trainNo]:
        print("Sorry we dont have enough tickets")
        print("Try lowering the ammount of tickets you wanna buy")
    if tickets <= seatsAvailable[trainNo]:
        ticketCost = tickets*costOfTicket
        print("Your tickets have been booked!")
        print("Cost of tickets", ticketCost)
        seatsAvailable[trainNo] - tickets
        print("--------SAFE TRAVELS---------")
        if tickets >= 10:
            freeT = int(tickets/10)
            discount = (freeT*costOfTicket)
            print("Since your group is larger or equal to 10")
            print("Every tenth passenger travels for free")
            finalPrice = ticketCost-discount
            totalRevenue = finalPrice
            print("Your cost will be", finalPrice)
            print("--------SAFE TRAVELS---------")

def train3():
    trainNo = 3
    print("How many tickets would you like to book? ")
    tickets = int(input("Enter: "))
    if tickets > seatsAvailable[trainNo]:
        print("Sorry we dont have enough tickets")
        print("Try lowering the ammount of tickets you wanna buy")
    if tickets <= seatsAvailable[trainNo]:
        ticketCost = tickets*costOfTicket
        print("Your tickets have been booked!")
        print("Cost of tickets", ticketCost)
        seatsAvailable[trainNo] - tickets
        print("--------SAFE TRAVELS---------")
        if tickets >= 10:
            freeT = int(tickets/10)
            discount = (freeT*costOfTicket)
            print("Since your group is larger or equal to 10")
            print("Every tenth passenger travels for free")
            finalPrice = ticketCost-discount
            totalRevenue = finalPrice
            print("Your cost will be", finalPrice)
            print("--------SAFE TRAVELS---------")

def train4():
    trainNo = 4
    print("How many tickets would you like to book? ")
    tickets = int(input("Enter: "))
    if tickets > seatsAvailable[trainNo]:
        print("Sorry we dont have enough tickets")
        print("Try lowering the ammount of tickets you wanna buy")
    if tickets <= seatsAvailable[trainNo]:
        ticketCost = tickets*costOfTicket
        print("Your tickets have been booked!")
        print("Cost of tickets", ticketCost)
        seatsAvailable[trainNo] - tickets
        print("--------SAFE TRAVELS---------")
        if tickets >= 10:
            freeT = int(tickets/10)
            discount = (freeT*costOfTicket)
            print("Since your group is larger or equal to 10")
            print("Every tenth passenger travels for free")
            finalPrice = ticketCost-discount
            totalRevenue = finalPrice
            print("Your cost will be", finalPrice)
            print("--------SAFE TRAVELS---------")

def bookTickets():
    print("Please choose the train yould like to travell in for eg(1, 2, 3)")
    inp = (int(input("Enter: ")))
    if inp == 1:
        train1()
    elif inp == 2:
        train2()
    elif inp == 3:
        train3()
    elif inp == 4:
        train4()


def display():
    print("DEPARTURES")
    for i in range(1):
        print(trainTime[0])
        print("ARRIVALS")
        print(trainTime[1])
        print("Seats Available Per Train")
        print(seatsAvailable)
        bookTickets()

display()