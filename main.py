class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self, grades):
        sum_of_one_course = 0
        count = 0
        for grades_list in grades.values():
            sum_of_one_course += sum(grades_list)
            count += len(grades_list)
        if count == 0:
            return 'Нет оценок'
        avg = sum_of_one_course/count
        return avg

    def __str__(self):
        average_grade = self.avg_grade(self.grades)
        c_in_progress = ', '.join(self.courses_in_progress)
        c_finished = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}\nКурсы в процессе изучения: {c_in_progress}\nЗавершенные курсы: {c_finished}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение')
            return
        if not other.grades:
            print('Недостаточно данных для сравнения')
            return
        if not self.grades:
            print('Недостаточно данных для сравнения')
            return
        return self.avg_grade(self.grades) < other.avg_grade(other.grades)

def avg_grade_for_course(students_list, course_name):
    for student in students_list:
        sum_of_one_course = 0
        count = 0
        for course in student.grades.keys():
            if course == course_name:
                for grades_list in student.grades.values():
                    sum_of_one_course += sum(grades_list)
                    count += len(grades_list)
                if count == 0:
                    return 'Нет оценок'
        avg = sum_of_one_course / count
        return avg

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self, grades):
        sum_of_one_course = 0
        count = 0
        for grades_list in grades.values():
            sum_of_one_course += sum(grades_list)
            count += len(grades_list)
        if count == 0:
            return 'Нет оценок'
        avg = sum_of_one_course/count
        return avg

    def __str__(self):
        average_grade = self.avg_grade(self.grades)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение')
            return
        if not other.grades:
            print('Недостаточно данных для сравнения')
            return
        if not self.grades:
            print('Недостаточно данных для сравнения')
            return
        return self.avg_grade(self.grades) < other.avg_grade(other.grades)

    def avg_grade_for_course(lecturers_list, course_name):
        for lecturer in lecturers_list:
            sum_of_one_course = 0
            count = 0
            for course in lecturer.grades.keys():
                if course == course_name:
                    for grades_list in lecturer.grades.values():
                        sum_of_one_course += sum(grades_list)
                        count += len(grades_list)
                    if count == 0:
                        return 'Нет оценок'
            avg = sum_of_one_course / count
            return avg

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


list_of_students = []
list_of_lecturers = []

best_student = Student('Semen', 'Semenov', 'm')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['SQL']
list_of_students.append(best_student)

second_student = Student('Ivan', 'Ivanov', 'm')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['SQL']
list_of_students.append(second_student)

cool_reviewer = Reviewer('Servey', 'Sergeev')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Andrey', 'Andreev')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['SQL']

cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(second_student, 'Python', 3)
second_reviewer.rate_hw(second_student, 'SQL', 7)
second_reviewer.rate_hw(second_student, 'Python', 10)

cool_lecturer = Lecturer('Vasiliy', 'Vasilyev')
cool_lecturer.courses_attached += ['Git']
cool_lecturer.courses_attached += ['SQL']
cool_lecturer.courses_attached += ['Python']
list_of_lecturers.append(cool_lecturer)

second_lecturer = Lecturer('Petr', 'Petrov')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['SQL']
list_of_lecturers.append(second_lecturer)

best_student.rate_hw(cool_lecturer, 'Git', 10)
best_student.rate_hw(cool_lecturer, 'Git', 9)
best_student.rate_hw(cool_lecturer, 'SQL', 10)
best_student.rate_hw(second_lecturer, 'SQL', 7)
second_student.rate_hw(second_lecturer, 'Python', 10)

print(list_of_students)
print(list_of_lecturers)
print(best_student)
print(second_student)
print(cool_lecturer)
print(second_lecturer)
print(best_student<second_student)
print(second_lecturer<cool_lecturer)


list_of_students = [best_student, second_student]
list_of_lecturers = [cool_lecturer, second_lecturer]
print(avg_grade_for_course(list_of_students, 'Python'))
print(avg_grade_for_course(list_of_lecturers, 'SQL'))