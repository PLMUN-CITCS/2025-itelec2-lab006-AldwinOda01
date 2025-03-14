# Aldwin Odavar
# ITELEC2
# Problem Set 01 - Exercise 04
# Utilizing Basic Math Libraries in Python

import math

def main():
    
    number = 16
    sqrt_result = math.sqrt(number)

    pi_value = math.pi

    angle_degrees = 30
    angle_radians = math.radians(angle_degrees)
    sin_result = math.sin(angle_radians)

    cos_result = math.cos(math.radians(60))
    tan_result = math.tan(math.radians(45))

    exp_result = math.exp(2)
    log_result = math.log(10) 
    log10_result = math.log(100, 10) 

    print(f"Square root of {number} is: {sqrt_result}")
    print(f"Value of pi is: {pi_value}")
    print(f"Sine of 30 degrees (in radians) is: {sin_result}")
    print(f"Cosine of 60 degrees (in radians) is: {cos_result}")
    print(f"Tangent of 45 degrees (in radians) is: {tan_result}")
    print(f"Exponential of 2 is: {exp_result}")
    print(f"Logarithm (base e) of 10 is: {log_result}")
    print(f"Logarithm (base 10) of 100 is: {log10_result}")

if __name__ == "__main__":
    main()
