from bozh import *
# Тестове за класовете Teacher и Student
def test_teacher():
    print("=== Тестване на клас Teacher ===")
    # Създаване на учител
    teacher = Teacher('Иванов', 35, 2500)
    print(f"Учител: {teacher.name}, Възраст: {teacher.age}, Заплата: {teacher.getSalary()}")
    
    # Добавяне на курсове
    teacher.addCourse('MATH101', 'Математика 1')
    teacher.addCourse('PHY201', 'Физика 2')
    teacher.addCourse('CSC101', 'Въведение в програмирането')
    
    # Извеждане на курсовете
    print("Курсове на учителя:")
    teacher.getCourses()
    print()

def test_student():
    print("=== Тестване на клас Student ===")
    
    # Създаване на студент
    student = Student('Петров', 20)
    print(f"Студент: {student.name}, Възраст: {student.age}")
    
    # Записване на курсове
    student.attendCourse('MATH101', 2023)
    student.attendCourse('PHY201', 2023)
    student.attendCourse('CSC101', 2024)
    
    # Добавяне на оценки
    student.addGrade('MATH101', 5)
    student.addGrade('MATH101', 6)
    student.addGrade('PHY201', 4)
    student.addGrade('PHY201', 5)
    student.addGrade('CSC101', 6)
    
    # Опит за добавяне на оценка към несъществуващ курс
    student.addGrade('BIO301', 3)
    
    # Извеждане на курсовете и оценките
    print("Курсове на студента:")
    student.getCourses()
    print()
    
    # Изчисляване на средни оценки
    print("Средни оценки:")
    print(f"MATH101: {student.getAvgGrade('MATH101')}")
    print(f"PHY201: {student.getAvgGrade('PHY201')}")
    print(f"CSC101: {student.getAvgGrade('CSC101')}")
    print(f"BIO301 (несъществуващ): {student.getAvgGrade('BIO301')}")
    print()

def test_edge_cases():
    print("=== Тестване на гранични случаи ===")
    
    # Студент без курсове
    student2 = Student('Георгиев', 22)
    print(f"Студент без курсове: {student2.name}")
    print("Курсове на студент без курсове:")
    student2.getCourses()
    print(f"Средна оценка за несъществуващ курс: {student2.getAvgGrade('MATH101')}")
    print()
    
    # Учител без курсове
    teacher2 = Teacher('Димитрова', 28, 2200)
    print(f"Учител без курсове: {teacher2.name}")
    print("Курсове на учител без курсове:")
    teacher2.getCourses()
    print()

def test_inheritance():
    print("=== Тестване на наследяването ===")
    
    # Проверка дали класовете наследяват SchoolMember
    teacher = Teacher('Стоянов', 40, 3000)
    student = Student('Михайлова', 21)
    
    print(f"Учителят е SchoolMember: {isinstance(teacher, SchoolMember)}")
    print(f"Студентът е SchoolMember: {isinstance(student, SchoolMember)}")
    print(f"Учителят има име: {teacher.name}")
    print(f"Учителят има възраст: {teacher.age}")
    print(f"Студентът има име: {student.name}")
    print(f"Студентът има възраст: {student.age}")

if __name__ == "__main__":
    test_teacher()
    test_student()
    test_edge_cases()
    test_inheritance()