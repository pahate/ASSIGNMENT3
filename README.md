# ASSIGNMENT3
# Task1 
# Input 
Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
4.   take no as 5
# python code 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = 5
print(f"Factorial of {number} is {factorial(number)}")


# Task 2
# input
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
# python code 
import math


num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)


print(f"\nResults for the number {num}:")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm (base e): {log_result}")
print(f"Sine (in radians): {sine_result}")
