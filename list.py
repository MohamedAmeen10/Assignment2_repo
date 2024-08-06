# Create an empty list
my_list = list()

# Add elements to the list
my_list.append("apple")
my_list.append("banana")
my_list.append("cherry")

# Print the list
print("The list contains:", my_list)

# Create a list from another iterable (e.g., a range)
numbers = list(range(1, 6))  # Creates a list [1, 2, 3, 4, 5]

# Print the list of numbers
print("The list of numbers:", numbers)

# Access elements by index
print("First element:", my_list[0])  # Prints 'apple'
print("Second element:", my_list[1])  # Prints 'banana'

# Iterate through the list
print("Fruits in the list:")
for fruit in my_list:
    print(fruit)
