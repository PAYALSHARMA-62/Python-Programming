lst=["james","neena","blake","neena","anna"]
print(f"Before reverse:{lst}")   # orginal list hi change hogi
lst.reverse()
print(f"After reverse:{lst}")


#I i want to have other object of reversed lst
lst=["james","neena","blake","neena","anna"]
print(f"Before reverse:{lst}")   # orginal list hi change hogi
result=list(reversed(lst))   # reverse krna pa huma ek reverse iterator milta hai then i want to change t into list
print(f"After reverse:{result}")
print(f"After reverse:{lst}")

 3 Interning
lst1=[10,[100]]  # isma 10 immutable h aur [100] mutable
lst2=lst1
print(lst1,lst2)
print(id(lst1),id(lst2))

lst1=[10,[100]]  # isma 10 immutable h aur [100] mutable
lst2=lst1
lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)


#Copy function  shallow copy
lst1=[10,[100]]  # isma 10 immutable h aur [100] mutable
lst2=lst1.copy()   # this is shallow copy aur isma immutable mai change nhi dekhaga but mutable mai change hoga
lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)


 #deep copy isma lst2 ka bhi child list  alg bnaya aur usma changes hoga
 import copy
lst1=[10,[100]]  # isma 10 immutable h aur [100] mutable
lst2= copy.deepcopy(lst1)   # deep copy is not a function of list it isa fn of copy module
print(lst1,lst2)
lst2[0]=20
lst2[1].append(200)
print(lst1,lst2)

# lst2=lst1    Interning
# lst2=lst1.copy()    Shallow copy
# lst2= copy.deepcopy(lst1)   deep copy