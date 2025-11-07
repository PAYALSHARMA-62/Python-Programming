""" inheitance: Code reusability, cost effective and reduces efforts and time effective
It means refining our code
Inheritance is a mechanism of acquiring some attributs of any existing class type into a new class type.
One of the key concept of OOPS
establish a hierachical elatinship among classes.
Established a superclasses/subclasses relationship
Establishes "is a" relationships.

Composition means has a relationship   eg: Car has a Audio system
Inheritance means Is a relationship     eg: Neurosurgen is a doctor



Benefits:
reusability of code
put code in one class, use it in all the subclasses
Write general purpose code designed for a supertype that works for all subtypes.
A superclass defines a genaral set of fuctionality, whereas subclasses define functionality specific to them.

Base class/ superclass/ parent class
derived class/ subclass/child class


1. Simple/ single Inheritance :   base-> Derived
2. Multiple Inheritance:    Base1        Base2
                              ^            ^
                              |            |
                               Derived class

3. Mulilevel
4. Hierarichal
5. Hybrid   (Hierarichal+Multilevel)
6. Diamond 


syntax for inheritance
class derivedclassname(Baseclassname):
    <statement1>
    ...
    <statement2>



if import from another module
class derivedclassname(Modulename.baseclassname):
    pass  (jb block ka andr kuch aur na likhna ho agr khali chooda toh error ayyga toh pass likhdo)
 and thses types of class which contains no code are called minial class and are  used only for inhritance


Break,continue and pass are transfer statements
"""

class Employee:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
    
    def EmpDetails(self):
        print(f"""
Eid: {self.eid}
Ename: {self.ename}
""")

class RegEmp(Employee):
    pass


#2. Hierarichal Inheritance
class Employee:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
    
    def EmpDetails(self):
        print(f"""
Eid: {self.eid}
Ename: {self.ename}
""")


class RegEmp(Employee):
    def __init__(self,eid,ename,basic,hra,da):
        super().__init__(eid,ename)
        self.basic=basic
        self.hra=hra
        self.da=da
        self.salary=self.basic+self.hra+self.da*30

    def printRegEmp(self):
        super().EmpDetails()
        print(f"""
Basic: {self.basic}
HRA: {self.hra}
DA: {self.da}
Salary: {self.salary}
""")

class DailyWagerEmp(Employee):
    def __init__(self,eid,ename,wage,nod):
        super().__init__(eid,ename)
        self.wage=wage
        self.nod=nod
        self.salary=self.wage*self.nod

    def printdailyWagerEmp(self):
        super().EmpDetails()
        print(f"""
Wage: {self.wage}
No. of days: {self.nod}
Salary: {self.salary}
""")



obj2=RegEmp(101,"James",200,3000,12)
obj2.printRegEmp()

obj3=DailyWagerEmp(102,'neena',900,40)
obj3.printdailyWagerEmp()





#3. Multilevel Inheritance
class Employee:
    def __init__(self,eid,ename,email):
        self.eid=eid
        self.ename=ename
        self.email=email
    
    def EmpDetails(self):
        print(f"""
Eid: {self.eid}
Ename: {self.ename}
Email: {self.email}
""")


class Manager(Employee):
    def __init__(self,eid,ename,email,dept):
        super().__init__(eid,ename,email)
        self.dept=dept


    def ManagerDetails(self):
        super().EmpDetails()
        print(f"""
Department: {self.dept}
""")

class Director(Manager):
    def __init__(self,eid,ename,email,dept,location):
        super().__init__(eid,ename,email,dept)
        self.location=location

    def DirectorDetails(self):
        super().ManagerDetails()
        super().EmpDetails()
        print(f"""
location: {self.location}
""")


obj1=Director(101,'james',"jhsjhf","CSE","delhi")
obj1.DirectorDetails()





#4. Multiple Inheritance
class Employee:
    def __init__(self,eid,ename,email):
        self.eid=eid
        self.ename=ename
        self.email=email
    
    def EmpDetails(self):
        print(f"""
Eid: {self.eid}
Ename: {self.ename}
Email: {self.email}
""")

class Developer:
    def __init__(self,proglang,workex):
        self.proglang=proglang
        self.workex=workex

    def DeveloperDetails(self):
        print(f"""
programming language: {self.proglang}
Work Experience: {self.workex}
""")


class Manager(Employee,Developer):
    def __init__(self,eid,ename,email,proglang,workex,dept,location):
        Employee.__init__(self,eid,ename,email)
        Developer.__init__(self,proglang,workex)
        self.dept=dept
        self.location=location

    def ManagerDetails(self):
        super().EmpDetails()
        super().DeveloperDetails()
        print(f"""
Department: {self.dept}
Location: {self.location}
""")



obj3=Manager(102,'neena',"fahgda","CPP",12,"CSE","Delhi")
obj3.ManagerDetails()