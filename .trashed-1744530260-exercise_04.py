# Aldwin Odavar
# ITELEC2
# Laboratory #06 – Utilizing Basic Math Libraries in Python

import math

# Calculate the square root of 16
number = 16
sqrt_result = math.sqrt(number)

# Get the value of pi
pi_value = math.pi

# Calculate the sine of 30 degrees
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
sin_result = math.sin(angle_radians)

# Calculate the cosine and tangent of an angle
cos_result = math.cos(math.radians(60))  # Cosine of 60 degrees
tan_result = math.tan(math.radians(45))  # Tangent of 45 degrees

# Calculate the exponential and logarithms
exp_result = math.exp(2)  # e^2
log_result = math.log(10)  # Natural log (base e) of 10
log10_result = math.log(100, 10)  # Log base 10 of 100

# Display results
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)
