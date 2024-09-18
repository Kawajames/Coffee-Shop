#cis129_lab03_coffeeShop.py
#Created by Dakota Kartchner for CIS129 Prog and Problem Solving

coffee_price = 5 #5$ for each coffee
muffin_price = 4 #4$ foe each muffin1
tax_rate = 0.06 # 0.06 is equal to 6%
#This shows the cost of each item

coffees_bought = int(input("How many coffees were bought?"))
#this will ask the user how many coffees were bought
muffins_bought = int(input("How many muffins were bought?"))
#this will ask the user how many muffins were bought

coffee_total = coffees_bought * coffee_price
muffin_total = muffins_bought * muffin_price
#calculates the total price based on amount of item bought multiplied by preset price 

total_price = coffee_total + muffin_total
#calculates the total price minus tax
total_tax = total_price * tax_rate
#calculates the total tax needed to be payed
total_price = total_price + total_tax
#calculates the total price including the taxes
#above code calculates the total price based on the values entered

#print(total_price) 
#above code used for testing

#this will print the final reciept based on what was entered
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffees_bought)
print("Number of muffins bought?")
print(muffins_bought)
print("***************************************")
print(" ")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(coffees_bought) + " Coffee at $" + str(coffee_price) + " each: $" + str(coffee_total) + ".00")
print(str(muffins_bought) + " Muffins at $" + str(muffin_price) + " each: $" + str(muffin_total) + ".00")
print("6% tax: $" + str(total_tax))
print("---------")
print(("Total: $") + str(total_price))
print("***************************************")