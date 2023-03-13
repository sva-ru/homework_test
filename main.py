class Student:
    list_all_student = []
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
        return sum(avg_list) / len(avg_list)

        # sum(list(i[0]) / len(list(i[0])
            # / len(self.grades.values())
    # and grade in self.range_grades
    # def add_courses(self, course_name):
    #     self.finished_courses.append(course_name)
    # def  __str__(self):
    #     pass

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    list_all_lecturer = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.course = ''
        self.__add_lecturer__()
    def __add_lecturer__(self):
        self.list_all_lecturer.append(self)
    def __str__(self):
        print(f'Имя: {self.name} \nФамилия: {self.surname}')
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
    # def  __str__(self):
    #     print(f'Имя: {self.name} \nФамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'man')
best_student2 = Student('Pac', 'Man', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Sql']


coll_reviewer = Reviewer('Vasya','Sokolov')
coll_reviewer.courses_attached += ['Python']
coll_reviewer.courses_attached += ['Sql']
#
cool_lecturer = Lecturer('Vova','Ivanov')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2 = Lecturer('Bill','Gets')
cool_lecturer2.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', [1,2,4,5])
best_student.rate_lecturer(cool_lecturer2, 'Python', [3,2,4,10])
coll_reviewer.rate_hw(best_student, 'Python', 5)
# coll_reviewer.rate_hw(best_student, 'Python', 10)
coll_reviewer.rate_hw(best_student, 'Sql', 8)

# coll_reviewer.rate_hw(best_student, 'Python', 15)
# coll_reviewer.rate_hw(best_student, 'Sql', 5)
# coll_reviewer.rate_hw(best_student, 'Sql', 12)

print(best_student.grades)
# print(cool_lecturer.grades)
# coll_reviewer.__str__()
# cool_lecturer.__str__()

# print(Student.list_all_student)
# print(Lecturer.list_all_lecturer)




# print(Lecturer.avg_grade(Lecturer.list_all_lecturer, 'Python'))
print(Student.avg_grade_course(Student.list_all_student, 'Sql'))
print(best_student.avg_grade())