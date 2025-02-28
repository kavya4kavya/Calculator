# Decimal and Binary Calculator

This Python script implements a command-line calculator that supports both decimal and binary arithmetic operations.

## Features

-   **Decimal Operations:**
    -      Addition
    -      Subtraction
    -      Multiplication
    -      Division
    -      Floor Division
    -      Square Root
    -      Cube Root
    -      Exponentiation
    -      Factorial
    -      Modulo
-   **Binary Operations:**
    -      Addition
    -      Subtraction
    -      Multiplication
    -      Division
-   **User-Friendly Interface:** Menu-driven interface for easy navigation.
-   **Error Handling:** Includes checks for division by zero and invalid input.

## How to Use

1.  **Prerequisites:**
    -      Python 3.x installed on your system.
2.  **Running the Script:**
    -      Save the Python code to a file (e.g., `calculator.py`).
    -      Open a terminal or command prompt.
    -      Navigate to the directory where you saved the file.
    -      Run the script using the command: `python calculator.py`
3.  **Using the Calculator:**
    -      Follow the on-screen prompts to select between decimal and binary operations.
    -      Choose the desired operation from the sub-menu.
    -      Enter the required operands when prompted.
    -   The script will display the result.
    -   To exit, select the exit option.

## Code Explanation

-   The script uses a `while` loop to maintain the calculator's running state until the user chooses to exit.
-   It uses `input()` to get user input and `print()` to display output.
-   Decimal operations utilize standard Python arithmetic operators and the `math` module for functions like square root and factorial.
-   Binary operations convert binary inputs to decimal, perform the calculation, and convert the result back to binary.
-   Error handling is implemented to prevent division by zero and manage invalid user choices.
-   The match case statement is used to handle the different operation choices.
