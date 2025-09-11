Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1=12.34
int(num1)
12
int("1234")
1234
int("123.456")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("123.456")
ValueError: invalid literal for int() with base 10: '123.456'
num=0b101
num
5
int(0b101)
5
int("0b101")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int("0b101")
ValueError: invalid literal for int() with base 10: '0b101'
int("0b101",2)
5
int("0o123",8)
83
int("0xF",16)
15
float(123)
123.0
float("123.45")
123.45
str(123)
'123'
num1=1000
num2="1000"
num1+num2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    num1+num2
TypeError: unsupported operand type(s) for +: 'int' and 'str'
num1+int(num2)
2000
str(num1)+num2
'10001000'
eval("123")
123
eval("123.45")
123.45
eval("name")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    eval("name")
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'name' is not defined
eval("'name'")
'name'
name=123
eval("name")
123
eval("12*6//3")
24


num1=10
num2=4
print("Sum=",num1+num2)
Sum= 14
print("Sub=",num1+num2)
Sub= 14
print("Sub=",num1-num2)
Sub= 6
print("product=",num1*num2)
product= 40
print("div=",num1/num2)
div= 2.5
print("mod=",num1%num2)
mod= 2
print("floor=",num1//num2)
floor= 2
print("Exp=",num1**num2)
Exp= 10000
print("Hello")
Hello
print(10//0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(10//0)
ZeroDivisionError: integer division or modulo by zero
print(10/0)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(10/0)
ZeroDivisionError: division by zero


a=10
a++
SyntaxError: invalid syntax
++a
10
a=a+1
a
11
a=a-1
a
10
a-=1
a
9
a*=10
a
90
a=b=c=d=10
a,b,c,d
(10, 10, 10, 10)
a==b-=2
SyntaxError: 'comparison' is an illegal expression for augmented assignment
a+=b-=2
SyntaxError: invalid syntax
a=10
b=20
c=30
a<b
True
a<b<c
True
a,b>c
(10, False)

a=1000
id(a)
2361543450032
b=a
id9b)
SyntaxError: unmatched ')'
id(b)
2361543450032
a is b
True
int a=1000
SyntaxError: invalid syntax
id(a)
2361543450032
b=a
id(b)
2361543450032
c=1000
id(c)
2361543450576
a is c
False
a==c
True
a=100
>>> b=100
>>> a is b
True
>>> a=256
>>> b=256
>>> a is b
True
>>> a=-5
>>> b=-5
>>> a is b
True
>>> a=257
>>> b=257
>>> a is b
False
>>> a=-6
>>> b=-6
>>> a is b
False
>>> 
>>> 
>>> 30 in [10,20,30,40,50]
True
>>> "j" in "james"
True
>>> "P" in "payal"
False
>>> 
>>> 
>>> num1=2
>>> num2=3
>>> print(num1&num2)
2
>>> print(num1|num2)
3
>>> print(num1^num2)
1
>>> print(num1~num20
...       
SyntaxError: '(' was never closed
>>> print(num1~num2)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> ~num1
...       
-3
