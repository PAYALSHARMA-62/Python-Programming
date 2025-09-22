## methods in string function
print(dir(str))



## upper charcters
st="welcome to my class"
st=st.upper()
st=st.lower()
st=st.capitalize() ## if i want to captilized letter
st=st.title() ## Agr muja hr ekk character upper mai chahiya toh
st=st.swapcase() ## if i want to swap upper and lower
print(st)

## formatted string
name="Payal"
age=20
print("MY name is",name,"and my age is",age,"Yaers old")
print("MY name is " +name+ " and my age is",str(age),"Yaers old")
print("My name is %s and i am %d years old"%(name,age))  ## If i dont want to use these format specifiers then use format functions
print("My name is {} and i am {} years old" .format(name,age))  ## Formated function
print(f"My name is {name} and i am {age} years old")  ## small f isko btayga ki yh varibales hai agr small f nhi diya toh satement ko as it is 
                                                            ## print kr dega

emp=[101,"James","james@gmail.in",10]
print("Empid:{}, name:{}, email:{}, did:{}".format(*emp))  ## * is variable length argumet string  unpacking the emp list


st="welcome to my class"
st=st.upper()
st=st.lower()
