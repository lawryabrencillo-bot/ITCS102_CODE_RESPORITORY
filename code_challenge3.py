sender= input("Enter the sender name -> ")

type= input("Enter the type of item -> ")

is_Fragile = bool(input("Is the item fragile? ---> "))

weight = float(input("Enter the weight of the item ---> "))

distance = float(input("distance -->"))

is_Express = bool(input("Is it express?"))

is_International = bool(input("Is it international?"))

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 100 and is_Express == False and is_International == False:
	print("FREE SHIPPING")

elif is_Express == True and is_International == True:
	print("paldo")

else:
	print("scam")

#print("sender, type, is_Fragile")
