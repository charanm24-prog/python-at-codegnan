# Add two numbers
a = int(input())
b = int(input())
print(a + b)

# Quotient and remainder
a = int(input())
b = int(input())
print("Quotient:", a // b)
print("Remainder:", a % b)

# Even or Odd
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Swap without third variable
a = int(input())
b = int(input())

a = a + b
b = a - b
a = a - b

print(a, b)

# Largest of three numbers
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# Square using exponent
n = int(input())
print(n ** 2)

# Divisible or not
a = int(input())
b = int(input())

if a % b == 0:
    print("Divisible")
else:
    print("Not Divisible")

# Area of rectangle
l = int(input())
w = int(input())
print(l * w)

# Positive, Negative or Zero
n = int(input())

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Check equal numbers
a = int(input())
b = int(input())

if a == b:
    print("Equal")
else:
    print("Not Equal")

# Voting eligibility
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Multiple of 3 and 5
n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Yes")
else:
    print("No")

# Greatest using nested if
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

# Leap year
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Vowel or consonant
ch = input().lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Grade system
marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# Prime number
n = int(input())
flag = True

if n <= 1:
    flag = False
else:
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

if flag:
    print("Prime")
else:
    print("Not Prime")

# Palindrome
n = input()

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Electricity bill
units = int(input())

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Bill:", bill)

# Century & Leap century
year = int(input())

if year % 100 == 0:
    print("Century Year")
    if year % 400 == 0:
        print("Leap Century")
    else:
        print("Not Leap Century")
else:
    print("Not a Century Year")
