st="hello"
print(st,id(st)) #st mai main object ki id : 11 22 33 33 44
for i in st:
    print(i,id(i))

st="misssissippi" #->5 objects total : multiple sss ko 1 s , multiple ko count as 1 only.
print(st,id(st)) #st mai main object ki id : 11 22 33 33 44
for i in st:
    print(i,id(i))

# m i sss i ss i pp i
# 1 2 333 2 33 2 44 2

st="welcome"
print(st[::-2]) #begigning from end : then 2 is begining from end and go till begining

st="welcome"
print(st[::2]) 

# melcowe : swap first two and last two char of string : min length of string : 4 
st=input("enter a string")
if(len(st)>=4):
    print(st[-2:]+st[2:-2]+st[:2])


#indexing and slicing:
st="abracadabra"
# output: abr$c$d$br$ : first not change:
s=st[0]
for i in st[1:]:#first occurance chodkr baaki sb 
    if i==st[0]:
        s+='$'
    else:
        s+=i
print(s)


#give string upper case and convert to lower case:
st=input("enter a string")
print(st.lower())
