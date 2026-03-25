n = int(input())
arr = list(map(int,input().split()))
maxSum = int(input())

possible_sum = {0}

for num in arr:
    new_sum = set()
    for s in possible_sum:
        if s+num <= maxSum:
            new_sum.add(s+num)

    possible_sum |= new_sum

print(max(possible_sum))