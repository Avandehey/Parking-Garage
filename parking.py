class parking():

    def __init__(self):
        self.removed_ticket = None
        self.removed_parking = None
        self.tickets = ["ticket1" , "ticket2" , "ticket3" , "ticket4" , "ticket5"]
        self.parking = ["parking1", "parking2", "parking3", "parking4", "parking5"]
        self.current_ticket = {
            "paid" : False
        }


    def driver(self):
            answer = input('will you take a ticket')
            if answer.lower() == "yes":
                return True
            else:
                return False
            


    def take_ticket(self):
        # if user takes ticket, reduce # of ticket by 1
        self.removed_ticket = self.tickets.pop(0)
        # if user takes ticket, reduce # of parking by 1
        self.removed_parking = self.parking.pop(0)


    def pay_parking(self):
        while True:
            answer = input("pay for parking")
            try:
                payed == float(answer)
                self.current_ticket["paid"] = True
                print("Ticket has been paid. You have 15 minutes to leave")
                break
            except:
                payed = None


    def leave_garage(self):
        while True:
            if self.current_ticket["paid"] == True:
                print("Thank you and have a nice day")
                self.removed_ticket.append(self.tickets[0])
                self.removed_parking.append(self.parking[0])
                break
            
            elif self.current_ticket["paid"] == False:
                answer = input("please pay for your ticket")
            else:
                while True:
                    if answer == float(answer):
                        paid = answer
                    else: 
                        paid = None

                        
                    if paid == None:
                        break
                    else:
                        self.current_ticket[paid] = True
                        print("Ticket has been paid. You have 15 minutes to leave")
                        break



parking = parking()
while True:
    # parking.driver()
    if parking.driver() == True:
        parking.take_ticket()
        parking.pay_parking() 
        parking.leave_garage()



