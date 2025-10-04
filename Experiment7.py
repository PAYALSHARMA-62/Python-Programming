stulist=[]
num=int(input("Enter number of students:"))
for i in range(num):
    d={}
    rno=int(input("Enter roll no: "))
    name=input("Enter name: ")
    branch=input("Enter branch: ")
    email=input("Enter email: ")
    d={"r":rno,"n":name,"b":branch,"e":email}
    stulist.append(d)
for i in stulist:
    print(i)
#search
num=int(input("Enter the rollno to be searched: "))
found=0
for i in stulist:
    if(i["r"]==num):
        print("found: ",i)
        found=1
        break
if(found==0):
    print("Not found!")