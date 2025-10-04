# Methods in dictinary

# 1 updating new dictionary
d={}
d1={"r":"red"}
d2={"g":'green'}
d.update(d1)
d.update(d2)
print(d)

d={}
d1={"r":"red"}
d2={"g":'green'}
for i in d1,d2:
    d.update(i)
print(d)
 # 2. setdefault
d={}
d1={"r":"red"}
d2={"g":'green'}
for i in d1,d2:   # override nhi kraga
    d.update(i)
print(d)
d.setdefault("g","grey")
d.setdefault("b","blue")
print(d)

# 3. clear
d={}
d1={"r":"red"}
d2={"g":'green'}
for i in d1,d2:   # override nhi kraga  voh value hogi vhi dekhayga aur nhi hoga the it will add
    d.update(i)
print(d)
d.setdefault("g","grey")
d.setdefault("b","blue")
print(d)
d.clear()
print(d)

# 4. pop item (return kraga deleted value)
d={}
d1={"r":"red"}
d2={"g":'green'}
for i in d1,d2:   # override nhi kraga
    d.update(i)
print(d)
d.setdefault("g","grey")
d.setdefault("b","blue")
print(d)
print(d.popitem())    # it always removes the last item
print(d)


# if want to remove specific item
d={}
d1={"r":"red"}
d2={"g":'green'}
for i in d1,d2:   # override nhi kraga
    d.update(i)
print(d)
d.setdefault("g","grey")
d.setdefault("b","blue")
print(d)
print(d.pop("g"))    # it always removes the item based on key
print(d)


# if i want only keys of a dictionary
d={'r':'red','g':'green','b':'blue'}
d2=dict.fromkeys(d,0)
print(d2)

# iteration in dictionary:
d={'r':'red','g':'green','b':'blue'}
d2=dict.fromkeys(d,0)
print(d2)
for i in d:
    print(i, d[i])
for i in d.keys():
    print(i)
for i in d.items():
    print(i)

    # if i want keys and values different
for i,j in d.items():
    print(i)

print(d.keys())  # yh keys list in format mai dega
print(d.values())  
print(d.items())  # yh tuple format mai key aur values dega

# print(d.get("z"))
# print("Important code")   # key hogi toh output aayaga nhi toh none dega

print(d.("z"))
print("Important code")   # key hogi toh output aayaga nhi toh none dega

# length of characters in string
lst=["James","Mahi","Payal","Simran"]
lst1=[]
for i in lst:
    lst1.append(len(i))
print(lst1)

lst=["James","Mahi","Payal","Simran"]
for i in lst:
    if(len(i)<5):
        lst.append(i)
print(lst)

