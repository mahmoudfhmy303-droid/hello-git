
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Grade:", self.grade)
        if self.grade >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")


s1 = Student("Ali", 85)
s2 = Student("Omar", 72)
s3 = Student("Sara", 96)
s4 = Student("Mona", 45)
s5 = Student("Youssef", 68)

students = [s1, s2, s3, s4, s5]

total = 0
highest = students[0]

print("STUDENT GRADE REPORT")
print("-" * 30)

for student in students:
    student.display()
    print("-" * 30)
    total += student.grade

    if student.grade > highest.grade:
        highest = student

average = total / len(students)

print("Class Average:", average)
print("Highest Grade:", highest.grade)
print("Top Student:", highest.name)