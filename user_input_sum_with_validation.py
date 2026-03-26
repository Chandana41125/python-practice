# Write a Python program which will keep adding a stream of numbers inputted by the user.
# The adding stops as soon as the user presses 'q' key on the keyboard. with some validation

Total = 0

while True:
    user_input = input("Enter the price of the Items or press 'q' to quit: ")

    try:
        Total += int(user_input)
        print(f"Total cost so far: {Total}")
    except ValueError:
        print("Invalid Input!! please enter a number or 'q' to quit")

    if user_input=='q':
        print(f"your bill total is {Total}. thanks for shopping with us. ")
        break