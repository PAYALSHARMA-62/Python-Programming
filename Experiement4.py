# program to perform linear search and Binary search
#Linear search
lst=[]
n=int(input("Enter the number of objects"))
num1=int(input("searched no"))
for i in range(n):
    num=eval(input("Enter the num"))
    lst.append(num)
print(lst)
# for i in range(n):
 if(lst[i]==num1):
    print(f"Number found! {lst[i]}")
    break
else:
    print("Number not found!")

# another method through mapp
lst=[]
n=int(input("Enter ur limit"))
lst=list(map(int,input(f"Enter  {n} number separted by space").split(" ")))
print(lst)
lst.sort()
print(f"After sorting list {lst}")
min=0
max=len(lst)-1
num=int(input("Enter the number to be searched: "))
while(min<=max):
    mid=(min+max)//2
    if(num==lst[mid]):
      print(f"Number is found {mid}")
      break
    elif(lst[mid]<num):
      max=mid-1
    else:
      min=mid+1
else:
    print("Elemnt not found!")