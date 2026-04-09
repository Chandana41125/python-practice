# 🔁 For Loop & Range Practice

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("\n----------------------\n")

# 2. Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

print("\n----------------------\n")

# 3. Print even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

print("\n----------------------\n")

# 4. Print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

print("\n----------------------\n")

# 5. Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

print("\n----------------------\n")

# 6. Sum of numbers from 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)

print("\n----------------------\n")

# 7. Factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

print("\n----------------------\n")

# 8. Numbers divisible by 3 (1 to 50)
for i in range(1, 51):
    if i % 3 == 0:
        print(i)

print("\n----------------------\n")

# 9. Count numbers divisible by 5 (1 to 100)
count = 0
for i in range(1, 101):
    if i % 5 == 0:
        count += 1
print("Count:", count)

print("\n----------------------\n")

# 10. Prime number check (optimized)
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a Prime")
            break
    else:
        print("Prime")