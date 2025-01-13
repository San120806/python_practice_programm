# # largest no.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1>num2 and num1>num3:
#     print(f"the largest is : {num1}")
# elif num2>num1 and num2>num3:
#     print(f"the largest is : {num2}")
# elif num3>num1 and num3>num2:
#     print(f"the largest is : {num3}")
# else:
#     print("There is a tie among the numbers.")

# # leap yr 
# year = int(input("Enter a year: "))
# if (year % 4 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# # multiplication table
# num= int(input("enter the no.: "))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# # sum of n natural no.s
# n = int(input("Enter a positive integer: "))
# sum_n = n * (n + 1) // 2  
# print(f"The sum of the first {n} natural numbers is {sum_n}.")

# # factorial of no. 
# num=int(input("enter the no.: "))
# fac=1
# for i in range(1, num+1):
#     fac=fac*i
#     print(f"the factorial of {num} is : {fac}.")


# # no. guessing
# import random
# random_number = random.randint(1, 100)
# guess = 0
# print("Guess the number between 1 and 100!")
# while guess != random_number:
#     guess = int(input("Enter your guess: "))
#     if guess < random_number:
#         print("Too low!")
#     elif guess > random_number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed it right!")

# #Count Digits of a Number-Input a positive integer and count how many digits it has.
# n=int(input("enter the no.: "))
# count=len(str(n))
# print(f"the no.{n} has {count} digits.")

# # reverse a no.
# num = int(input("Enter a positive integer: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10
# print(f"The reversed number is {reverse}.")

# # Sum of Even and Odd Numbers Separately
# n=int(input("enter the no.: "))
# sum_evn=0
# sum_odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_evn+=i
#     else:
#         sum_odd+=i
# print(f"Sum of even numbers: {sum_evn}")
# print(f"Sum of odd numbers: {sum_odd}")    

# # Palindrome Checker (Integer)
# num = int(input("Enter a positive integer: "))
# original = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10
# if original == reverse:
#     print(f"{original} is a palindrome.")
# else:
#     print(f"{original} is not a palindrome.")








