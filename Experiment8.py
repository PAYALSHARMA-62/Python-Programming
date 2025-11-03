"""Write a program to illustrate iteration over the list and the dictionary"""

lst=["C","PYTHON","JAVA","C#","C++","PHP"]
print("List basis Iteration: ")
for i in lst:
    print(i,end=" ")
    
dict={"Subject":"chemistry","Code":"101","Marks":"92","Opted number":"20"}
print("\n\nKeys Basis Iteration: ")
for keys in dict.keys():
    print(keys,end=" ")


print("\n\nValues Basis Iteration: ")
for values in dict.values():
    print(values,end=" ")

print("\n\nItems Basis Iteration: ")
for items in dict.items():
    print(items,end=" ")
    


    