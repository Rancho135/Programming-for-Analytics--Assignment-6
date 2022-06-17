

#****************************************************************
#Name:Goodnews Agbadu

#
#ANA1001 Lab 6
#****************************************************************



'''question 1
Write a program that tells the user a madlibs story. (you can reuse your
previous story as a starting point)
Store a list of nouns, verbs and adverbs, as well as other story elements and
ask the user to add elements to the list
Use the random function to pick a random story element from the list and build
the story. See  https://pynative.com/python-random-choice/ for details on how to
do this When the program is run it should tell the user a unique story.
Keep looping (ask the user for another name and repeat the printing) until q is
entered'''

import statistics
import random
import time

food = ["rice","bagel","chicken"]
location=["india","Nigeria","canada","Niger"]
people=["trump","adi","messi","sharon"]
times =["morning","evening","night"]
things=["computer","phone","replit","text book"]
adverbs =["slowly","sweetly","warmly"]

# makes a story using random function(r)
#picks a random item from food,location,people,times,things and adverbs
#runs a while loop where the condition is true that means the loop will run until its broken or the flag is turned false

while True:
  print("\n" + f" I was hanging out with my friends eating {random.choice(food).title()}.")
#picks a random item from heroes and place
  print(f" Few minutes later {random.choice(people).title()} called me, and said i want to take you to a python class in {random.choice(location).title()} to learn python.")
  time.sleep(2)
    
#picks a random item from things
  print(f" I dont have the basic skills, I said.. he said do not worry, you can use your {random.choice(things).title()} as your learning instruments.")
  time.sleep(2)
  print(" I agreed and I was very happy and excited to learn python.")
  time.sleep(2)
#picks a random item from choice
  print(f" Immediately looked through the window {random.choice(adverbs)} it was already {random.choice(times).title()} then I realized it was all a prank.")
  time.sleep(2)

  choice = input(" Do you want to read this prank story again? y for yes , q for quit: ")
  time.sleep(2)

  if choice == "y":
    continue
  elif choice == "q":
    break
print("\n")


'''Write a program that asks the user for their name and the size of the pizza they wish to order (in this example they can only order one size pizza). 
Pizzas prices: small $6.99, medium $8.99 and large $10.99
Ask how many pizzas they want 
Calculate 13% tax
Print a message with their name, order, tax and total for the order
This program should not loop
Sleep 2 seconds'''

#inputs name,quantity and size for the pizza
import time #import time packages
name = input("What is your name? ")

size = input("Select the size of pizza - type 1 for small , 2 for medium and 3 for large? ")

qty = input("How many pizzas do you want ")

qty = int(qty)

size =  int(size)

#an if statement to determine the price and tax for the pizza ordered
if size == 1:
  size = "small"
  price = 6.99
  tax = price * 0.13
  total = tax + price
elif size == 2:
  size = "medium"
  price = 8.99
  tax = price * 0.13
  total = tax + price
else :
  size = "large"
  price = 10.99
  tax = price * 0.13
  total = tax + price
if qty == 1:
  print(f"Hi {name} , you ordered {qty} {size.title()} of pizza , and your tax is {tax*qty:.2f} and your total is {total*qty:}.")
  time.sleep(2)
else:
  print(f"Hi {name}, you ordered {qty} number of {size.title()} pizza, and your tax is ${tax*qty:.2f} and your total is ${total*qty:}.")
  time.sleep(2)

  print("\n")



'''Write a program to calculate the cost of a dinner for each one of the members of a dinner party according to their age:
If the person is under 5, dinner is free
If the person is under 10, dinner is $5
If the person is under 18, dinner is $10
If the person is over 65, the dinner is $12
All other diners pay $15
Calculate 8% tax
Program should loop until exit is entered, with each loop a new diner is added, and the total overall numbers updated
Display the total for each diner, the total number of diners, the average cost per diner, and the cumulative total (cost) for all diners
Sleep 2 seconds'''


# Instructions: to see the cumulative total cost, you will need to run the code for person 1 and person 2.
import time
number_of_persons = 0
total_number_of_dinners = 0
    
# loop
while True:
  total = 0
  number_of_persons += 1
  if input('Welcome to Goodnews resturant...Press q to quit, enter to add dinner plate: ') == 'q':
    time.sleep(2)
    break
  name = input('Enter person ' + str(number_of_persons) + ' name: ')
  age = int(input('Enter person ' + str(number_of_persons) + ' age: '))
  if age < 5:
    pass
  elif age < 10:
    total += 5
  elif age < 18:
    total += 10
  elif age > 65:
    total += 12
  else:
    total += 15
  total += total * 8 / 100
  total_number_of_dinners += total
  print('Cost of dinner', number_of_persons, ': ', total, '$')
  time.sleep(2)
  print('No of dinners: ', number_of_persons)
  time.sleep(2)
  print('The average cost for each plate: ', total_number_of_dinners / number_of_persons)
  time.sleep(2)
  print('The total cost: ', total_number_of_dinners)