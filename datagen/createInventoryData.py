import random
from random import randint, randrange
import sys

counterMax = int(sys.argv[1])
fileName = "inventory.csv"


# sku will just be the counter
# name will be random based on different lists

dressShirtlist = ['Fancy Dress Shirt 1', 'Expensive Dress Shirt 1' , 'Cheap Dress Shirt 1']
dresslist = ['Red Dress', 'Black Dress', 'Fancy Dress 1', 'Purple Dress']
shoeslist = ['Nike', 'Vans', 'Oxford', 'Boot']
sockslist = ['Expensive Sock 1', 'Expensive Sock 2', 'Sport Socks']
tielist = ['Black Tie', 'Bow Tie', 'Cheap Tie']
heelslist = ['Black heels', 'High Heels', 'Low Heels', 'Wedge Heels']
tshirtlist = ['Fancy Tshirt 1', 'Black Tshirt', 'Datastax Tshirt']
jeanslist = ['Levi', 'Lucky', 'Cheap']
coatlist = ['Black', 'Tan', 'Red']
jacketlist = ['Varsity', 'Puff', 'Active']

# location will be spread over 50 states
# number of items will be random
# back order will mostly be N with some Y
# Counter for state will 1-50 then loop
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
listItems=["dressShirt", "dress", "shoes", "socks", 
           "tie", "heels", "tshirt", "jeans", "coat", "jacket"]

f = open(fileName, "w")

counter = 0 
stateCounter = 0
sku = 0
while counter != counterMax:
    counter = counter + 1 
    state = states[stateCounter]

    stock_loc = states[stateCounter]
    for item in listItems:
        sku = sku + 1
        i = randrange(1,3)
        for j in range(0,i):
            sku = sku + 1
            if item == "dressShirt":
               name = random.choice(dressShirtlist)
            if item == "dress":
               name = random.choice(dresslist)
            if item == "shoes":
               name = random.choice(shoeslist)
            if item == "socks":
               name = random.choice(sockslist)
            if item == "tie":
               name = random.choice(tielist)
            if item == "heels":
               name = random.choice(heelslist)
            if item == "tshirt":
               name = random.choice(tshirtlist)
            if item == "jeans":
               name = random.choice(jeanslist)
            if item == "coat":
               name = random.choice(coatlist)
            if item == "jacket":
               name = random.choice(jacketlist)
            
            num_items = randrange(0,200)
            if counter % 100 == 0 and num_items % 3 == 0:
               backorder="Y"
            else:
               backorder="N"
            lineToWrite = str(sku) + "|" + name + "|" + item + "|" + state + "|"+ str(num_items) + "|" + backorder + "\n"
            f.write(lineToWrite)

    if stateCounter == 49:
       stateCounter = 0
    else:
       stateCounter = stateCounter+1
