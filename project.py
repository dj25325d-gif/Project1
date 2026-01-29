print("Welcome to the Personal Data Collector")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
fav_num = int(input("Enter your favourite number: "))

print("\n--- Your Details ---")

print("Name:", name, "(Type:", type(name), ", Memory:", id(name), ")")
print("Age:", age, "(Type:", type(age), ", Memory:", id(age), ")")
print("Height:", height, "(Type:", type(height), ", Memory:", id(height), ")")
print("Favourite Number:", fav_num, "(Type:", type(fav_num), ", Memory:", id(fav_num), ")")

birth_year = 2026 - age
print("\nYour birth year is:", birth_year)

print("\nThank you for using the program!")
