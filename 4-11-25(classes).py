""" Student  Management record  
properties that define object is instance of member"""
class Student:
    def __init__(self):
        self.sid=None
        self.name=None
        self.branch=None
        self.sem=None
        self.cgpa=None  
     # self.sid=None   is public
        # self._sid=None  is protected  (just like public ) it is standard not rule in ptyhon
        # self.__sid=None is private 


    def setData(self,sid,name,branch,sem,cgpa):
        self.sid=sid
        self.name=name
        self.branch=branch
        self.sem=sem
        self.cgpa=cgpa

    def printDetails(self):
        print(f"""
Sid:{self.sid}
Name:{self.name}
Branch:{self.branch}
Semester:{self.sem}
CGPA:{self.cgpa}
""")


obj=Student()     # it is the object
obj.printDetails()

obj.setData(12,"Jmes","CSE",5,9)
obj.setData(13,"Neena","IT",4,8)
obj.printDetails()



#   constructor parametrized ek hi brr constructor use hota h aur update ka liya setdata fn use hoa toh dono important h
class Student:
    cname="MIET"
    def __init__(self,sid,name,branch,sem,cgpa,email):
        self.sid=sid
        self.name=name
        self.branch=branch
        self.sem=sem
        self.cgpa=cgpa
        self.email=email
     # self.sid=None   is public
        # self._sid=None  is protected  (just like public ) it is standard not rule in ptyhon
        # self.__sid=None is private 


    def printDetails(self):
        print(f"""
Sid:{self.sid}
Name:{self.name}
Branch:{self.branch}
Semester:{self.sem}
CGPA:{self.cgpa}
Email:{self.email}
College Name:{Student.cname}
""")

 
obj1=Student(12,"Jmes","CSE",5,9,'james@hmail.in')     # constructor is calling here   obj1 is referring to object ko bnna h heap mai
obj1.printDetails()
obj2=Student(13,"Neena","IT",4,8,'neena@hmail.o')   #d dataset is updatig
obj2.printDetails() 



#self is current object reference   in C++ it is called this 
# mtlb ob1 na call kiya toh ib1 ko represent krunga obj2 na call kiya toh ob2 ko represent krunga



# the mabers which are shared or common amog all the objects voh costructor/object mai nhi bnta  , class ka andr bnnaga and is called class variable
# each object can access it



# functionality dena h jisma student apni email update kr aaya
class Student:
    cname="MIET"
    def __init__(self,sid,name,branch,sem,cgpa,email):
        self.sid=sid
        self.name=name
        self.branch=branch
        self.sem=sem
        self.cgpa=cgpa
        self.email=email
     
    def updateEmail(self,newemail):   # setter functions
        self.email=newemail


    def printDetails(self):
        print(f"""
Sid:{self.sid}
Name:{self.name}
Branch:{self.branch}
Semester:{self.sem}
CGPA:{self.cgpa}
Email:{self.email}
College Name:{Student.cname}
""")

 
obj1=Student(12,"Jmes","CSE",5,9,'james@hmail.in')     # constructor is calling here   obj1 is referring to object ko bnna h heap mai
obj1.printDetails()
obj2=Student(13,"Neena","IT",4,8,'neena@hmail.o')   #d dataset is updatig
obj2.printDetails() 

obj2.updateEmail("Neenaxyz.com")
obj2.printDetails()


# to update class variables we need to create sattic function jiska self parameter nhi hota
class Student:
    cname="MIET"
    def __init__(self,sid,name,branch,sem,cgpa,email):
        self.sid=sid
        self.name=name
        self.branch=branch
        self.sem=sem
        self.cgpa=cgpa
        self.email=email
     
    def updateEmail(self,newemail):   # setter functions
        self.email=newemail

    @staticmethod
    def updatecname(newcname):
        Student.cname=newcname



    def printDetails(self):
        print(f"""
Sid:{self.sid}
Name:{self.name}
Branch:{self.branch}
Semester:{self.sem}
CGPA:{self.cgpa}
Email:{self.email}
College Name:{Student.cname}
""")

 
obj1=Student(12,"Jmes","CSE",5,9,'james@hmail.in')     # constructor is calling here   obj1 is referring to object ko bnna h heap mai
obj1.printDetails()
obj2=Student(13,"Neena","IT",4,8,'neena@hmail.o')   #d dataset is updatig
obj2.printDetails() 

obj2.updateEmail("Neenaxyz.com")
obj2.printDetails()


Student.updatecname("JammuMiet")
obj2.printDetails()
obj1.printDetails()




