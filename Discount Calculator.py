amount = int(input("Enter the Amount: "))

if amount < 1000:
    discount = 0.05
elif amount < 5000:
    discount = 0.10
else:
    discount = 0.15

final_amount = amount - (amount * discount)

print(f"{final_amount:.2f}")