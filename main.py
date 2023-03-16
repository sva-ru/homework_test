class Student:
    list_all_student = []
    # avg_gr = 0.0
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.__add_student__()
    def __add_student__ (self):
        self.list_all_student.append(self)
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and all(i in range(1, 11) for i in grade):
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка'
    def avg_grade_course(list_student, course):
        sum_gr = 0
        count_grade = 0
        for it in list_student:
            for cr, gr in it.grades.items():
                if cr == course:
                    count_grade += len(gr)
                    sum_gr += sum(gr)
        if count_grade != 0:
            return round(sum_gr / count_grade, 2)
        return ""
    def avg_grade (self):
        avg_list = []
        for i in self.grades.values():
            avg_list += i
        return round(sum(avg_list) / len(avg_list),2)

    def __str__(self):
        txt = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\n'
        txt += f'Курсы в процессе изучения: {", ".join(self.grades.keys())}\n'
        txt += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return txt

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __lt__(self, lecturer):
        avg_gr_st = self.avg_grade()
        avg_gr_lec = lecturer.avg_grade()
        return avg_gr_st < avg_gr_lec

    def __gt__(self, lecturer):
        avg_gr_st = self.avg_grade()
        avg_gr_lec = lecturer.avg_grade()
        return avg_gr_st > avg_gr_lec



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    list_all_lecturer = []
    # avg_gr = 0.0
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.course = ''
        self.__add_lecturer__()
    def __add_lecturer__(self):
        self.list_all_lecturer.append(self)
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}')
    #
    def avg_grade_course(list_lecturer, course):
        sum_gr = 0
        count_grade = 0
        for it in list_lecturer:
            for cr, gr in it.grades.items():
                if cr == course:
                    count_grade += len(gr)
                    sum_gr += sum(gr)
        if count_grade != 0:
            return round(sum_gr / count_grade, 2)
        return ""
    def avg_grade (self):
        avg_list = []
        for i in self.grades.values():
            avg_list += i
        return round(sum(avg_list) / len(avg_list), 2)

    def __lt__(self, student):
        avg_gr_lec = self.avg_grade()
        avg_gr_st = student.avg_grade()
        return avg_gr_st < avg_gr_lec

    def __gt__(self, student):
        avg_gr_lec = self.avg_grade()
        avg_gr_st = student.avg_grade()
        return avg_gr_st > avg_gr_lec


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def  __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}')


# Создаем два объекта из класса Student, заполяем их атрибуты
best_student = Student('Ruoy', 'Eman', 'man')
best_student2 = Student('Pac', 'Man', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Sql']
best_student.add_courses('Java')
# Создаем два объекта из класса Reviewer, заполяем их атрибуты
coll_reviewer = Reviewer('Vasya', 'Sokolov')
coll_reviewer.courses_attached += ['Python']
coll_reviewer.courses_attached += ['Sql']
coll_reviewer2 = Reviewer('Vlad', 'Vladovich')
coll_reviewer2.courses_attached += ['Java']
# Создаем два объекта из класса Lecturer, заполяем их атрибуты
cool_lecturer = Lecturer('Vova','Ivanov')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2 = Lecturer('Bill', 'Billy')
cool_lecturer2.courses_attached += ['Python']
# метод выставления оценок лекторам у класса Student
best_student.rate_lecturer(cool_lecturer, 'Python', [1,2,4,5])
best_student.rate_lecturer(cool_lecturer2, 'Python', [3,2,4,10])
# метод выставления оценок студентам у класса Reviewer
coll_reviewer.rate_hw(best_student, 'Python', 5)
coll_reviewer.rate_hw(best_student, 'Python', 10)
coll_reviewer.rate_hw(best_student, 'Sql', 8)
# функция для подсчета средней оценки за лекции всех лекторов в рамках курса
print(Lecturer.avg_grade_course(Lecturer.list_all_lecturer, 'Python'))
# функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
print(Student.avg_grade_course(Student.list_all_student, 'Sql'))
# функция для подсчета средней оценки за домашние задания у класса Student
avg_gr = best_student.avg_grade()
# функция для подсчета средней оценки за лекции у класса Lecturer
avg_gr = cool_lecturer.avg_grade()
# Перезагрузка магического метода __str__ у всех классов
print(coll_reviewer)
print(cool_lecturer)
print(best_student)
# сравнение между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания
print(cool_lecturer < best_student)
print(cool_lecturer > best_student)