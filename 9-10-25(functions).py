# python supports pass by value(Where the value is always an object reference, not the value of the object)
# Hence many professionals term it as Pass by object reference   
lst=[10,20,30]
lst2=lst
print(lst2 is lst)   # it will be true as output 


lst=[10,20,30]
lst2=lst.copy()
print(lst2 is lst)  

lst=[10,20,30]
lst2=lst
lst[-1]=300
print(lst2)

lst="jame"
lst2=lst
lst=lst+"bond"
print(lst2)


# Argument passing mechanism in python
lst="MIET"
def test(p):
    p.append("JAMMU")    # yha pr p aur lst dono ek hi hai
print(lst)
test(lst)
print(lst)

lst="MIET"
def test(p):
    p=p+"JAMMU"    # yha nya object bnn rha hai

print(lst)
test(lst)
print(lst)


lst=["MIET"]
def test(p):
    p=["JAMMU"]    # yha nya object bnn rha hai

print(lst)
test(lst)
print(lst)


lst=["MIET"]
def test(p):
    p.append("JAMMU")   # yha nya object bnn rha hai

print(lst)
test(lst)
print(lst)



# Scope; 1. Local VAriable  2. Global Variable
# Local Variable: The Variable defined within the function has a local scope and hence they are called local variable
# Local scope means they can be accessed within the function only
# They appear when the function
# Scope are; Local, Enclosing, Built-in and Global

  
  
   # buit-in   if not in built in then exception
num=10   # global level
def parent():  # parent is enclosing block here
    num=100
    def lcl():
        num=1000    # local scope
        print(num)


#
num=10
def test():
    num=100
    print(num)

test()
print(num)



#
num=10
def test():
    num+=100
    print(num)   # we are modifying the global value in local toh error ayyga

test()
print(num)



#
num=100
def test():
    global num
    num+=100
    print(num)   

test()
print(num)



# call stack: shows curently execution fn. in our environment
def fun2():
    z=30
    print("Inside function2")

def fun1():
    y=20
    print("Inside function1")
    fun2()
    print("End of fun1")

print("Inside main")
fun1()
print("End of main")
       # Ek function sa dusra function pr jump krna is context switching


# Type of function parameters
# 1. Mandatory position
# 2. OPTIOnal
# 3. var argument
# 4. key var argument
# 5. Keyword

# 1. mandatory parameter
def name(fname):
    print(f"fname:{fname}")

name()


# correct way4
def name(fname):
    print(f"fname:{fname}")

name("James")


# type hinting
def name(fname:str)->None:   # means devloper wants/demanding string trype  None means no return type
    print(f"fname:{fname}")

name("James")


def name(fname:int)->int:   # means devloper wants/demanding string trype  None means no return type
    print(f"fname:{fname}")

name("James")


def name(fname,lname):
    print(f"fname:{fname}  lname:{lname}")

name("James","Bond")



# if i want lsatname optional
def name(fname,lname="NA"):
    print(f"fname:{fname}  lname:{lname}")

name("James")   # if lname is given in print then it will overrite the NA


#
def name(fname,mname="NA",lname="NA"):
    print(f"fname:{fname} Mname:{mname} lname:{lname}")

name("James",lname="Bond")  
#Agr phla keyword argumnet sa shuru kr diya toh end bhi keyword argument sa krna pdaga
# like we cannt give print(fname="james","k","bond")
# print("james",fname="nenna",lastname="k",mname="bond")   error dega

# sumof 2, 3 or any numbers
def add(num1,num2):
    return num1+num2

def add(num1,num2,num3):
    return num1+num2+num3

def add(num1,num2,num3,num4):
    return num1+num2+num3+num4   #isma 1st fn ko override kraga 2nd fn and 2nd fn ko override kraga 3rd fn toh 3rd wala function hi chalagaa

print(add(1,2,3,4))



def add(num1,num2):
    return num1+num2

def add(num1,num2,num3):
    return num1+num2+num3

def add(num1,num2,num3=0,num4=0):
    return num1+num2+num3+num4    #agr muja 1st function chalana ha  overrloading not allowe in python

print(add(1,2,3,4))