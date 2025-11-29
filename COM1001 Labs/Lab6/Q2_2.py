#Credits to Kerem Gökcek for submitting the solution to the repository.

import random

try:
    items_num = int(input("How many items should be used? "))
except ValueError:
    raise TypeError("Item number must be an integer.")
if items_num < 2:
    raise ValueError("Item number must be greater than or equal to 2.")

items = []
for _ in range(0, items_num - 1): #Creates a randomly generated knapsack.
    weight = random.randint(1, 20)
    value = random.randint(10, 100)
    items.append((weight, value))

try:
    custom_weight = int(input("Weight? "))
except ValueError:
    raise TypeError("Weight must be an integer.")
if not (1 <= custom_weight <= 20):
    raise ValueError("Weight must be in range of 1 to 20.")

try:
    custom_value = int(input("Value? "))
except ValueError:
    raise TypeError("Value must be an integer.")
if not (10 <= custom_value <= 100):
    raise ValueError("Value must be in range of 10 to 100.")

print("Automatically generated items:", items)
items.append((custom_weight, custom_value))
print("User-provided item:", (custom_weight, custom_value))
print("Combined item list:", items)

knapsack_capacity = random.randint(20, 60)
print("Knapsack capacity:", knapsack_capacity)

for i in range(0, len(items)): #Sorts the items to put the most valuable (smaller weight to value ratio) items.
    greatest_ratio = items[i][1] / items[i][0]
    greatest_index = i
    for n in range(i + 1, len(items)):
        if items[n][1] / items[n][0] > greatest_ratio:
            greatest_ratio = items[n][1] / items[n][0]
            greatest_index = n
    if i != greatest_index:
        items[i], items[greatest_index] = items[greatest_index], items[i]

print("Sorted list by ratio:", items)

selected_items = []
total_weight = 0
total_value = 0
for item in items:
    if item[0] + total_weight <= knapsack_capacity:
        selected_items.append(item)
        total_weight += item[0]
        total_value += item[1]

print("Selected items:", selected_items)
print("Total weight:", total_weight)
print("Total value:", total_value)