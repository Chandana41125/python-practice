# 🪭 Fan Class - Python OOP Practice

# 1. Basic Fan Class (Color)
class Fan:
    def __init__(self, color):
        self.color = color

    def show_color(self):
        print("Color:", self.color)


f1 = Fan("White")
f1.show_color()


print("\n----------------------\n")


# 2. Multiple Objects (Brand & Speed)
class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")


f1 = Fan("Usha", 5)
f2 = Fan("Bajaj", 4)

f1.show_details()
f2.show_details()


print("\n----------------------\n")


# 3. Change Speed
class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def change_speed(self, new_speed):
        self.speed = new_speed
        print("Updated Speed:", self.speed)


f1 = Fan("Usha", 5)
f1.change_speed(6)


print("\n----------------------\n")


# 4. Turn ON / OFF Fan
class Fan:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False  # default OFF

    def turn_on(self):
        self.is_on = True
        print("Fan is ON")

    def turn_off(self):
        self.is_on = False
        print("Fan is OFF")


f1 = Fan("Usha")
f1.turn_on()
f1.turn_off()


print("\n----------------------\n")


# 5. Increase Speed
class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def increase_speed(self):
        self.speed += 1
        print("Speed:", self.speed)


f1 = Fan("Usha", 4)
f1.increase_speed()