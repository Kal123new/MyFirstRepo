

##############


# Python Exercises: Nested Loops and Lists

# ---
# Exercise 1: Matrix Sum
# ---
# Task: Write a function that takes a 2D list (a list of lists) of numbers
# and returns the sum of all its elements.
#
# Example:
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
 ]
# Expected Output: 45
# ---


    # Your code here

def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total
print(matrix_sum(matrix))

    # Test the function


# ---
# Exercise 2: Find the First Duplicate
# ---
# Task: Write a function that finds the first integer that appears more than once
# in a list. Use nested loops to compare each element with every other element.
#
# Example:
items = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# Expected Output: 2
# ---

def find_first_duplicate(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return items[i]
    return None
print(find_first_duplicate(items))


# ---
# Exercise 4: Flatten a 2D List
# ---
# Task: Write a function that takes a 2D list and returns a single
# "flattened" list containing all the elements from the original nested lists.
#
# Example:
nested_list = [['a', 'b', 'c'], ['d', 'e'], ['f']]
 # flat_list = ['a', 'b', 'c', 'd', 'e', 'f']
# ---

    
    # Your code here
def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list
print(flatten_list(nested_list))

# ---
# Exercise 5: Find Common Elements
# ---
# Task: Write a function that returns a new list containing elements that are
# present in *both* list1 and list2. Do not include duplicates in the result.
#
# Example:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Expected Output: [4, 5]
# ---

    # Your code here
def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
print(common_elements(list1, list2))


# Test the function
