#JEEPNEY SIMULATOR 
route = ["BAYAN", "STI", "DLL"]
passengers = []
SEATS = 6
FARE = 13
total_boarded = 0
get_off = 0
total = 0


while True:
    print("\tJEEP CAPACITY")
    print("Occupied seats: ", len(passengers), "/", SEATS)
    print("Available seats: ", SEATS - len(passengers))
    print()
    print("Sakay: ", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 Sakay 2 Priority seat 3 Para po!")
    print("4 Baba sa pinto 5 Baba sa harap")
    print("6 Seat check 7 Balikan 8 Exit")
    choice = input("Choice: ")


    if choice == "1":
        if len(passengers) == SEATS:
            print("PUNO NA HO")
        else:
            name = input("Name: ")
            passengers.append(name)
            total_boarded += 1
            total += FARE
            print(name, "boarded at the back")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("PUNO NA HO")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total_boarded += 1
            total += FARE
            print(name, "took the priority seat")

    elif choice == "3":
        name = input("BABA AYAW? ")
        if name in passengers:
            passengers.remove(name)
            get_off += 1
            print(name, "got off. Ingat po!")
        else:
            print(name, "not on this jeep")

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            left = passengers.pop()
            get_off += 1
            print(left, "got off at the door")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            front = passengers.pop(0)
            get_off += 1
            print(front, "got off at the front")

    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers [i])

    elif choice == "7":
        route.reverse()
        print("Route: ", route)

    elif choice == "8":
        print("JEEPNEY TRIP SUMMARY")
        print("Total passengers boarded: ", total_boarded)
        print("Total passengers who got off:" , get_off)
        print("Passengers remaining: ", len(passengers))
        print("Total fare today:", total)
        break
    
    else:
        print("Invalid choice")