#Parking fine calculation
#Input: hours(integer)
#Output: fine based on rules


hours = int(input())
if hours <= 2:
    print(100)
elif hours <= 5:
    print(50)
else:
    print(20)
