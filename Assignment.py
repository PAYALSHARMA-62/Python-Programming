FILENAME = 'students.txt'

# Load all students from file
def load_students():
    students = {}
    try:
        with open(FILENAME, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    roll = parts[0]
                    name = parts[1]
                    marks = list(map(int, parts[2].split(',')))
                    students[roll] = {'name': name, 'marks': marks}
    except FileNotFoundError:
        pass
    return students

# Save all students to file
def save_students(students):
    with open(FILENAME, 'w') as f:
        for roll, data in students.items():
            marks_str = ','.join(map(str, data['marks']))
            f.write(f"{roll}|{data['name']}|{marks_str}\n")

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
