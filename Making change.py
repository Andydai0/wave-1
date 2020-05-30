c=int(input('Please enter an amount:'))
print("Your change is:")
print(c//200, "toonies")
c = c%200
print(c//100, "loonies")
c = c%100
print(c//25, "quarters")
c = c%25
print(c//10, "dimes")
c = c%10
print(c//5, "nickles")
c = c%5
print(c//1, "pennies")