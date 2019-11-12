# variables 
dollars = 0 
halfDollars = 0
quarters = 0 
dimes = 0 
nickels = 0 
pennies = 0
price = 0
change = 0
given = 0

print("enter the amount of money you owe")
owe = float(input("money owe: "))
given = float(input("how much money did you give? "))

nickels += pennies * 5
dimes += nickels * 2
quarters += nickels * 5
halfDollars += quarters * 2
dollars += halfDollars * 2

nickels = 0
dimes = 0
quarters = 0
halfDollars = 0
dollars = 0

change = 0
change = given - owed
print(round(change, 2))

change = change * 100

dollars = change/100
change = change % 100
change = round(change,1)

halfDollars - change / 50
change = change % 50
change = round(change, 1)

quarters - change / 25
change - change % 25

dimes = change / 10
change = change % 10

nickels = change / 5
change = change % 5

print("dollars: " + str(dollars))
print("half-dollars: " + str(halfDollars))
print("quarters: " + str(quarters))
print("dimes: " + str(dimes))
print("nickels: " + str(nickels))
print("pennies: " + str(pennies))
             
