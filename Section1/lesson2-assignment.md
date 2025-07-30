# Lesson 2 Assignment: Working with Data in Python

Test your knowledge of Python data types and structures! Complete all problems to reinforce what you've learned about strings, numbers, booleans, lists, and dictionaries.

**NOTE**: If you are going to use build in methods to solve the problems then be ready to explain what the built in method does. 

---

## Strings

### Problem 1: String Slicing and Indexing
Given the string `message = "Python Programming"`, write code to:
- Extract and print the first 6 characters
- Extract and print the last 11 characters
- Extract and print every other character starting from index 1
- Print the string in reverse order

### Problem 2: String Methods
You have a user input: `user_text = "  Hello, WORLD! This is Python!  "`. Write code to:
- Remove leading and trailing whitespace and convert to lowercase
- Replace all exclamation marks with periods
- Split the text into a list of words
- Count how many times the letter 'o' appears in the cleaned text

### Problem 3: String Manipulation
Create a program that takes a person's full name (first and last name separated by a space) and:
- Converts it to "Last, First" format
- Creates initials (e.g., "John Doe" becomes "J.D.")
- Checks if the name contains only alphabetic characters and spaces
- Calculates the total number of characters excluding spaces

---

## Numbers

### Problem 4: Arithmetic Operations
A store sells items at different prices. Write a program that:
- Calculates the total cost of 3 items priced at $12.99, $8.50, and $15.75
- Applies a 15% discount to the total
- Calculates the sales tax (8.5%) on the discounted amount
- Rounds the final amount to 2 decimal places and displays it

### Problem 5: Type Conversion and Validation
Create a program that:
- Asks the user to enter their age as a string
- Converts it to an integer and checks if the conversion is successful
- If the age is valid, calculate what year they were born
- If the age is invalid (contains non-numeric characters), display an appropriate message
- Display the result with proper formatting

### Problem 6: Number Formatting and Operations
Given a temperature in Celsius, write a program that:
- Converts it to Fahrenheit using the formula: F = (C × 9/5) + 32
- Converts it to Kelvin using the formula: K = C + 273.15
- Displays all three temperatures rounded to 1 decimal place
- Determines if the temperature is below freezing (0°C), room temperature (20-25°C), or hot (above 30°C)

---

## Booleans

### Problem 7: Logical Operations
Create a program that evaluates student eligibility for a scholarship. A student qualifies if:
- Their GPA is 3.5 or higher AND they have completed at least 60 credit hours
- OR they are in their senior year (4th year) with a GPA of at least 3.0
- Write code that takes these inputs and determines eligibility using boolean logic

### Problem 8: Truthy and Falsy Values
Write a program that tests the truthiness of different values:
- Create a list containing: `0, "", [], None, "hello", [1, 2, 3], -1, 0.0`
- Use a loop to check each value and print whether it's truthy or falsy
- Count how many truthy and falsy values there are in total

### Problem 9: Boolean Conditions
Create a password strength checker that returns `True` if a password meets all criteria:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Test your function with several password examples

---

## Lists

### Problem 10: List Manipulation
You have a shopping list: `shopping = ["milk", "bread", "eggs", "butter", "cheese"]`
Write code to:
- Add "apples" and "bananas" to the end of the list
- Insert "yogurt" at the second position (index 1)
- Remove "bread" from the list
- Print the list in alphabetical order (without permanently changing the original list)
- Display the length of the final list

### Problem 11: List Methods and Iteration
Create a program that:
- Starts with an empty list called `numbers`
- Adds the squares of numbers 1 through 10 to the list (1, 4, 9, 16, ...)
- Removes any numbers greater than 50
- Calculates and prints the sum of all remaining numbers
- Finds and prints the maximum and minimum values in the list

### Problem 12: List Data Processing
You have test scores: `scores = [85, 92, 78, 96, 88, 76, 94, 89, 82, 90]`
Write a program that:
- Calculates the average score
- Counts how many scores are above average
- Creates a new list containing only scores of 90 or higher
- Determines the letter grade for each score (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: below 60)

---

## Dictionaries

### Problem 13: Dictionary Operations
Create a student record system using a dictionary:
- Start with: `student = {"name": "Alice", "age": 20, "major": "Computer Science"}`
- Add a "gpa" key with value 3.7
- Update the age to 21
- Add a "courses" key with a list of 3 course names
- Print all keys and values in a formatted way

### Problem 14: Dictionary Iteration and Analysis
You have inventory data: `inventory = {"apples": 50, "bananas": 30, "oranges": 25, "grapes": 40, "strawberries": 15}`
Write code to:
- Print each item and its quantity in the format "Item: apples, Quantity: 50"
- Find the item with the highest quantity
- Calculate the total number of all fruits
- Create a new dictionary with only items that have more than 20 in stock

### Problem 15: Real-World Dictionary Application
Create a simple grade book program that:
- Uses a dictionary where keys are student names and values are lists of their test scores
- Starts with data for 3 students, each having 3-4 test scores
- Calculates each student's average grade
- Determines which student has the highest average
- Adds a new student with their scores to the dictionary
- Prints a formatted report showing each student's scores and average

---

## Completion Checklist

After finishing all problems, make sure you can:
- [ ] Manipulate strings using indexing, slicing, and methods
- [ ] Perform arithmetic operations and handle number conversions
- [ ] Use boolean logic and understand truthy/falsy concepts
- [ ] Create, modify, and iterate through lists
- [ ] Work with dictionaries for data storage and retrieval
- [ ] Apply these concepts to solve real-world programming problems

---

**Great work!** These exercises will prepare you for more advanced Python concepts in the next lessons.
