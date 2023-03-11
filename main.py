class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer)  and grade >= 1 and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # def add_courses(self, course_name):
    #     self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']

coll_reviewer = Reviewer('Vasya','Sokolov')
coll_reviewer.courses_attached += ['Python']
#
cool_lecturer = Lecturer('Vova','Ivanov')
cool_lecturer.courses_attached += ['Python']

# best_student.rate_lecturer(cool_lecturer, 'Python', 10)
coll_reviewer.rate_hw(best_student, 'Python', 10)
coll_reviewer.rate_hw(best_student, 'Python', 15)
best_student.rate_lecturer(cool_lecturer,'Python',9)
print(best_student.grades)
print(cool_lecturer.grades)

