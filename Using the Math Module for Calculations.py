import math


num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num)
log_result = math.log(num)
sine_result = math.sin(num)


print(f"\nResults for the number {num}:")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm (base e): {log_result}")
print(f"Sine (in radians): {sine_result}")

