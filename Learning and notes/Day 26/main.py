numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Angela"
new_list = [letter for letter in name]

doubled_list = [number * 2 for number in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)