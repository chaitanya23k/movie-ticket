#movie ticket booking
print("Welcome to python movie theatre")
user = input("What is your name? ")
people = int(input("How many people? "))
choice = input("Select the tickets choice please: normal or premium? ")
normal = 150
premium = 300


if choice == "normal":
    ticket_total = people * normal
    gst = ticket_total * 0.05
    price = ticket_total + gst
    print(f"Your ticket price for {people} is {price}")
elif choice == "premium":
    ticket_total = people * normal
    gst = ticket_total * 0.10
    price = ticket_total + gst
    print(f"Your ticket price for {people} is {price}")
else:
    print("Sorry invalid choice")
    


    
    
    
    
print("******Reciept******")
print(f"Customer name: {user}")
print(f"Ticketprice: {ticket_total}")
print(f"Choice: {choice}")
print(f"People: {people}")
print(f"Gst: {gst}")
print(f"Total: {price}")
print("------Enjoy the movie------")
print("******Thank You******")
      
    