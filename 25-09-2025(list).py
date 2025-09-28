# list mai contain different type of object

lst=[12,12.4,True,"James",12+5j,[12,34,6]]
for i in lst:
  print(i,type(i))

lst=[12,12.4,True,"James",12+5j,[12,34,6],sum,len] #yh sum aur len function lsit mai operations perform kraga
for i in lst:
  print(i,type(i))

# list can also hold function inside it
lst=[12,12.4,True,"James",12+5j,[12,34,6],sum,len] #yh sum aur len function lsit mai operations perform kraga
print(lst[-1]("Payal")) 
# same for sum
  
# list can grow and shrink at runtime  isma ek hi ID grow aur shrink toh ID sbki same hogi
lst=[]
print(lst,id(lst))
lst.append(10)
print(lst,id(lst))
lst.append(20)
print(lst,id(lst))
lst.append(30)
print(lst,id(lst))
lst.append(40)
print(lst,id(lst))
lst.append(50)
print(lst,id(lst))
del(lst[-1])
print(lst,id(lst))


# Nested lsit: a list of list
lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:  # cl h yha child pura list ka jaisa [1,2,3] [4,5,6]
    for ele in cl:  #ele hi each elemnt in child list  like 
        if(ele%2==0):
          print("*",end=" ")
        else:
          print(" ",end=" ")
    print()


lst=[[1,2,3],[4,5,6],[7,8,9]]
for cl in lst:  
    for ele in cl: 
        print(ele**2,end=" ")
    print()


lst=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j]=lst[i][j]**2
    print(lst,end=" ")
print()


#  Square of evry number in alist having elements as numbers and list
lst=[[1,2,3],4,5,6,[7,8,9]]
for i in lst:
    if(type(i)==list):
        for j in i:
            print(j**2,end=" ")
    else:
        print(i**2,end=" ")

# Employee record  in list of multiple object types
lst=[]
n=int(input("Enter the numberof objects"))
for i in range(n):
   num=eval(input("Enter the num"))
   lst.append(num)
print(lst)


# list functions
lst=[]
lst.append("james")   # append add the element at the end of list
lst.insert(1,"Payal")      # insert If i want to insert at specific location  we have to give index value
lst.insert(1,"Payal")      # isma index 1 wala phla wala payal index 2 pa shift hojayga
lst.append(12)
lst.append(True)
print(lst)
print(lst.count("Payal"))    # Count specifies  the occurrence
print(lst.index("Payal"))   # index value sbsa phla wala payal ki dega
print(lst.index("Payal",2,7))   # index range  start index aur end index



lst1=["red","Green","Blue"]  # 
lst2=["Orange","Skyblue","Black"]
lst1=lst1+lst2
print(lst1)   # isma mera object alg bnaga


# 2nd waylst1=["red","Green","Blue"]  (Extend)
lst1=["red","Green","Blue"]
lst2=["Orange","Skyblue","Black"]
lst1.extend(lst2)   # object same rahaga
print(lst1)
   
lst1=["red","Green","Blue"]   # append 
lst2=["Orange","Skyblue","Black"]
for i in lst2:
    lst1.append(i)
    print(lst1)


lst=list(range(2,11,2))   
print(lst)
res=lst.pop()  #pop nikalka return bhi krta hai
print(f"popped element is {res}")
print(lst)

# agr muja particular index ka element pop krna hai toh
lst=list(range(2,11,2))   
print(lst)
res=lst.pop(1)  #pop nikalka return bhi krta hai  1 is index here
print(f"popped element is {res}")
print(lst)


lst=["james","Payal","Neena","Neena"]
lst.remove("Neena")   # remove ki liya chahaiya value aur phli occureence kragalst.remove("Neena")  
del[lst[0]]  # index ka basis pr delection
print(lst)
lst.clear()  # remove all from list
print(lst)

lst=["james","payal","neena","neena"]
print(f"Before: {lst}")
lst.sort()
print(f"After: {lst}")


# If in descending order
lst=["james","payal","neena","neena"]
print(f"Before: {lst}")
lst.sort(reverse=True)
print(f"After: {lst}")   # isma yh problem ayyai ki abb muja phla wali list nhi milagi 
print(lst)


lst=["james","payal","neena","neena"]
print(f"Before: {lst}")
res=sorted(lst)
print(f"After: {res}")   # yh nyi sorted list bnayga aur original wali preserve rhagi
print(f"After: {lst}")

