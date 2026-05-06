# ==========================================
# LIST COMPREHENSION PRACTICE QUESTIONS
# ==========================================


# 1. Squares from 1 to 10
square = [i * i for i in range(1, 11)]
print("Squares:", square)


# 2. Even Numbers from 1 to 20
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print("Even Numbers:", even_numbers)


# 3. Convert City Names to Uppercase
cities = ["mysore", "bangalore", "pune", "mumbai"]

city_upper = [i.upper() for i in cities]
print("Uppercase Cities:", city_upper)


# 4. Length of Each City Name
city_length = [len(i) for i in cities]
print("City Name Lengths:", city_length)


# 5. Numbers Divisible by 5 from 1 to 50
divisible_by_five = [i for i in range(1, 51) if i % 5 == 0]
print("Divisible by 5:", divisible_by_five)


# ==========================================
# INTERMEDIATE LEVEL QUESTIONS
# ==========================================


# 6. Remove Vowels from a String
text = input("Enter a string: ").lower()

vowels = "aeiou"

remove_vowels = "".join([i for i in text if i not in vowels])

print("Without Vowels:", remove_vowels)


# 7. Cubes of Odd Numbers from 1 to 20
list_of_cubes = [i ** 3 for i in range(1, 21) if i % 2 != 0]
print("Cubes of Odd Numbers:", list_of_cubes)


# 8. Flatten a Nested List
list1 = [[1, 2], [3, 4], [5, 6]]

flatten_list = [j for i in list1 for j in i]

print("Flatten List:", flatten_list)


# 9. First Letter of Each Word
list2 = ["apple", "banana", "mango"]

first_letter_list = [i[0] for i in list2]

print("First Letters:", first_letter_list)


# 10. Positive Numbers from a List
l1 = [-1, 2, 3, -4, 4, -46, 8, 0]

positive_numbers = [i for i in l1 if i > 0]

print("Positive Numbers:", positive_numbers)


# ==========================================
# SLIGHTLY TRICKY QUESTIONS
# ==========================================


# 11. Convert String to List
alphabets = "A B C D"

str_to_list = [i for i in alphabets.split()]

print("String to List:", str_to_list)


# 12. Multiplication Table of 5
multiple_table = [i * 5 for i in range(1, 6)]

print("Multiplication Table of 5:", multiple_table)


# 13. Convert String List into Integer List
l1 = ["1", "2", "3"]

list_to_int = [int(i) for i in l1]

print("String List to Integer List:", list_to_int)


# 14. Common Elements Between Two Lists
l2 = [1, 2, 3, 4, 5]
l3 = [1, 2, 3, 4, 6, 7]

common_elements = [i for i in l2 if i in l3]

print("Common Elements:", common_elements)


# 15. Replace Negative Numbers with 0
l4 = [-1, 2, 3, -3, -8]

negative_zero = [0 if i < 0 else i for i in l4]

print("Negative Numbers Replaced with 0:", negative_zero)


# ==========================================
# INTERVIEW DEFINITION
# ==========================================

print("\nDefinition:")
print("List comprehension is a compact and efficient way to create lists in Python using a single line of code with loops and optional conditions.")