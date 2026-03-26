# Write a Python program which will keep adding a stream of numbers inputted by the user.
# The adding stops as soon as the user presses 'q' key on the keyboard.


Total = 0
i=1
print("Sriram varma store")
while True:
    userInput = input("Enter the Item price or press 'q' to quit: ")

    if userInput!='q':
        Total += int(userInput)
        print(f"{i}. Order Total so far: {Total} ")
        i+=1
    else:
        print(f"Your Bill total is {Total}. Thank you for shopping with us.")
        break