import random
import re

class Customer:
    def __init__(self,customer_id,name,phone_no):
        self.customer_id = customer_id
        self.name = name
        self.phone_no = phone_no

    def generate_random_id(self):
        cust_id = random.randint(1000,9999)
        return f"TICK{cust_id}"

    def verify_customer_id(customer_id):
        if customer_id[0:4]== "TICK" and customer_id[4:8].isdigit():
            print("Valid Password")
        else:
            print("Invalid Password")

class TicketBooking:
    def __init__(self):
        self.events = {"Concert":{"price":1000,"seats":100},"Movie":{"price":700,"seats":250},"Drama":{"price":500,"seats":200}}
        self.booked_tickets = []

    def view_events():
        for events,details in self.events.items():
            print(f"{events}:{details['price']} per ticket {details['seats']} seats are available")

    def book_tickets(self,event_name,quantity,customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event['seats'] >= quantity:
              totalprice = event['price']*quantity
              event['seats'] -= quantity
              self.booked_tickets.append({"Customer Id":customer.customer_id,"Event":event.name,"Quantity":quantity,"Total price":totalprice,})
            else:
              print("Seats are not Available!!!!!!")
        else:
            print("Event name is not Available")

    def view_tickets(self,customer):
        print("*******Ticket Information*******")
        cus_ticket = [t for t in self.booked_tickets if t["customer_id"]== customer.customer_id]
        if not cus_ticket:
            print("No tickets booked")
        else:
            for tick in cus_ticket:
                print(f"Event:{tick['event']},Quantity:{tick['quantity']},Total cost:{tick['totalprice']}")


if__name__ = "__main__"


book = TicketBooking()
print("***********Welcome to TICKET Booking Application*************")
customer_id = input("Enter the Customer Id:")

if Customer.verify_customer_id(customer_id):
    name = input("Enter your Name:")
    phone_number = int(input("Enter your Phone number:"))
    customer = Customer(customer_id,name,phone_number)
    print("Valid!!!! View the booking details")
else:
    print("Invalid!!!! Please register")
    name = input("Enter your Name:")
    phone_number = int(input("Enter your Phone number:"))
    customer_id  = Customer.generate_random_id()
    customer = Customer(cust_id,name,phone_number)
    print("Your Customer Id id:",customer_id)


while True:
    print("************Booking Information**************")
    print("\n1.View Events")
    print("\n2.book Tickets")
    print("\n3.View my Tickets")
    print("\n4.Exit")
    choice = int(input("Enter any option to continue booking:"))
    if choice == 1:
        book.view_events()
    elif choice == 2:
        event_name = input("Enter any Event:")
        quantity = int(input("Enter the number of tickets:"))
        book.book_tickets(event_name,quantity,customer)
    elif choice == 3:
        book.view_tickets(customer)
    elif choice == 4:
        print("Enter valid Option!")
        
        
                       