# 
class Employees:
    Cname="Tesla"
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal



    def setdata(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal


    def updatesal(self,newsal):
        self.sal=newsal

    @staticmethod
    def Update(newCname):
        Employees.Cname=newCname

    def Details(self):
        print(f"""
Eid: {self.eid}
Ename: {self.ename}
Salary: {self.sal}
Cname: {self.Cname}
""")

obj1=Employees(101,"Neha",2000)
obj1.Details()
obj2=Employees(102,"Mah",3000)
obj2.Details()


obj2.updatesal(6000)
obj1.Details()
obj2.Details()

Employees.Update("Amazon")
obj1.Details()
obj2.Details()








import json

FILENAME = 'students.txt'

# Load all students from file
def load_students():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except:
        return {}

# Save all students to file
def save_students(students):
    with open(FILENAME, 'w') as f:
        json.dump(students, f)

# Add new student
def add_student():
    students = load_students()
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = []
    for i in range(5):
        m = int(input(f"Marks for subject {i+1}: "))
        marks.append(m)
    students[roll] = {'name': name, 'marks': marks}
    save_students(students)
    print("Student added!\n")

# Show all students
def show_all():
    students = load_students()
    for roll, data in students.items():
        print("Roll No:", roll, "Name:", data['name'], "Marks:", data['marks'])

# Total, average, and grade
def result(roll):
    students = load_students()
    if roll in students:
        marks = students[roll]['marks']
        total = sum(marks)
        avg = total // 5
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Total: {total}, Average: {avg}, Grade: {grade}")
    else:
        print("Student not found!")

# Search student
def search():
    students = load_students()
    to_search = input("Enter roll no or name: ")
    found = False
    for roll, data in students.items():
        if roll == to_search or data['name'].lower() == to_search.lower():
            print(roll, data)
            found = True
    if not found:
        print("Not found!")

# Update marks
def update():
    students = load_students()
    roll = input("Roll No to update: ")
    if roll in students:
        marks = []
        for i in range(5):
            m = int(input(f"New marks for subject {i+1}: "))
            marks.append(m)
        students[roll]['marks'] = marks
        save_students(students)
        print("Updated!\n")
    else:
        print("Student not found!")

# Delete student
def delete():
    students = load_students()
    roll = input("Roll No to delete: ")
    if roll in students:
        del students[roll]
        save_students(students)
        print("Deleted!\n")
    else:
        print("Student not found!")

# Show topper(s)
def topper():
    students = load_students()
    max_total = -1
    toppers = []
    for data in students.values():
        total = sum(data['marks'])
        if total > max_total:
            max_total = total
            toppers = [data['name']]
        elif total == max_total:
            toppers.append(data['name'])
    print("Topper(s):", ', '.join(toppers), "with marks:", max_total)

# Menu
while True:
    print("\n1.Add 2.Show All 3.Result 4.Search 5.Update 6.Delete 7.Topper 8.Exit")
    ch = input("Choice: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        show_all()
    elif ch == '3':
        roll = input("Enter roll no: ")
        result(roll)
    elif ch == '4':
        search()
    elif ch == '5':
        update()
    elif ch == '6':
        delete()
    elif ch == '7':
        topper()
    elif ch == '8':
        break
    else:
        print("Try again.")





import json
from datetime import datetime

books = {}

def save_books():
    with open('books.json', 'w') as f:
        json.dump(books, f)

def load_books():
    global books
    try:
        with open('books.json', 'r') as f:
            books = json.load(f)
    except:
        books = {}

def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    copies = int(input("Copies: "))
    books[book_id] = {'title': title, 'author': author, 'genre': genre, 'copies': copies}
    save_books()

def display_catalog():
    load_books()
    for book_id, info in books.items():
        print(f"{book_id}: {info}")

def search_books():
    query = input("Enter title or author: ").lower()
    load_books()
    for info in books.values():
        if query in info['title'].lower() or query in info['author'].lower():
            print(info)

def issue_book():
    book_id = input("Book ID to issue: ")
    user = input("User name: ")
    load_books()
    if book_id in books and books[book_id]['copies'] > 0:
        books[book_id]['copies'] -= 1
        save_books()
        today = datetime.now().strftime('%Y-%m-%d')
        record = {'book_id': book_id, 'user': user, 'date': today}
        try:
            with open('issued.json', 'r') as f:
                issued = json.load(f)
        except:
            issued = []
        issued.append(record)
        with open('issued.json', 'w') as f:
            json.dump(issued, f)
        print("Book issued.")
    else:
        print("Not available.")

def return_book():
    book_id = input("Book ID to return: ")
    load_books()
    if book_id in books:
        books[book_id]['copies'] += 1
        save_books()
        print("Book returned.")
    else:
        print("Invalid ID.")

def display_by_genre():
    genre = input("Genre: ").lower()
    load_books()
    genre_books = set()
    for book_id, info in books.items():
        if info['genre'].lower() == genre:
            genre_books.add(info['title'])
    print("Books in genre:", genre_books)

def delete_zero_books():
    load_books()
    keys_to_delete = [book_id for book_id, info in books.items() if info['copies'] == 0]
    for book_id in keys_to_delete:
        books.pop(book_id)
    save_books()
    print("Zero-copy books deleted.")

def books_issued_today():
    today = datetime.now().strftime('%Y-%m-%d')
    try:
        with open('issued.json', 'r') as f:
            issued = json.load(f)
        for record in issued:
            if record['date'] == today:
                print(record)
    except:
        print("No books issued today.")

def main():
    load_books()
    while True:
        print("\nMENU:")
        print("1. Add Book 2.Display Catalog  3.Search Book  4.Issue Book 5.Return Book  6.Display Genre Books 7. Delete Zero Copy Books 8.Books Issued Today 9.Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            display_catalog()
        elif choice == '3':
            search_books()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            display_by_genre()
        elif choice == '7':
            delete_zero_books()
        elif choice == '8':
            books_issued_today()
        elif choice == '9':
            save_books()
            print("All changes saved. Bye!")
            break
        else:
            print("Invalid choice.")

main()
