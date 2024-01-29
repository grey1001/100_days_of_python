from replit import clear
print("Welcoome to the blind auction")

bidders = {}
other_bidders = "yes"

while other_bidders == "yes":	
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid # this part adds the name and bid to the dictionary
    other_bidders = input(f"Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "yes":
        clear()

highest_bid = max(bidders, key=bidders.get)
print(f"The winner is {highest_bid} with a bid of ${bidders[highest_bid]}")