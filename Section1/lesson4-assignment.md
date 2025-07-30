# Lesson 4 Assignment: List/Dictionary Comprehensions and Lambda Functions

Test your knowledge of advanced Python features! Complete all problems to master list comprehensions, dictionary comprehensions, and lambda functions.

---

## List Comprehensions

### Problem 1: Basic List Comprehensions
Using list comprehensions, create the following lists:
- A list of squares for numbers 1 through 20
- A list of even numbers from 0 to 50
- A list containing the first letter of each word in: `["apple", "banana", "cherry", "date", "elderberry"]`
- A list of numbers from 1 to 100 that are divisible by both 3 and 5

### Problem 2: Filtering with List Comprehensions
Given the list `temperatures = [72, 85, 90, 68, 77, 92, 88, 75, 81, 95]`:
- Create a list of temperatures above 80 degrees
- Create a list of "Hot" or "Mild" labels where temperatures above 85 are "Hot" and others are "Mild"
- Create a list of temperatures converted to Celsius (C = (F - 32) × 5/9) for only temperatures above 75°F
- Create a list of the differences between each temperature and the average temperature

### Problem 3: Complex List Comprehensions
Working with nested data:
- Given `words = ["hello", "world", "python", "programming", "comprehension"]`, create a list of words that have more than 5 letters and contain the letter 'o'
- Create a list of all possible pairs (tuples) from two lists: `colors = ["red", "blue", "green"]` and `sizes = ["small", "medium", "large"]`
- Given a string `"The quick brown fox jumps over the lazy dog"`, create a list of words with their lengths, but only for words longer than 3 characters

---

## Dictionary Comprehensions

### Problem 4: Basic Dictionary Comprehensions
Create dictionaries using comprehensions:
- A dictionary mapping numbers 1-10 to their cubes
- A dictionary mapping each letter in "PYTHON" to its position in the alphabet (A=1, B=2, etc.)
- A dictionary from the list `["apple", "banana", "cherry"]` where keys are the fruits and values are their lengths
- A dictionary mapping each number from 1-20 to "even" or "odd"

### Problem 5: Filtering Dictionary Comprehensions
Given the dictionary `grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92, "Eve": 88}`:
- Create a dictionary containing only students with grades above 85
- Create a dictionary mapping student names to letter grades (A: 90+, B: 80-89, C: 70-79, etc.)
- Create a dictionary showing how many points each student needs to reach an A (90)
- Create a dictionary with student names as keys and whether they passed (grade >= 80) as boolean values

### Problem 6: Advanced Dictionary Comprehensions
Working with more complex data:
- Given two lists `names = ["Alice", "Bob", "Charlie"]` and `ages = [25, 30, 35]`, create a dictionary mapping names to ages
- From the sentence `"the quick brown fox jumps over the lazy dog"`, create a dictionary mapping each unique word to the number of times it appears
- Given `inventory = [("apples", 50), ("bananas", 30), ("oranges", 25)]`, create a dictionary but only include items with quantities above 30

---

## Lambda Functions

### Problem 7: Basic Lambda Functions
Create lambda functions for:
- Converting Fahrenheit to Celsius
- Calculating the area of a rectangle (length × width)
- Determining if a number is even
- Extracting the first word from a sentence
- Test each lambda function with sample inputs

### Problem 8: Lambda Functions with Built-in Functions
Given the list `numbers = [15, 8, 23, 42, 4, 16, 35, 7, 29, 12]`:
- Use `map()` with a lambda to square each number
- Use `filter()` with a lambda to get only numbers greater than 15
- Use `sorted()` with a lambda to sort the numbers by their last digit
- Use `reduce()` (from functools) with a lambda to find the product of all numbers

### Problem 9: Advanced Lambda Applications
Working with more complex scenarios:
- Given `students = [{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 92}, {"name": "Charlie", "grade": 78}]`, use lambda functions to:
  - Sort students by grade (highest first)
  - Filter students with grades above 80
  - Extract just the names of all students
- Create a lambda function that takes a string and returns it with only vowels
- Use a lambda with `max()` to find the longest word in `["python", "programming", "comprehension", "lambda", "function"]`

---

## Combined Challenges

### Problem 10: Comprehensive Data Processing
Given this dataset of employees:
```python
employees = [
    {"name": "Alice", "department": "Engineering", "salary": 75000, "years": 3},
    {"name": "Bob", "department": "Marketing", "salary": 60000, "years": 5},
    {"name": "Charlie", "department": "Engineering", "salary": 85000, "years": 7},
    {"name": "Diana", "department": "Sales", "salary": 70000, "years": 2},
    {"name": "Eve", "department": "Engineering", "salary": 90000, "years": 8}
]
```
Use comprehensions and lambda functions to:
- Create a list of names of all Engineering department employees
- Create a dictionary mapping department names to average salaries
- Find the employee with the highest salary using a lambda function
- Create a list of salary increases (10% for employees with 5+ years, 5% for others) using conditional expressions

### Problem 11: Text Analysis Pipeline
Given a text sample, create a complete analysis using comprehensions and lambdas:
- Use a list comprehension to extract all words (split by spaces and remove punctuation)
- Use a dictionary comprehension to count word frequencies
- Use lambda functions with filter to find words longer than 5 characters
- Use lambda functions with map to convert all words to title case
- Create a final summary dictionary with total words, unique words, and average word length

### Problem 12: Mathematical Operations Pipeline
Create a program that:
- Uses a list comprehension to generate 50 random integers between 1 and 100
- Uses dictionary comprehension to categorize them as "small" (1-33), "medium" (34-66), or "large" (67-100)
- Uses lambda functions to find the statistical measures: mean, median (using sorted), and mode
- Creates a final report using string formatting that summarizes all the data

---

## Completion Checklist

After finishing all problems, make sure you can:
- [ ] Write efficient list comprehensions for data transformation and filtering
- [ ] Create dictionary comprehensions for mapping and data organization
- [ ] Use conditional expressions within comprehensions
- [ ] Write and apply lambda functions for quick operations
- [ ] Combine lambda functions with map(), filter(), sorted(), and other built-ins
- [ ] Choose when to use comprehensions vs traditional loops
- [ ] Apply these techniques to real-world data processing scenarios
- [ ] Write more concise and "Pythonic" code

---

**Outstanding!** You've mastered some of Python's most powerful and expressive features. These skills will make your code more efficient and readable, and prepare you for advanced Python programming and frameworks like Flask!