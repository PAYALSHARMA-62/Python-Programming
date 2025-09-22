##/9/25
##num3=12
##num4=12
##num3+num4
##
##num1=eval(input("enter first number"))
##num2=eval(input("Enter second number"))
##res=num1+num2
##print("Res: ",res)
##
##
##num1=eval(input("enter first number"))
##num2=eval(input("Enter second number"))
##if num1%2==0 and num2%2==0:
## res=num1+num2
##print("Res: ",res)
##
##
##if(print("hello")):
##    print("inside if")
##else:
##    print("inside else")



##per=int(input("Enter the percentage: "))
##if(100>=per>=90):
##    print("A")
##elif(90>=per and per>=80):
##    print("B")
##elif(80>=per>=70):
##    print("C")
##elif(70>=per>=50):
##    print("D")
##else:
##    print("No GRAde")

"""
Check if a number is postive ,Negative or Zero
num=int(input("Enter the number:"))
if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")
"""

"""
per=int(input("Enter the percentage: "))
if(per>=60):
    print("DFirst div")
if(per>=75):
    print("With Distriction")
else:
    print("Pass")
"""



"""
10/9/25
"""

"""
1. Switch case: 
num=int(input("Enter the number of row"))
match num:
 case 1:print("Sunday")
 case 2:print("Monday")
 case 3:print("Tuesday")
 case _:print("Invalid Choice")
 """  

"""
char = input("Enter a char")
if (len(char)==1):
   match char:
       case 'a':print("Vowel")
       case 'e':print("Vowel")
       case 'i':print("Vowel")
       case 'o':print("Vowel")
       case 'u':print("Vowel")
       case   _:print("Constant")
else:
   print("INVALID")
"""

"""
2. While loop when number of iterations are known
i=1
while(i<=5):
    print("HEllo world!")
    i+=1
"""

"""
3. while loop when number of iteration are unknown
while True:
    print("Hello World")
    choice=input("Do you want to print it again y/n")
    if(choice=='n'):
        break
"""


"""
check whetehr random number is equal, high or low to given number
import random
num=random.randint(1,100)
while True:
    num1=int(input("Enter the number:"))
    if(num1>num):
        print("Number is High")
    elif(num1<num):
        print("Number to low")
    else:
       break
   """



"""
12/09/25
"""
"""
arr=[10,20,30,40,50]
print(arr[0])
print(arr[1])
print(arr[2])
"""


""""
while loop
arr=[10,20,30,40,50]
i=0
while(i<5):
 print(arr[i])
 i+=1
"""

"""
taking global len of array
arr=[10,20,30,40,50]
i=0
while(i<len(arr)):
 print(arr[i])
 i+=1
"""


"""
for loop

arr=[10,20,30,40,50]
for i in arr:
 print(i)
"""

"""
2nd way of for loop
for i in [10,20,30,40,50]:
 print(i)
 """

"""
square
for i in [10,20,30,40,50]:
 print(i,i**2,sep="->")
"""


"""end ka use
for i in [10,20,30,40,50]:
 print(i,end=" ")
"""

"""
for i in ["Payal","Mahi","Simarn","Balke"]:
 print(i,end=" ")
"""

"""
for i in 12345:
 print(i,end=" ")
"""
"""
for i in '12345':
 print(i,end=" ")
"""

"""
for i in "12345":
 print(i,end=" ")
"""

"""
for i in 123.45:
 print(i,end=" ")
"""


"""
for i in "123.45":
 print(i,end=" ")
"""

"""
for i in [1,1,1,1,1,]:
  print("HEllo")
"""

"""
print(range(20))
"""

"""
for i in range(20):
  print(i)
"""

"""
stop range
for i in range(200):
  print("Hello")

  by default value is zero
"""


"""
start,stop range
for i in range(11,20):
  print("Hello",end=" ")
"""

"""
start,stop,step
for i in range(11,20,2):
  print(i)
"""

"""
for i in range(5,100,5):
  print(i)
"""

"""
for i in range(100,4,-5):
  print(i)
  """


"""
isma else if ka andr h
arr=[1,3,6,8,9]
num=int(input("Enter the number"))
for i in arr:
    if num==i:
        print("Element Found")
        break
    else:
        print("Not Found")
"""

"""
for-else
arr=[1,3,6,8,9]
num=int(input("Enter the number"))
for i in arr:
    if num==i:
        print("Element Found")
        break
else:
        print("Not Found")
"""

"""
arr=[1,3,6,8,9]
num=int(input("Enter the number"))
flag=0
for i in arr:
    if num==i:
        flag=1
        print("Element Found")
        break
    
if(flag==0):
        print("Not Found")
"""

10
"""
i=int(input("Enter "))
for i in range(i+1):
      print(i)
"""

"""
Write a program to print all natural numbers from 1 to n using while loop

n=int(input("Enter n"))
i=1
while(i<=n):
    print(i)
    i+=1
"""

"""
Write a program to print all natural numbers in reverse from n to 1 using while loop
n=int(input("Enter n"))
i=1
while(i<=n):
    print(n)
    n-=1
"""

"""
Write a program to print all even numbers from 1 to 100 using while loop

n=int(input("Enter n"))
i=0
while(i<=n):
    print(i)
    i+=2
"""

"""
Write a program to print all sum numbers from 1 to 100 using while loop

n=int(input("Enter n"))
i=1
sum=0
while(i<=n):
    sum=sum+i;
    i+=1

print(sum)
"""

"""
Write a program to print sum of all even numbers from 1 to 100 using while loop"""

n=int(input("Enter n"))
i=0
sum=0
while(i<=n):
    sum=sum+i;
    i+=2

print(sum)
