sum = 0

tuloy = True

while tuloy == True:
    x = int(input("Enter a number: "))

    if x == 0:
        print("loop is terminated")
        tuloy = False

    else:
        print("continue the loop")
        sum += x
        print("current sum is: ", sum)
        continue    