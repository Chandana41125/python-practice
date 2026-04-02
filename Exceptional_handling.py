# Error occured if we divide any number by 0 in the below program

# a = int(input("Enter a num1: "))
# b = int(input("Enter a num2: "))
# res = a/b
# print(res)


# we cannot stop that error occurance so we can handle that by using try and except keywords

a = int(input("Enter a num1: "))
b = int(input("Enter a num2: "))
try:
    res = a/b
except Exception as e:
    print("Error Ocurred")