# Python Introductory Lesson

Welcome to your first Python lesson! In this lesson, you'll be introduced to the basics of Python programming. We’ll guide you step by step, so you’re ready to start coding.

---

## 1. Your First Python Program

Open your code editor and create a new file named `hello.py`. Enter the following code:
```python
print("Hello, world!")
```
Save the file, then run it in your terminal:
```sh
python hello.py
```
**Observe what is displayed in your terminal.**

---

## 2. Variables & Types

Variables are used to store data. Python automatically determines the type.

```python
name = "Alice"
age = 20
height = 1.75
is_student = True
```

- Discuss the type of data stored in each variable.
- Practice printing each variable using `print()`.

---

## 3. Basic Operations

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # Integer division
print(a % b)   # Modulo (remainder)
print(a ** b)  # Exponent
```
- Predict the output of each print statement, then run the code and compare.

---

## 4. Input from the User

```python
name = input("What's your name? ")
print("Nice to meet you, " + name + "!")
```
- Explain what `input()` does.
- Try running the code and entering your name.

---

## 5. Conditionals

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```
- Discuss what happens if you enter 18 or 17.

---

## 6. Loops

### For Loop
```python
for i in range(5):
    print("i =", i)
```

### While Loop
```python
count = 0
while count < 5:
    print("count =", count)
    count += 1
```
- Compare and discuss the differences between the two loops.
- Think about routines in your daily life where you naturally repeat an action for a group of items or until a condition is met, without explicitly calling it a “loop.” The challenge is to identify and describe an example of such a naturally occurring loop in your real life. The goal is to recognize how looping behavior exists outside programming, even if you’re not consciously aware of it.

---

## 7. Functions

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
```
- Explain what this code does.
- Write your own function that adds two numbers and returns the result.

---

## 8. Lists

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(len(fruits))
fruits.append("orange")
print(fruits)
```
- Practice changing and printing elements in the list.

---

## 9. Mini Project

Create a Python program that:
- Prompts the user for their name and age.
- Displays a message such as: "Hello, Alice! You will be 30 in 10 years."

---

## Tips

- Save your files frequently.
- Don’t be afraid to experiment!
- If you’re stuck, ask questions.

---

**Great job!** You’ve completed your first Python lesson!