"""
Function Demo  #docstring comment
Dev By KSG
"""
def add(num1:int,num2:int)->int:
    "add 2 numbers and return an integer"   #block level comment
    return num1+num2    # return sum to its calling environment this is called document a function   # inline  comment

print(help(add))
 # if i want to show help then put it in triple single or triple doublequotes



# Paramters:
# 1.Variable Argument (n numbers ka sum) for this we need 4th parmter var arg
def add(*vararg):
    # avrarg Demo
    print(vararg)

add()
add(1)
add(1,2)   # it works on n number of positional argument
add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5,6,7,7,8,9,9,0)

#2.method
def add(*vararg):
    sum=0
    for i in vararg:
        sum+=i
    print(f"Sum of nums= {vararg}")

add()
add(1)   
add(1,2)
add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5,6,7,7,8,9,9,0)


# vararg cannot tackle keyword argument like print(a=10,b=20,c=40)
# to tackle it use keyvarargument
def add(**keyvararg):
    sum=0       # through tuple
    print(keyvararg)

add(a=10,b=20,c=30,d=40)



#
def add(**keyvararg):
    print("Sum of elements: ",sum(keyvararg.values()))
                                                           # for dictionary
add(a=10,b=20,c=30,d=40)


"""
def testpara(a,b,*c,d=10,e=20,**f):
    print(f"""
     a={a}  # a=10
    b={b}   #b=20
    c={c}   #c=(30,40,50)    # extra positional
    d={d}   #d=10 
    e={e}   #e=20
    f={f}    #f={100,200,300}    # extra keyword arg
    """)
testpara(10,20,30,40,50,x=100,y=200,z=300)

"""
# order:
# mandatory
# vararg
# optional/default/keyword arg
# keyvararg
"""


#
def greet():
   return "Hello World"

result=greet()    # result ids reference variable and return is object
print(result)

#
def greet():
   return "Hello World"

result=greet    # greet contains the adress of greet fn()
print(result)

#
def greet():
   return "Hello World"

result=greet    # yha variabl emai function address dalka variable call kru toh voh bhi fn bnn jata h
print(result())



# Lambda Expression
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    inner()

outer()
inner()   # we cantnot call the inner function directly give error



# if i want to use inner after the outer function
def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    return inner

i=outer()    # i storing inner ka adress
i()      # function reurning from function


def outer():
    print("Hello from outer function")
    def inner():
        print("Hello from inner function")
    return inner()

i=outer()    # i() gives error bcz we return the function inerr()  
i()      