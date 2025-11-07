# Multilevel Inheritaance
class Parent1:
    def fun1(self):
        print("Hello from fun1")

class Parent2(Parent1):
    def fun2(self):
        print("Hello from fun2")

class child(Parent2,Parent1):   # parent2 is child of parent1  MRO(Method resolution order) yh exception tb aati h jb tum parent phla likho aur child baad mai
                                    # agr maina Parent1,Parent2 diya toh yh exception MRO aayga
    def fun3(self):
        print("Hello from fun3")

ob=child()
ob.fun1()
ob.fun2()
ob.fun3()


 """Abstract classes are those having fn declaration but having missing definition
Example fruit is abstract classes and apple,mango are objects  

the claases which define rule for below classes
  Abstarct class object cannot be created

"""



# Overriding with Inheritance
# Polymorphism with Inheritance
from abc import ABC, abstractclassmethod
class MediaPlayer(ABC):
    def PlayAudio(self):
       print("Can play Audio!")    # yh compulsory h
    
    @abstractclassmethod
    def PlayVideo(self):        # it is abstract classs
        pass

                                              #agr abstractclass method parent mai bna diya toh usko child sa bypass krns pdaga
class SoundRecorder(MediaPlayer):
    def PlayVideo(self):
        print("I can't play video")

class VlcPlayer(MediaPlayer):
    def PlayVideo(self):
        print("I can play video")


sr=SoundRecorder()
sr.PlayAudio()
sr.PlayVideo()

vlc=VlcPlayer()
vlc.PlayAudio()
vlc.PlayVideo()


#2.
from abc import ABC, abstractclassmethod
class Bird(ABC):
    def speak(self):
       print("Can play speak!")    # yh compulsory h
    
    @abstractclassmethod
    def Fly(self):        # it is abstract classs
        pass

                                              #agr abstractclass method parent mai bna diya toh usko child sa bypass krns pdaga
class Penguine(Bird):
    def Fly(self):
       pass                     # yh exception dega  bcz yh bird ka child h to isma abstract class nhi bnn skti

class Parrot(Bird):
    def fly(self):
        print("I can play Fly")


p=Parrot()
p.speak()
p.Fly()

# 0r ob:Bird=Parrot()



#3. Overriding with inheritance
# Polymorphism without Inheritance
from abc import ABC, abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def PrintArea(self):        
        pass

    @abstractclassmethod
    def PrintPerimeter(self):
        pass

class Square(Shape):
    def PrintArea(self,a):
        area=4*a
        print("Area of Square: ",{area})

    def PrintPerimeter(self,b):
        best=b*b
        print("Perimeter: ",{best})


s=Square()
s.PrintArea(2)
s.PrintPerimeter(3)


# Overriding without Inheritance
                                              #agr abstractclass method parent mai bna diya toh usko child sa bypass krns pdaga
class Dog:
    def Speak(self):
       print("Dogs barkkks")                    # yh exception dega  bcz yh bird ka child h to isma abstract class nhi bnn skti

class Cat:
    def Speak(self):
        print("cat meaaaaooon")


def sound(obj):
    obj.Speak()

d=Dog()
sound(d)
c=Cat()
sound(c)



# object as insatnce
class Address:
    def __init__(self,street,city,state):
        self.street=street
        self.city=city
        self.state=state

    def PrintAddress(self):
        print(f"""Street: {self.street}

City: {self.city}
State: {self.state}""")

class Student:
    def __init__(self,rollno,name,address):   #address yh object
        self.rollno=rollno
        self.name=name
        self.address=address
    
    def PrintDetails(self):
        print(f"rollno:{self.rollno} name:{self.name}")
        self.address.PrintAddress()

class Employee:
    def __init__(self,eid,ename,address):   #address yh object
        self.eid=eid
        self.ename=ename
        self.address=address
    
    def PrintDetails(self):
        print(f"Eid:{self.eid} Ename:{self.ename}")
        self.address.PrintAddress()

add=Address("Sector-18",'Noida',"UP")
stu=Student(101,"james",add)
stu.PrintDetails()

emp=Employee(1001,"king",add)
emp.PrintDetails()