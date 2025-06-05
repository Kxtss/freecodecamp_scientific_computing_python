# FreeCodeCamp Scientific Computing with Python Projects

This repository contains solutions to the five required projects for the **Scientific Computing with Python Certification** from FreeCodeCamp. These projects focus on developing foundational programming skills in Python, including logic, data structures, algorithms, and simulations, applied to scientific and computational problems.

## Projects Included:

1.  **Arithmetic Formatter Project**
2.  **Budget App Project**
3.  **Polygon Area Calculator Project**
4.  **Probability Calculator Project**
5.  **Time Calculator Project**

---

## 1. Arithmetic Formatter Project

### Description

This project involves creating a Python function that accepts arithmetic problems in a string format and arranges them vertically, similar to how they are presented in elementary school. The function can also optionally display the answers for each problem. It handles various validations for the input problems, such as the number of problems, digit-only numbers, valid operators, and digit limits.

### Features

* **Vertical Alignment**: Formats arithmetic problems (addition and subtraction) into a vertical, right-justified display.
* **Input Validation**: Checks for common errors like too many problems, non-digit characters in numbers, invalid operators, or numbers exceeding four digits.
* **Optional Answers**: Can display the computed answers below the dashed line for each problem.

### Files

* `arithmetic_formatter.py`

### How to Run

You can find the `arithmetic_arranger` function in the provided code. An example of its usage is in the `main` function:

```python
# Example usage:
from arithmetic_formatter import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))
```

## 2. Budget App Project

### Description
This project simulates a simplified budgeting application using object-oriented programming. It allows users to create budget categories (e.g., Food, Clothing, Auto), deposit funds, withdraw money, and transfer funds between categories. It also generates a visual bar chart showing the percentage of spending across different categories.

### Features
* ***Category* Class**: Represents a budget category with methods for **deposit**, **withdraw**, **transfer**, and **get_balance**.
* ***Ledger* System**: Each category maintains a ledger of transactions with amounts and descriptions.
* ***Spend* Chart Generation**: A function **create_spend_chart** visualizes spending percentages across multiple categories as a bar chart.
* **Object-Oriented Design**: Utilizes classes and methods to encapsulate budgeting logic.

### Files

* `budget_app.py`

### How to Run

The **main** function demonstrates how to create **Category** objects, perform transactions, and generate the spend chart:

```Python

# Example usage:
from budget_app import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)  # Transfer from food to clothing
clothing.withdraw(20, "new shirt")  # An additional withdrawal for Clothing

auto = Category("Auto")
auto.deposit(500, "initial gas fund")
auto.withdraw(30.00, "gas fill-up")
auto.withdraw(15.50, "car wash")

# Print the string representation of the "Food" category
print(food)

# Create the spend chart with all test categories
categories_for_chart = [food, clothing, auto]
chart_output = create_spend_chart(categories_for_chart)
print(chart_output)
```

## 3. Polygon Area Calculator Project

### Description

This project involves creating classes for **Rectangle** and **Square** to calculate geometrical properties such as area, perimeter, and diagonal. It also includes functionality to generate a string-based "picture" of the shape and to determine how many times one shape can fit inside another. The **Square** class inherits from **Rectangle**, demonstrating inheritance principles.

### Features

* **Rectangle Class**:
    * Initialize with **width** and **height**.
    * Methods to set **width** and **height**.
    * Calculates **area**, **perimeter**, **diagonal**.
    * Generates a string **picture** representation (using **`*`** characters).
    * Determines **amount_inside** another shape.
* **Square Class**:
    * Inherits from **Rectangle**.
    * Initializes with **side** (width and height are set equally).
    * Overrides **set_width** and **set_height** to maintain square properties.
    * **Object-Oriented Design**: Demonstrates inheritance and method overriding.

### Files

* `shape_calculator.py`

### How to Run

The **main** function showcases the functionality of both **Rectangle** and **Square** classes:

```Python

# Example usage:
from shape_calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())

# Modify the rectangle's height and calculate its perimeter
rect.set_height(3)
print(rect.get_perimeter())

# Print the string representation of the rectangle
print(rect)

# Get the visual picture representation of the rectangle
print(rect.get_picture())

# Create a Square object
sq = Square(9)
print(sq.get_area())

# Modify the square's side and calculate its diagonal
sq.set_side(4)
print(sq.get_diagonal())

# Print the string representation of the square
print(sq)

# Get the visual picture representation of the square
print(sq.get_picture())

# Prepare the rectangle for testing get_amount_inside
rect.set_height(8)
rect.set_width(16)

# Calculate how many squares (sq) fit inside the rectangle (rect)
print(rect.get_amount_inside(sq))
```

## 4. Probability Calculator Project

### Description

This project implements a probability calculator that estimates the likelihood of drawing a specific set of colored balls from a "hat" by running a large number of random experiments. It uses a Monte Carlo simulation approach to approximate probabilities that might be difficult to calculate analytically. This project is a core part of the FreeCodeCamp Scientific Computing with Python certification.

### Features

* ***Hat* Class**: Simulates a hat containing balls of various colors. It supports adding balls by color and quantity and provides a method to **draw** balls randomly without replacement.
* ***experiment* Function**: Orchestrates the Monte Carlo simulation. It performs numerous drawing experiments from a deep copy of the hat and counts how many times the drawn balls meet the specified **expected_balls** criteria.
* **Monte Carlo Simulation**: Estimates probabilities through repeated random trials, making it suitable for complex probability scenarios.
* **Deep Copying**: Ensures that each experiment starts with the hat in its original state, preventing side effects between simulations.

### Files

* `probability_calculator.py`

### How to Run

The **main** function demonstrates how to set up a **Hat** and run an **experiment** to calculate a probability:

```Python

# Example usage:
from probability_calculator import Hat, experiment

hat = Hat(black=6, red=4, green=3)

probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1}, # E.g., expecting at least 2 red and 1 green
    num_balls_drawn=5,                     # Drawing 5 balls per experiment
    num_experiments=2000,                  # Performing 2000 experiments
)

print(f"Estimated probability: {probability}")
```

## 5. Time Calculator Project

### Description

This project provides a function to calculate a new time by adding a given duration to a start time. It correctly handles time formats (AM/PM), calculates changes in days, and can optionally update and display the new day of the week.

### Features

* **Time Addition**: Adds hours and minutes from a duration to a starting time.
* **AM/PM Handling**: Converts between 12-hour (AM/PM) and 24-hour formats internally for calculation and converts back for output.
* **Day Changes**: Accurately determines if the new time falls on the "next day" or "N days later".
* **Day of Week Tracking**: If an initial day of the week is provided, the function calculates and returns the correct new day of the week.

### Files

* `time_calculator.py`

### How to Run

You can use the **add_time** function with different parameters to see its behavior:

```Python

# Example usage:
from time_calculator import add_time

# Adding time without a specific starting day
print(add_time("11:30 AM", "2:32", "Monday")) 
# Expected: 2:02 PM, Monday

print(add_time("3:00 PM", "3:10"))
# Expected: 6:10 PM

print(add_time("11:59 PM", "24:05"))
# Expected: 12:04 AM (2 days later)
```