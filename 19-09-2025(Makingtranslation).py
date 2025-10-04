st="python is a high level language"
# jitne bhi vowels hain unhe specific char ke puche kro hide;
st1="aeiou" #jinkko hide krna ha 
st2="*****" # a ko 1 se,  2 ko b se  and so on
#transition table: which helps in masking (mapping table)
ttab=str.maketrans(st1,st2)
print(ttab) #gives ascii code  of a: 1 and so on
print(st.translate(ttab))



st="hello"
print(st.upper()) # st is a string object and we can apply any function  on it
print(str.upper(st))#method 2  object nhi hota too string class ka use hota ha


#masking:
st="python is an object orientedprogramming language"
st1="aeiou"
st2="12345" #st1 char replaced by st2
#---now mapping table:
ttab=str.maketrans(st1,st2)
print(ttab) #--returns dictionary: pass this fn to translate fn jo string mein data ko hde krta ha 
res=st.translate(ttab)    #ttab is translation table
print(st)
print(res) #--> masked characters.
# if u want to hide , then give space or replace by **: used for shiphered text



import string #sare   variables pehle se bane hain
print(string.ascii_lowercase)
print(string.ascii_uppercase)
#special symbols in punctuation
print(string.ascii_letters)
print(string.octdigits)



#make sipher text: secret letter:
st="python is an object orientedprogramming language"
import string
st1=string.ascii_lowercase
st2=st1[::-1] # z to a 
print(st1,st2,sep="\n")
ttab=str.maketrans(st1,st2)
print(ttab) #->mapping table
res=st.translate(ttab)
print(st)
print(res)
print(res.translate(ttab))# to decode again



#function returns diff types of objects: string to list conversion:

st="noida,dehradun,jammu,delhi,ghaziabad"  
#to convert string in an array 
res=st.split(",") #here comma is delimeter  list conatiaing string objects as members
print(res) #returns list  

st="noida,dehradun,jammu,delhi,ghaziabad" 
#to convert string in an array 
res=st.split(",",maxsplit=2) #here comma is delimeter  list conatiaing string objects as members
print(res) #returns list  

st="noida,dehradun,jammu,delhi,ghaziabad" 
#to convert string in an array 
res=st.split(",",maxsplit=1) #maxsplit kii kitne parts mien todna ha 
print(res) #returns list   

st="noida,dehradun,jammu,delhi,ghaziabad" 
#to convert string in an array 
res=st.split("e") #maxsplit kii kitne parts mien todna ha 
print(res) #returns list   


st="noida,dehradun,jammu,delhi,ghaziabad" 
#to convert string in an array 
res=st.split(",") #maxsplit kii kitne parts mien todna ha 
print(res) #returns list   
newstr="*".join(res) #glue string ke pieces joins
print(newstr)

#leading aur trailing char ko hatata ha : lstrip

#llstrip used to delete leading / starting character 
#rstrip delted end characters.
st="Mr james,Mr king,Mr blue,Mr black"  # want names to eliminate Mr only
res=st.split(",")
print(res)
for i in res:
    print(i.lstrip("Mr "))

st="Mr james.,Mr king.,Mr blue.,Mr black."  # want names to eliminate Mr only
res=st.split(",")
print(res)
for i in res:
    print(i.rstrip("."))




st="malyalam"
print(st.lstrip("ma"))

st="malyalam"
print(st.rstrip("m"))

st="malyalam"
print(st.rstrip("am"))

#for deleeting leading and trailing both:
#use strip
st="malyalam"
print(st.strip("m")) 


#by deaault removes extra spaces:
st="            malyalam            "
print(st.strip())


#isvalid is a function: returns bool value : true if string has all characters as digits.

contactno=input("enter ur number")
if contactno.isdigit() and len(contactno)==10:
    print("valid contact")
else:
    print("invalid contact")


contactno=input("enter ur number")
if contactno.isalnum(): #alphabtes with digits without space
    print("valid contact")
else:
    print("invalid contact")


contactno=input("enter ur number")
if contactno.islower():
    print("valid contact")
else:
    print("invalid contact")

contactno=input("enter ur number")
if contactno.isupper():
    print("valid contact")
else:
    print("invalid contact")


#replace;
st="python is a high level language"
res=st.replace("python","JavaScript")
print(res)

#to delete by replace:
st="python is a high level language"
res=st.replace("python"," ")
print(res)

st="python is a high level language"
res=st.replace(" ","") #space ko replace 
print(res)

#2 nos input : addition
num1=int(input("enter num1"))
num2=int(input("enter num2"))  #->map, reduce, filter 

#single statement input in one time:
st="welcome"
print(st[::-1])

print(st[6::-1])


numlist=input("enter 5 numbers sep by space")
print(numlist) #returns a string of numbers 

#use split:
numlist=input("enter 5 numbers sep by space").split()
print(numlist) #now returns diff numbers:
# now list to map: har ek value pr integer fn apply kro

#use split:
a,b,c,d,e=map(int,input("enter 5 numbers sep by space").split())
# now list to map: har ek value pr integer fn apply kro
print(a,b,c,d,e) #for fixed inputs


#list se :
a=list(map(int,input("enter 3 numbers sep by space").split()))
print(a) #for not fixed inputs 


st="hello"
st=st.upper()
print(st.count("L"))

print("hello".upper().count("L")) # Method Changing: string pr har function apply krskte hain
#int ke agge . se function nhi legea by . int ka hi funciton legaga : sirf string pr hi krskte hain string ke int ka nhi
# string ke agge . se string fn aur int ke agge . se int functions : int ke agge . se string fn nhi legea na string ke agge . se int fn nhi

# a ko dollar se replace: pehle wale a ko chodkr
st="abracadabra"
print(st[0]+st[1:].replace("a","$"))



st=["Racecar","123@Madam","hello","Noon"]
#to convert string in an array 
 #here comma is delimeter  list conatiaing string objects as members
st.remove("hello")
print(st)

#string ko list mein convert krke:
st = "Racecar,123@Madam,hello,Noon"

lst = st.split(",")   # string → list

for i in range(len(lst)):
    lst[i] = lst[i].replace("hello", "")   # har element me replace

print(lst)