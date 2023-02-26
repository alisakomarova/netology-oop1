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

def avg_grade_common(people_list, course_name):
    sum_of_one_course = 0
    count = 0
    for person in people_list:
        sum_of_one_person = 0
        count_of_one_person = 0
        for course, grades_list in person.grades.items():
            if course == course_name:
                sum_of_one_person += sum(grades_list)
                count_of_one_person += len(grades_list)
        sum_of_one_course += sum_of_one_person
        count += count_of_one_person
    if count == 0:
        return 'Нет оценок'
    avg = sum_of_one_course / count
    return avg

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

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'SQL', 6)
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

print(best_student)
print(second_student)
print(cool_lecturer)
print(second_lecturer)
print(f'Средний балл у best_student ниже, чем у second_student? - {best_student<second_student}')
print(f'Средний балл у second_lecturer ниже, чем у cool_lecturer? - {second_lecturer<cool_lecturer}')

avg_python = avg_grade_common(list_of_students, 'Python')
avg_sql = avg_grade_common(list_of_students, 'SQL')
avg_git = avg_grade_common(list_of_students, 'Git')
print(f'Средний балл по курсу Python среди всех студентов: {avg_python}')
print(f'Средний балл по курсу SQL среди всех студентов: {avg_sql}')
print(f'Средний балл по курсу Git среди всех студентов: {avg_git}')

avg_python_lecturers = avg_grade_common(list_of_lecturers, 'Python')
avg_sql_lecturers = avg_grade_common(list_of_lecturers, 'SQL')
avg_git_lecturers = avg_grade_common(list_of_lecturers, 'Git')
print(f'Средний балл по курсу Python среди всех лекторов: {avg_python_lecturers}')
print(f'Средний балл по курсу SQL среди всех лекторов: {avg_sql_lecturers}')
print(f'Средний балл по курсу Git среди всех лекторов: {avg_git_lecturers}')