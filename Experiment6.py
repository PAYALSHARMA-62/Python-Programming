# Write a program to create PGt

a=int(input("Enter the first objects"))
b=int(input("Enter the second objects"))
c=int(input("Enter the third number"))
if(a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
    print("The triangle is Right Angled Triangle")
else:
    print("The triangle is not Right Angled Triangle")
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)**0.5)
print("Area of the triangle= ",area)