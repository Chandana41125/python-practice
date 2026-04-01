
# Addition of the two number
def sum_fun(num1, num2):
    print(num1 + num2)
sum_fun(10, 24)

# Subtraction of the two number
def sum_fun(num1, num2):
    print(num1 - num2)
sum_fun(10, 5)


# Multiplication of the two number
def sum_fun(num1, num2):
    print(num1 * num2)
sum_fun(10, 24)

# Division of the two number
def sum_fun(num1, num2):
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Division by zero is not possible")
sum_fun(10, 0)

#Average of three number
def average_of_three_num(a,b,c):
    average = (a+b+c)/3
    print(average)
average_of_three_num(10,20,30)



#function to print length of the cities
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
def calc_length(city):
    print(len(city))
calc_length(cities)


#function to print all city name in single line
def calc_length1(city):
        for city in cities:
            print(city,end=", ")
        print("")
calc_length1(cities)


#function that convert USD to INR
def converter(usd_val):
    INR = usd_val * 93
    print(f"{usd_val} USD = {INR} INR ")
converter(93)


#function that convert INR to USD
def converter1(INR_val):
    USD = INR_val / 93
    print(f"{INR_val} INR =  {USD} USD ")
converter1(93)


#function to find even and odd number
def odd_even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

odd_even(int(input("Enter the number: ")))

