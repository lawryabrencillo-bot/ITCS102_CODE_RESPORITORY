sender = input("Enter the sender name -> ")

type = input("Enter the type of item -> ")

is_Fragile = input("Is the item fragile? (yes/no) ---> ").lower() == "yes"

weight = float(input("Enter the weight of the item ---> "))

distance = float(input("distance --> "))

is_Express = input("Is it express? (yes/no) ---> ").lower() == "yes"

is_International = input("Is it international? (yes/no) ---> ").lower() == "yes"


base_cost = (weight * 2.50) + (distance * 0.15)


if weight <= 2.0 and distance <= 100 and is_Express == False and is_International == False:
    total = 0.00

elif is_Express == True and is_International == True:
    total = (base_cost * 1.40) + 50

elif is_Express == True or (is_International == True and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("Sender:", sender)
print("Type:", type)
print("Fragile:", is_Fragile)
print("Base Cost:", format(base_cost, ".2f"))
print("Total Shipping Cost:", format(total, ".2f"))