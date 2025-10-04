a=int(input("Enter the first objects"))
b=int(input("Enter the second objects"))
c=int(input("Enter the case number"))
match c:
    case 1:  print(f"Addition of {a} and {b} is: ",a+b)
    case 2:  print(f"Subtraction of {a} and {b} is: ",a-b)
    case 3:  print(f"Multiplication of {a} and {b} is: ",a*b)
    case 4:  print(f"Division of {a} and {b} is: ",a//b)
    case 5:  print(f"Modulus of {a} and {b} is: ",a%b)
    case _:print("Invalid!")

    