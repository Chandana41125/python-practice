def factorial(num):
    fact = 1
    if num == 0 or num ==1:
        return 1
    else:
        for n in range(num,0,-1):
            fact = fact * n
    return fact


res = factorial(int(input("Enter a number that you want to do factorial: ")))
print(res)

count = 0
for i in str(res):
    if i == '0':
        count += 1
print(int(count))