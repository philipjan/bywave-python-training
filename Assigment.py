def init_computation(input):
    if int(input) in range(60, 75):
        print("Derp!")
    elif int(input) in range(75, 85):
        print("Good")
    elif int(input) in range(85, 95):
        print("Very Good")
    elif int(input) in range(95, 101):
        print("Level Asian!")
    else:
        print("Invalid Value")


input1 = input("Input number (60-100): ")
init_computation(input1)
