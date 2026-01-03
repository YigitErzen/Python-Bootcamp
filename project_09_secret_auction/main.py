import art

print(art.logo)

flag = True

bids = {}

while(flag):
    name = input("What is your name?: ")
    bid = float(input("What is your bid? $"))

    bids[name] = bid

    any_other_bid = input("Are there any other bidders? Type 'yes or 'no'").lower()

    if(any_other_bid == "yes"):
        print("\n" * 100)
    else:
        flag = False

highest_bid = 0
highest_bid_owner =""

for key in bids:
    if(bids[key] > highest_bid):
        highest_bid_owner = key
        highest_bid = bids[key]

print("\n" * 100)
print(f"The winner is {highest_bid_owner} with {highest_bid}$")

