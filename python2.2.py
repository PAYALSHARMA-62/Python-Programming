Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1=12.5
type(num)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(num)
NameError: name 'num' is not defined. Did you mean: 'num1'?
type(num1)
<class 'float'>
id(num1)
1871196453488
num1+=num1+100
num1
125.0
help(keyword)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    help(keyword)
NameError: name 'keyword' is not defined. Did you forget to import 'keyword'?
help(keywords)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined
help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

int(123.89)
123
int=100
int(123.78)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(123.78)
TypeError: 'int' object is not callable
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'int', 'num1']
int
100
int()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int()
TypeError: 'int' object is not callable
del(int)
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'num1']
int(123.90)
123
num1=1000
type(num1)
<class 'int'>
num1=0b101
num1
5
num1=0b101

num1=1111
num1
1111
num1=00123
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
num1=0o123
num1
83
num1=0o282
SyntaxError: invalid digit '8' in octal literal
num1=0xF
num1
15
num1=0xface
num1
64206
num1=0xzoom
SyntaxError: invalid hexadecimal literal

num1=15
bin(num1)
'0b1111'
num1=face
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    num1=face
NameError: name 'face' is not defined
num1="Face"
bin(num1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    bin(num1)
TypeError: 'str' object cannot be interpreted as an integer
num1=15
bin(num1)
'0b1111'
oct(num1)
'0o17'
hex(num1)
'0xf'
num1=123.45
type(num1)
<class 'float'>
num1=2e2
num1
200.0
num1=3e2
num1
300.0
num1=12+5j
type(num1)
<class 'complex'>
num1
(12+5j)
num2
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    num2
NameError: name 'num2' is not defined. Did you mean: 'num1'?
num2=3_7j
num1
(12+5j)
num2
37j
num1+num2
(12+42j)
num1.real
12.0
num1.img
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    num1.img
AttributeError: 'complex' object has no attribute 'img'. Did you mean: 'imag'?
num1.real
12.0
num1.imag
5.0
num1.conjugate()
(12-5j)
c=12j+5
c
(5+12j)
passexam=True
type(passexam)
<class 'bool'>
True==1
True
False==0
True
True>False
True
st="python"
print(st)
python
type(st)
<class 'str'>
py="Payal"
print(py)
Payal
type(py)
<class 'str'>
num1=123.456
float(num10
      float(num1)
      
SyntaxError: '(' was never closed
float(num1)
      
123.456
int(num1)
      
123
num1
      
123.456
num1=int(num1)
      
num1
...       
123
>>> num1=int("1234")
...       
>>> num1
...       
1234
>>> num1=int("1234.56")
...       
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    num1=int("1234.56")
ValueError: invalid literal for int() with base 10: '1234.56'
>>> num1=int("A")
...       
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    num1=int("A")
ValueError: invalid literal for int() with base 10: 'A'
>>> float(123)
...       
123.0
>>> float("123")
...       
123.0
>>> num1=123
...       
>>> num2="123"
...       
>>> num1+num2
...       
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    num1+num2
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> num1+int(num20
... 
...          num1
...          
SyntaxError: '(' was never closed
>>> num1+int(num2)
...          
246
>>> str(num1)+num2
...          
'123123'
