# 1.	Write a python program to print all natural numbers from 1 to n. - using while loop

num=int(input("Enter the n numbers"))
i=1
while(i<num):
    print(i)
    i+=1

# 2.	Write a python program to print all natural numbers in reverse (from n to 1). - using while loop

num=int(input("Enter the n numbers"))
i=1
while(i<=num):
    print(num)
    i-=1

# 3.	Write a python program to print all even numbers between 1 to 100. - using while loop
n=int(input("Enter numbers"))
i=0
while(i<=n):
    print(i)
    i+=2

# 4.	Write a python program to find sum of all natural numbers between 1 to n.
n=int(input("Enter numbers"))
sum=0
for i in range(n):
    sum+=i
print(sum)

# 5.	Write a python program to find sum of all even numbers between 1 to n.

n=int(input("Enter numbers"))
i=0
sum=0
while(i<=n):
    print(i)
    sum+=i
    i+=2
print(sum)

#  6.	Write a python program to print multiplication table of any number.
n=int(input("Enter numbers"))
num=int(input("Enter the multiplication number"))
i=0
while(i<=n):
    print(num*i)
    i+=1


# 7.	Write a python program to count number of digits in a number.

n=int(input("Enter the number"))
count=0
if(n==0):
    count=1
else:
    while(n>0):
        n=n//10
        count+=1
print(count)


# 8.	Write a python program to find first and last digit of a number.
n=int(input("Enter the number"))
last=n%10

first=n
while(first>10):
    first=first//10
print(last,first)


# 9.	Write a python program to find sum of first and last digit of a number.
n=int(input("Enter the number"))
sum=0
last=n%10

first=n
while(first>10):
    first=first//10
    sum=last+first
print(sum)


# 10.	Write a python program to calculate product of digits of a number.
n=int(input("Enter the number"))
product=1
num=abs(n)
if(num==0):
    product=0
else:
    while(num>0):
       product*=num%10
       num=num//10
print(product)

#  11.	Write a python program to enter a number and print its reverse.
n=int(input("Enter the numer"))
reverse=0
while(n>0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)


# 12.	Write a python program to check whether a number is palindrome or not.
n=eval(input("Enter the numer"))
reverse=0
original=n
while(n>0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if(original==reverse):
    print("Palindrome")
else:
    print("Not palindrome")



# 14.	Write a python program to find power of a number using for loop.
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result =", base ** exp)


# 15.	Write a python program to find all factors of a number.

n = int(input("Enter a number: "))

print("Factors of", n, "are:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")

# 16.	Write a python program to calculate factorial of a number.
# Program to calculate factorial of a number

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i   # factorial = factorial * i

print("Factorial of", n, "is:", factorial)



# Program to check if a number is prime

n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is NOT a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is NOT a prime number")
            break
    else:
        print(n, "is a prime number")


# Program to print all prime numbers between 1 and n

n = int(input("Enter the value of n: "))

print("Prime numbers between 1 and", n, "are:")

for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


# Program to find sum of all prime numbers between 1 and n

n = int(input("Enter the value of n: "))
sum_primes = 0

for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        sum_primes += num

print("Sum of all prime numbers between 1 and", n, "is:", sum_primes)
