""" math module :- The math module is a built-in module  that provides access to a variety of mathematical functions. It deal with basic operations like (+), (-), (*), (/) and advanced operations like trigonometric, logarithmic, exponential functions. """

import math

#constant math functions
print("\n__________constant math functions__________\n")

# equivalent to float("nan")
print("The value of Not a Number:", math.nan) 
# Checks whether a value is NaN (not a number) or not
print ("nan value is true or false:", math.isnan (-45.34))

# positive equivalent to float("inf")
print("The value of positive infinity:", math.inf)
 # negative equivalent to float("-inf")
print("The value of negative infinity:", -math.inf)
# Checks whether a number is infinite or not
print("inf value is true or false:", math.isinf(56))

# Check whether the values are finite or not
print("finite value true or false:",math.isfinite(2000))
print("nan is finite or not:",math.isfinite(float("nan")))
print("inf is finite or not:",math.isfinite(float("inf")))

print("The value of pi:", math.pi)  # 3.14
print("The value of e:", math.e)   # Euler's number
print("The value of tau:", math.tau)  # 2*pi


# Normal math functions
print("\n__________Normal math functions__________\n")

# return absolute float value (non-negative number)
print("The absolute value:", abs(-3.9))

# return absolute float value (non-negative number)
print("The absolute value:", math.fabs(-4))

# math.pow(x, y): Return the value of 9 raised to the power of 3
print("x to the power y:", math.pow(9, 3)) #x=9, y=3

# square root of different numbers
print("exact square root:", math.sqrt(64))
print("not-exact square root:", math.sqrt(10.1))

# square root numbers downward to the nearest integer
print("square root nearest integer:", math.isqrt(10))

# Rounds a number upward to the nearest integer
print("upward to the nearest integer:", math.ceil(5.3))
print("upward to the nearest integer:", math.ceil(-5.3))

# Round a numbers downward to the nearest integer
print("downward to nearest integer:", math.floor(0.6))

# math.trunc() method returns the truncated integer part of a number
print("truncated interger:", math.trunc(2.77))

# Round value upward or downward to the nearest integer
print("nearest round value:", round(3.4))

# Return the product of the elements (three way)
print("product of elements in range:", math.prod(range(1,6)))
print("product of elements:", math.prod([2,3,4,10]))
elements = 2,3,5,4
print("product of elements:", math.prod(elements))

# Print the sum of all items (three way)
print("sum of elements in range:", math.fsum(range(1,6)))
print("sum of elements:", math.fsum([100, 400, 340, 500]))
elements = 2,3,5,4
print("sum of elements:", math.prod(elements))

# Return factorial of a number
print("factorial of a number:", math.factorial(6))

# math.fmod(x,y) method returns the remainder (modulo) of x/y
print("remainder of 20/4:", math.fmod(20, 4))
print("remainder of -10/3:", math.fmod(-10, 3))

# math.remainder() method returns the remainder of x with respect to y
print ("remainder of number:", math.remainder(9, 2))

# logarithmic math functions
print("\n__________logarithmic math functions__________\n")

# math.log() method returns the natural logarithm of a number
print("natural logarithm of number:", math.log(2.7183))

# math.log10() method returns the base-10 logarithm of a number
print("base-10 logarithm of a number:", math.log10(2))

# math.log2() method returns the base-2 logarithm of a number
print("base-2 logarithm of a number:", math.log2(1))

# math.log1p() method returns log(1+number) of a number
print("log(1+number):", math.log1p(2))

# exponential math functions
print("\n__________exponential math functions__________\n")

# math.exp(x) method returns (e) raised to the power of x (e^x)
print("exponential of positive value:", math.exp(50))
print("exponential of negative value:", math.exp(-30))

# math.expm1() method returns (E^x - 1)
print("exponential value of expm1:", math.expm1(32))

# math.ldexp() method returns  x * (2**i) of the given numbers x and i
print("Idexp of number:", math.ldexp(9, 3))

# math.frexp() method returns the mantissa and the exponent of a number, as a pair (m,e)
# mathematical formula for this method : number = (m * 2**e)
print("frexp of number:", math.frexp(4))

# Trigonometric math functions
print("\n__________Trigonometric math functions__________\n")

# math.degrees() method converts an angle from radians to degrees
print("radians into degrees:", math.degrees(8.90))

# math.radians() method converts an angle from degrees into radians
print("degrees into radians:", math.radians(180))

# Note: PI (3.14..) radians are equal to 180 degrees, which means that 1 radian is equal to 57.2957795 degrees

# math.sin() method returns the sine of a number
print("sine of number:", math.sin(0.00))
print("sine of number:", math.sin(math.pi/2))

# math.sinh() method returns the hyperbolic sine of a number
print("hyperbolic sine of number:", math.sinh(90))

# math.cos() method returns the cosine of a number
print("cosine of number:", math.cos(0.00))
print("cosine of number:", math.cos(math.pi/2))

# math.cosh() method returns the hyperbolic cosine of a number
print("hyperbolic cosine of number:", math.cosh(90))

# math.tan() method returns the tangent of a number
print("tangent of number:", math.tan(90))

# math.tanh() method returns the hyperbolic tangent of a number
print("hyperbolic tangent of number:", math.tan(90))
