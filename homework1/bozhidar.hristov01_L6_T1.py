class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getCourses(self):
        for course_id, course_name in self.courses.items():
            print(f"{course_id} {course_name}")
    
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}
    
    def getSalary(self):
        return self.salary
    
    def addCourse(self, course_id, course_name):
        self.courses[course_id] = course_name

class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, course_id, year):
        self.courses[course_id] = {'grades' : [], 'year' : year}

    def addGrade(self, course_id, grade):
        if course_id in self.courses:
            self.courses[course_id]['grades'].append(grade)

    def getAvgGrade(self, course_id):
        if course_id in self.courses:
            grades = self.courses[course_id]['grades']
            if len(grades) > 0:
                return sum(grades) / len(grades)
        return 0