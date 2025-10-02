# exercise_prime_json_csv_question.py

"""
Python Exercise:

Write a Python program that does the following:

1. Ask the user to enter 10 numbers (one by one).
2. From these numbers, find which ones are prime.
3. Store the prime numbers inside a dictionary
   (example format: {"prime_0": 2, "prime_1": 11}),
   where the key is "prime_index" and the value is the prime number.
4. Save this dictionary into a JSON file (primes.json).
5. Read back the JSON file and extract only the prime numbers
   that are greater than 7.
6. Save these filtered prime numbers into a CSV file (filtered_primes.csv)
   with one column named prime_number.

--------------------------------------------
Example Run:

Input:
Enter number 1: 4
Enter number 2: 7
Enter number 3: 11
Enter number 4: 15
Enter number 5: 2
Enter number 6: 13
Enter number 7: 20
Enter number 8: 3
Enter number 9: 9
Enter number 10: 19

Dictionary saved to JSON (primes.json):
{
    "prime_2": 11,
    "prime_4": 2,
    "prime_5": 13,
    "prime_7": 3,
    "prime_9": 19
}

Filtered primes > 7 saved to CSV (filtered_primes.csv):
prime_number
11
13
19
"""

# Your solution goes here...

import json
import csv

numbers = []
for i in range(10):
    while True:
        num = input(f"Enter number {i + 1}: ")
        try:
            num_int = int(num)
            numbers.append(num_int)
            break 
        except ValueError:
            print("Please enter a valid integer.")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True
prime_dict = {}
prime_index = 0

for num in numbers:
    if is_prime(num):
        prime_dict[f"prime_{prime_index}"] = num
        prime_index += 1


with open("primes.json", "w") as f:
    json.dump(prime_dict, f, indent=4)

with open("primes.json", "r") as f:
    loaded_primes = json.load(f)

filtered_primes = [v for v in loaded_primes.values() if v > 7]

with open("filtered_primes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["prime_number"])
    for prime in filtered_primes:
        writer.writerow([prime])