# Lesson 3 Assignment: Modular Programming & Error Handling

Test your knowledge of Python modules and error handling! Complete all problems to practice importing modules, creating your own modules, and handling errors gracefully.

---

## Importing Modules

### Problem 1: Built-in Modules
Write a program that uses Python's built-in modules to:
- Use the `math` module to calculate the area of a circle (π × r²) where the user provides the radius
- Use the `random` module to generate 5 random integers between 1 and 100
- Use the `datetime` module to display the current date and time in a user-friendly format
- Calculate how many days are left until New Year's Day of the next year

### Problem 2: Creating Your Own Module
Create a module called `calculator.py` that contains functions for:
- `add(a, b)` - returns the sum of two numbers
- `subtract(a, b)` - returns the difference of two numbers
- `multiply(a, b)` - returns the product of two numbers
- `divide(a, b)` - returns the division result, but handles division by zero
- Then create a main program that imports your calculator module and demonstrates all functions

### Problem 3: Module Exploration
Write a program that:
- Imports the `os` module and displays the current working directory
- Uses the `sys` module to print the Python version and platform information
- Imports `json` and creates a dictionary with your personal information (name, age, hobbies), then converts it to a JSON string
- Uses any one additional built-in module of your choice and demonstrates one of its functions

---

## Error Handling

### Problem 4: Basic Try-Except Handling
Create a program that asks the user for two numbers and performs division:
- Use `try-except` to handle the case where the user enters invalid input (not a number)
- Handle division by zero with a specific error message
- Use a `finally` block to print "Calculation attempt completed"
- Allow the user to try again if an error occurs

### Problem 5: File Handling with Error Management
Write a program that:
- Asks the user for a filename to read
- Uses `try-except` to handle the case where the file doesn't exist
- If the file exists, counts the number of lines and characters in it
- If the file doesn't exist, creates a new file with that name and writes "This is a new file" to it
- Handles any permission errors that might occur during file operations

### Problem 6: User Input Validation
Create a program that asks the user to enter their age and validates it:
- Use error handling to ensure the input is a valid integer
- Check that the age is between 0 and 150 (raise a custom error message if not)
- If the age is valid, categorize the person as: Child (0-12), Teen (13-19), Adult (20-64), or Senior (65+)
- Keep asking for input until a valid age is provided
- Display appropriate error messages for each type of invalid input

---

## Combined Challenges

### Problem 7: Module Creation with Error Handling
Create a module called `file_utils.py` that contains functions with proper error handling:
- `read_file(filename)` - reads and returns file contents, handles file not found errors
- `write_file(filename, content)` - writes content to a file, handles permission errors
- `count_words(filename)` - counts words in a file, handles various file-related errors
- Create a main program that imports and tests all these functions with both valid and invalid inputs

### Problem 8: Random Number Game with Error Handling
Create a number guessing game that:
- Uses the `random` module to generate a secret number between 1 and 100
- Handles invalid input (non-numeric entries) gracefully
- Handles out-of-range guesses (not between 1 and 100)
- Keeps track of the number of valid attempts
- Provides hints ("too high" or "too low") for valid guesses
- Allows the user to quit by typing "quit" and handles this gracefully

### Problem 9: Data Processing with Multiple Error Types
Write a program that processes a list of student data:
- Create a list of dictionaries representing students: `[{"name": "Alice", "scores": [85, 92, 78]}, {"name": "Bob", "scores": [90, 88]}, ...]`
- Calculate the average score for each student
- Handle cases where a student might have no scores (empty list)
- Handle cases where scores might contain invalid data (non-numeric values)
- Use the `statistics` module to calculate the mean, but handle cases where it's not available
- Save the results to a file and handle any file writing errors

---

## Completion Checklist

After finishing all problems, make sure you can:
- [ ] Import and use Python's built-in modules effectively
- [ ] Create your own modules with reusable functions
- [ ] Handle common errors using try-except blocks
- [ ] Write user-friendly error messages
- [ ] Use finally blocks appropriately
- [ ] Combine modular programming with proper error handling
- [ ] Handle file operations safely with error management
- [ ] Validate user input and provide helpful feedback

---

**Excellent work!** You now have the skills to write more robust and organized Python programs. These concepts will be essential as you build larger applications in future lessons.