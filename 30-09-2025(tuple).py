# tuple properties:

t=tuple("james")
print(t,type(t))
t=('j','a','m','e','s')


t=10,20,30
print(t,type(t))   # jb bhi multiple values ek value mi daala toh this is called packing


t=(10,20,30)
print(t,type(t))
a,b,c=t   # unpacking
print(f"a:{a} b:{b} c:{c}")    # t mai jitna valus h utna hi pack variables hona chahiya

# Star wal aprograms(  unpackings)
t=10,20,30,40,50
print(t)
a,*b=t  # phli value a  mai jaygi aur baki sari b mai list bnaga
print(a,b)


t=10,20,30,40,50
print(t)
a,*b,c=t  # phli value a  mai jaygi aur baki sari b mai list bnaga
print(a,b,c)


t=10,20,30,40,50
print(t)
*a,b,c=t  # phli value a  mai jaygi aur baki sari b mai list bnaga
print(a,b,c)

t=10,20
print(t)
a,*b,c=t  # phli value a  mai jaygi aur baki sari b mai list bnaga
print(a,b,c)

# swap
num1=input("Enter first number:")
num2=input("Enter Second number:")
print(f"Before swap num1:{num1} num2:{num2}")
temp=num1
num1=num2
num2=temp
print(f"After swap num1:{num1} num2:{num2}")


num1,num2=input("Enter first number:"),input("Enter Second number:")  # tuple
print(f"Before swap num1:{num1} num2:{num2}")
num1,num2=num2,num1
print(f"After swap num1:{num1} num2:{num2}")


#fibonacci (Classical Approach)
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(8):
    num3=num1+num2
    print(num3,end=" ")
    num1=num2
    num2=num3


num1,num2=0,1
for i in range(10):
  print(num1,end=" ")
  num1,num2=num2,num1+num2

# have class int 
num1=(10)
print(type(num1))

# having class tuple identfied by ,
num1=(10,)
print(type(num1))

# in tuple modification  no can be done

# Methods in tuple  count, Index
 t=(10,20,30,40,50)
 print(t[0],t[-1],t[::-2],t[::-1])
t[0]=1000
 print(t[0])    # it shows error
 del(t[-1])   # can't delete



t=(12,12.4,"james",12+5j,True,[1,2,3,4])# tuple can hold anything inside it
t[-1].append(1000)
print(t)

 t=(10,20,30,40,50)
print(t.count(30))
print(t.index(40))


# Dictionaries:
# 1. It is not a sequence (indexing and slicing are not allowed)
# 2. It is an un-ordered collection
# 3. It is mutable(operations like insertion updation and deletion)
# 4. It may contains dupliacte values but key are always unique)
# 5. It preserves the insertion ordered
# 6. it may contains only imuutable type of object as keys but any type of obj as values



#1. property
name={"james":5000,"Gagan":5000,"Khushi":6000,"Prabh":3000,"Mahi":2000} # whenever we want tight bonding between the values we use 
#print(name[-1])   # (Key arror) exception aayga because indexing is not allowed
print(name["Mahi"])

#2. property
d1={'r':'red','b':'blue'}
d2={'b':'blue','r':'red'}
print(d1==d2)

#3. property
#d=dict()    empty dict ka yh do tarika
d={}
d['r']='red'   # yh dekhaga ki r ka koi keyboard ha agr h toh override hoga nhi toh add hoga
print(d,id(d))
d['b']='blue' 
print(d,id(d))
d['b']='black'      # tis shows that both insertion and updation are allowed
print(d,id(d))
d['c']='green'     
print(d,id(d))
del(d['r'])      #deletion
print(d,id(d))

#Hashing    :  can be applied on immutable type of object   in mutable object(list) hashing is not allowed, dictionary also

d={"int":10,"str":"james","list":[10,20,30],"tuple":(10,),[2]:[10,2]}
print(d)

d={"int":10,"str":"james","list":[10,20,30],"tuple":(10,)}
print(d)

# in dictionary keys are immutable type of object values can be anything