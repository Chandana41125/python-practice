# 🔁 While Loop Practice

# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

print("\n----------------------\n")

# 2. Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

print("\n----------------------\n")

# 3. Print even numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

print("\n----------------------\n")

# 4. Print odd numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

print("\n----------------------\n")

# 5. Multiplication table
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

print("\n----------------------\n")

# 6. Sum of numbers from 1 to n
n = int(input("Enter a number: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)

print("\n----------------------\n")

# 7. Factorial of a number
n = int(input("Enter a number: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)

print("\n----------------------\n")

# 8. Numbers divisible by 3 (1 to 50)
i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i += 1

print("\n----------------------\n")

# 9. Count numbers divisible by 5 (1 to 100)
i = 1
count = 0
while i <= 100:
    if i % 5 == 0:
        count += 1
    i += 1
print("Count:", count)

print("\n----------------------\n")

# 10. Prime number check (optimized)
n = int(input("Enter a number: "))

if n <= 1:
    print("Not prime")
else:
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            print("Not prime")
            break
        i += 1
    else:
        print("Prime")