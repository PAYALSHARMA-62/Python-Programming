# list
# 'james' "james" '''james''' 
#  [12,34,5,67] =>list
# [12 34 5 6] => ndarray
#  (12 34 5 6) =>tuple  
# {12 34 5 6} =>set
#   [1:23,2:45} =>dictionary

# list creating ways 1. with the help of list constructor 2. put data in square bracket
#  1. list() : When we want to convert existing object it to list
#  2. []:  when we want to create new list obj

# lst=list()   these are two ways for list defining
lst=[]
print(lst,type(lst))

st="HELLO"
lst=list(st)
 print(lst)  # bna hua obj ko list mai create krna hai

or
lst=['H','O','L','E']

# in list int float are not allowed


lst=list(1234)  # isma hamesha sequence jaygi , iterable 
 print(lst)  

lst=[10,20,30,40]
for i in lst:
   print(i,end=" ")
   print(lst[-3:],end=" ")
   print(lst[0],lst[:3])
   print(lst[-4:3])

lst=[10,20,30,40]
print(lst[::2])  # forward
print(lst[::-1])  # reverse
