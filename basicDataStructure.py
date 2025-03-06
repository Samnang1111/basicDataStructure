# Exercise 1
# Create a tuple with different data types
my_tuple = ("Hello", 123, 45.67, True, [1, 2, 3])
print("Original Tuple:", my_tuple)

# Add "please add me" text and your birthday to the tuple
birthday = "2000-01-01"
new_data = ("please add me", birthday)
updated_tuple = my_tuple + new_data
print("Updated Tuple:", updated_tuple)

# Check whether your birthday exists in the tuple
if birthday in updated_tuple:
    print(f"Your birthday ({birthday}) exists in the tuple!")
else:
    print(f"Your birthday ({birthday}) does not exist in the tuple.")

# Find the length of the updated tuple
tuple_length = len(updated_tuple)
print("Length of the updated tuple:", tuple_length)

# Exercise 2
# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
first_element = my_tuple[0]
last_element = my_tuple[-1]

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

# Exercise 3
# Prompt the user to input their name, age, and city
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Store the inputs in a tuple
user_tuple = (name, age, city)

# Print the tuple
print(f"Your tuple: {user_tuple}")

# Use the count() method to count occurrences of 'Vanda'
count_vanda = user_tuple.count('Vanda')
print(f"Count of 'Vanda' in the tuple: {count_vanda}")

# Use the index() method to find the index of 'Phnom Penh'
# We use try-except to handle cases where 'Phnom Penh' is not in the tuple
try:
    index_phnom_penh = user_tuple.index('Phnom Penh')
    print(f"Index of 'Phnom Penh' in the tuple: {index_phnom_penh}")
except ValueError:
    print("Phnom Penh is not in the tuple.")

# Exercise 4
# Initial list of numbers
numbers_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8]

# Convert the list to a set
numbers_set = set(numbers_list)
print("Converted set:", numbers_set)

# Add 10, 20, 30 to the set
numbers_set.update([10, 20, 30])
print("Set after adding 10, 20, 30:", numbers_set)

# Remove the last three items from the set
# Convert to a sorted list to simulate "last three items" removal
numbers_list = sorted(numbers_set)
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

# Challenging Exercise
# Step 1: Create a tuple with some student names
student_names = ("Reaksa", "Chan Panha", "Mani", "Amara", "Sreytim", "Laksmey", "Khayhour", "Reaksa", "Mani")

# Step 2: Convert the tuple to a set to remove duplicates
student_set = set(student_names)
print("Set after removing duplicates:", student_set)

# Step 3: Search for a name in the set
search_name = input("Enter a name to search: ")
if search_name in student_set:
    print(f"{search_name} is in the set.")
else:
    print(f"{search_name} is not in the set.")

# Step 4: Add or remove names based on user input
action = input("Do you want to add or remove a name? (add/remove): ").strip().lower()
if action == "add":
    name_to_add = input("Enter a name to add: ")
    student_set.add(name_to_add)
    print("Updated set:", student_set)
elif action == "remove":
    name_to_remove = input("Enter a name to remove: ")
    if name_to_remove in student_set:
        student_set.remove(name_to_remove)
        print("Updated set:", student_set)
    else:
        print(f"{name_to_remove} is not in the set.")

# Step 5: Save the set of names to a file
with open("students.txt", "w") as file:
    for name in student_set:
        file.write(name + "\n")
print("Names saved to file.")

# Step 6: Load the names from the file and display them
loaded_set = set()
with open("students.txt", "r") as file:
    for line in file:
        loaded_set.add(line.strip())
print("Names loaded from file:", loaded_set)



