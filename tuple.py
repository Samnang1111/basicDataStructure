# Task 1
# Create a tuple with different data types
my_tuple = ("Hello", 123, 45.67, True, [1, 2, 3])
print("Original Tuple:", my_tuple)

# Add "please add me" text and your birthday to the tuple
birthday = "2000-01-01"  
new_data = ("please add me", birthday)
updated_tuple = my_tuple + new_data
print("Updated Tuple:", updated_tuple)

# Check whether your birthday exists 
if birthday in updated_tuple:
    print(f"Your birthday ({birthday}) exists in the tuple!")
else:
    print(f"Your birthday ({birthday}) does not exist in the tuple.")

# Find the length
tuple_length = len(updated_tuple)
print("Length of the updated tuple:", tuple_length)

# Task 2
# Create a tuple containing at least five numbers and print the first and last element.
# •
# Create two sets of numbers (example: {1, 2, 3, 4} and {3, 4, 5, 6}) and:
# ➢
# Perform union(), intersection(), and difference().
# ➢
# Print the results of each operation.

#  Create a tuple
tuple = (1, 2, 3, 4, 5)
first_element = tuple[0]
last_element = tuple[-1]

print("First Element:", first_element)
print("Last Element:", last_element)

# Create two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Perform union
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Perform intersection
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Perform difference
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
print("Difference of set1 and set2:", difference_set1)
print("Difference of set2 and set1:", difference_set2)

# Task 3
# Write a program that ask the user to input three values: name, age, and city, and store these in a tuple.
# •
# Use tuple methods such as count() and index() to search for specific elements:
# •
# Verify that your result should be:

name = str(input('Enter name: '))

age = int(input('Enter age: '))

city = str(input('Enter city: '))

tuple = (name, age, city)

# ?
count_name = tuple.count(name)
city_index = tuple.index(city)

print(count_name)
print('Your tuple:', tuple)
print(f'index of `{city}` in the tuple: {city_index}')


# Task 4

# Take a list of numbers [1, 2, 3, 4, 4, 5, 6, 6, 7, 8], convert it to a set and display the set.
# •
# Write a program to adding 10, 20, 30 to a set
# •
# Write a Python program to remove three last items from the following set at once.
# •
# Checking if 6 is a member of a set
# •
# Finding the length of a set

# Convert a list to a set and display it
numbers_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8]
numbers_set = set(numbers_list)
print("Converted set:", numbers_set)

# Add 10, 20, 30 to the set
numbers_set.update([10, 20, 30])
print("Set after adding 10, 20, 30:", numbers_set)

# Remove the last three items from the set at once
numbers_list = list(numbers_set)
removed_items = numbers_list[-3:]  # Get the last three items
numbers_set = set(numbers_list[:-3])  # Keep everything except the last three
print("Removed items:", removed_items)
print("Set after removing last three items:", numbers_set)

# Check if 6 is a member of the set
is_member = 6 in numbers_set
print("Is 6 a member of the set?", is_member)

# Find the length of the set
set_length = len(numbers_set)
print("Length of the set:", set_length)





