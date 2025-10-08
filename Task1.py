import math

# Step 1: Ask the user for input
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)

# Step 3: Display the results
print(f"\nResults for the number {num}:")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm (base e): {log_result}")
print(f"Sine (in radians): {sine_result}")

