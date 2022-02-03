from gettext import find
import art

print(art.logo)
bid_item = {}
def add_bid(name,bid_price):
    bid_item[name]=bid_price

def find_highest_price(bid_item):
    highest_price = 0
    final_bid_owner = ""
    #print(auction_list)
    for item in bid_item:
        bid_item_price = bid_item[item]
        if  bid_item_price > highest_price:
            highest_price = bid_item_price
            final_bid_owner = item

    print(f"The winner is {final_bid_owner} and bid price is {highest_price}")

want_to_bid = True
while want_to_bid:
    name = input("what is your name? ")
    bid_price = int(input("please input bid price: "))
    add_bid(name, bid_price)
    continue_bid = input("if there are other users who want to bid? ")
    if continue_bid.lower() == "no" and continue_bid != "":
        want_to_bid = False
       
find_highest_price(bid_item)