
import random
from random import randint, randrange
import sys

counterMax = int(sys.argv[1])
TEST = False
fileName = "customer.csv"
if len(sys.argv) > 2:
   if str(sys.argv[2]) == "test":
      TEST = True
      fileName = "customerTest.csv"


# id will be just 1-100000 with a counter
# name will just be customer<counter>
# gender will be random from list
genderList = ["M", "F"]
# Age will be random from range 18-90
# Counter for state will 1-50 then loop
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
# homestore will be same counter as for state
# number of items with equal random number from 2-5
listItems=["dressShirt", "dress", "shoes", "socks", 
           "tie", "heels", "tshirt", "jeans", "coat", "jacket"]
# year random between 2016-2018
# month random between 1-12
rewardsList=["Y","N"]

f = open(fileName, "w")

counter = 0 
stateCounter = 0
while counter != counterMax:
    counter = counter + 1 


    id = counter
    name = "Customer" + str(id)
    gender = random.choice(genderList)
    age = randrange(18,90)
    if counter % 4 == 1:
       age = randrange(18,23)
    state = states[stateCounter]
    homestore = stateCounter
    
    if TEST:
       items = list()
       items.append(random.choice(listItems))
       if age in range(18,23):
          items = list()
          jeansOrShirt=['jeans', 'tshirt']
          items.append("jeans")
    else:
       items = list() 
       if counter % 3 == 1:
          if age in range(17,24):
             items = ['tshirt', 'jeans']
          else:
             items = ['shoe', 'socks']
       elif counter % 4 == 1 and gender == "F":
          items = ['dress', 'heels']
       elif counter % 5 == 1:
          items = ['coat', 'jacket']
       elif counter % 6 == 1:
          items = ['dressShirt', 'tie'] 
       else:
          items = ['shoes', 'heels', 'dress']
          #numItems=randrange(2,4)
          #items = list()
          #for i in range(numItems):
              #FPGrowth expects a list of unique items :(
              #itemType = random.choice(listItems)
              #if itemType not in items:
               #  items.append(itemType)
              #else: 
              #   while itemType in items:
               #     itemType = random.choice(listItems)
                 #items.append(itemType)
        

    if stateCounter == 49:
       stateCounter = 0
    else:
       stateCounter = stateCounter+1

    year = randrange(2016,2018)
    month = randrange(1,12)
    rewards = random.choice(rewardsList) 
    lineToWrite = str(id) + "|" + name + "|" + gender + "|" + str(age) + "|" + state + "|"+ str(homestore) + "|" + str(items) + "|" + str(year) + "|" + str(month) + "|" + rewards + "\n"
    f.write(lineToWrite)
