# 🔹 Conditional Statements Practice

# 1. Check Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

print("\n----------------------\n")


# 2. Check Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\n----------------------\n")


# 3. Grade Based on Marks
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")

print("\n----------------------\n")


# 4. Largest of Three Numbers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if (num1 > num2) and (num1 > num3):
    print("num1 is greatest")
elif (num2 > num1) and (num2 > num3):
    print("num2 is greatest")
elif (num3 > num1) and (num3 > num2):
    print("num3 is greatest")
else:
    print("Numbers are equal or two are equal")

print("\n----------------------\n")


# 5. Leap Year Check
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")