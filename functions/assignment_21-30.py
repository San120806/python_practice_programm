# #arithmetic operator
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error! Division by zero."

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")

# if operation == "+":
#     print(f"Result: {add(num1, num2)}")
# elif operation == "-":
#     print(f"Result: {subtract(num1, num2)}")
# elif operation == "*":
#     print(f"Result: {multiply(num1, num2)}")
# elif operation == "/":
#     print(f"Result: {divide(num1, num2)}")
# else:
#     print("Invalid operation!")

# # power function
# def power(base , exponent):
#     result=1

#     if exponent>0:
#         for _ in range(exponent):
#             result*=base
#     elif exponent<0:
#         for _ in range(abs(exponent)):
#             result *= base
#         result = 1 / result
#     else:
#         result=1
#     return result
# base=float(input("enter the base: "))
# exponent=int(input("enter the exponent: "))

# print(f"{base} raised to the power {exponent} is {power(base , exponent)}")

# # Count Characters in a String (Function)
# def count_characters(s):
#     return len(s)
# string=input("enter the string: ")
# print(f"the no. of characters in the string is: {count_characters(string)}")

# # Check Prime (Function)
# def cehck_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# num= int(input("enter a no.: "))
# if cehck_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

#   Fibonacci Series (Function)
# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     while len(fib_series) < n:
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")

# # Write a function gcd(a, b) that computes the greatest common divisor of a and b.
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# num1=int(input("enter the 1st no. : "))
# num2=int(input("enter the 2nd no. : "))
# print(f"the GCD of {num1} and {num2} is: {gcd(num1 , num2)}")

# # Write a function lcm(a, b) that finds the least common multiple of a and b.
# def gcd(a,b):
#     while b:
#         a,b=b,a%b
#     return a
# def lcm(a,b):
#     return abs(a*b)//gcd(a,b)
# num1=int(input("enter the 1st no.: "))
# num2=int(input("enter the 2nd no.: "))
# print(f"the LCM of {num1} and {num2} is : {lcm(num1, num2)}")

# # Factorial (Recursive)
# def fac(n):
#     if n==0 or n==1:
#         return 1
#     return n* fac(n-1)
# num = int(input("enter the no. : "))
# print(f"The factorial of {num} is: {fac(num)}")

# # Tower of Hanoi
# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, target, source)

# # Input from user
# n = int(input("Enter the number of disks: "))
# tower_of_hanoi(n, 'A', 'C', 'B')

# # count occurences
# def count_occurrences(lst, x):
#     return lst.count(x)

# lst = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
# x = int(input("Enter the element to count: "))
# print(f"The element {x} appears {count_occurrences(lst, x)} times in the list.")





    









