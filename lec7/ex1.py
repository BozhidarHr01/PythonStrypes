class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    
    def info(self):
        return f"Name: {self.name}, age: {self.age}"

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses_teching = {}

    def add_course(self, course_name):
        if course_name not in self.courses_teching:
            self.courses_teching[course_name] = {"course_name": course_name}
            return f"Course {course_name} added to list"
        else:
            return f"Course {course_name} already in list"

    def info(self):
        base_info = super().info() 
        courses_list = list(self.courses_teching.keys())

        return f"{base_info}, Salary: {self.salary}, Courses teaching: {courses_list}"

class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses_studying = {}

    def join_course(self, course_name, year):
        if course_name not in self.courses_studying:
            self.courses_studying[course_name] = {"year": year, "grades" : []}
            return f"Joined course {course_name}, {year}"
        else:
            return f"Already in course {course_name}"

    def add_grade(self, course_name, grade):
        if course_name in self.courses_studying:
            self.courses_studying[course_name]["grades"].append(grade)
            return f"Grade {grade} added for course {course_name}"
        else:
            return f"Not in course {course_name}"
        
    def info(self):
        base = super().info()
        courses_info = []
        for course_name, info in self.courses_studying.items():
            courses_info.append(f"{course_name} ({info['year']}): {self.courses_studying[course_name]}")
        courses_str = "; ".join(courses_info)
        return f"{base}, Courses: {courses_str}"


teacher1 = Teacher("Ivan Ivanov", 35, 2500)
teacher2 = Teacher("Maria Ivanova", 32, 2000)

teacher1.add_course("Maths")
teacher2.add_course("Physics")

student1 = Student("Petar Georgiev", 18)
student2 = Student("Ivan Petrov", 20)

student1.join_course("Maths", 2024)
student2.join_course("Physics", 2023)

student1.add_grade("Maths", 4.37)
student2.add_grade("Maths", 3)
student2.add_grade("Physics", 5.23)

print(teacher1.info())
print(teacher2.info())

print(student1.info())
print(student2.info())
