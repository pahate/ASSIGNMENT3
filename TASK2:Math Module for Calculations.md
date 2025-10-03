# Task 2
# input
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:

Asks the user for a number as input.
Uses the math module to calculate the: o Square root of the number o Natural logarithm (log base e) of the number o Sine of the number (in radians)
Displays the calculated results.

# python code
import math

num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num) log_result = math.log(num) sine_result = math.sin(num)

print(f"\nResults for the number {num}:") print(f"Square Root: {sqrt_result}") print(f"Natural Logarithm (base e): {log_result}") print(f"Sine (in radians): {sine_result}")
