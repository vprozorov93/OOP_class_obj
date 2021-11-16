from functools import reduce


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if isinstance(other, Student) and self._avg_rate() < other._avg_rate():
            return True
        elif isinstance(other, Student) and self._avg_rate() > other._avg_rate():
            return False
        return "Ошибка"

    def __gt__(self, other):
        if isinstance(other, Student) and self._avg_rate() > other._avg_rate():
            return True
        elif isinstance(other, Student) and self._avg_rate() < other._avg_rate():
            return False
        return "Ошибка"

    def rate_lec(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and
                course in lector.courses_attached and
                (course in self.finished_courses or course in self.courses_in_progress) and
                grade in range(1, 11)):
            if course in lector.grades_for_lec:
                lector.grades_for_lec[course] += [grade]
            else:
                lector.grades_for_lec[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_rate(self):
        if len(self.grades) == 0:
            return 0
        i = 0
        sum_ = 0

        for ix, el in self.grades.items():
            i += len(el)
            sum_ += sum(el)

        return round(sum_ / i, 2)

    def _course_in_list_to_str(self, list_):
        if len(list_) == 0:
            return 0
        return ' '.join(list_)

    def __str__(self):
        res = f"""
    Имя: {self.name}
    Фамилия: {self.surname}
    Средняя оценка за домашние задания: {self._avg_rate()}
    Курсы в процессе изучения: {self._course_in_list_to_str(self.courses_in_progress)}
    Завершенные курсы: {self._course_in_list_to_str(self.finished_courses)}
    """
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course):
        self.courses_attached.append(course)

    def __str__(self):
        return f"""
    Имя: {self.name}
    Фамилия: {self.surname}
    """


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lec = {}

    def __lt__(self, other):
        if isinstance(other, Lecturer) and self._avg_rate() < other._avg_rate():
            return True
        elif isinstance(other, Lecturer) and self._avg_rate() > other._avg_rate():
            return False
        return "Ошибка"

    def __gt__(self, other):
        if isinstance(other, Lecturer) and self._avg_rate() > other._avg_rate():
            return True
        elif isinstance(other, Lecturer) and self._avg_rate() < other._avg_rate():
            return False
        return "Ошибка"

    def _avg_rate(self):
        if len(self.grades_for_lec) == 0:
            return 0
        i = 0
        sum_ = 0

        for ix, el in self.grades_for_lec.items():
            i += len(el)
            sum_ += sum(el)

        return round(sum_ / i, 2)

    def __str__(self):
        return super().__str__() + f"Средняя оценка за лекции: {self._avg_rate()}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avg_for_students(students, course):
    if (isinstance(course, str) and
            reduce(lambda x, y: x * y, [isinstance(student, Student) for student in students]) != 0):
        sum_ = 0
        i = 0
        for student in students:
            if student.grades.get(course) is not None:
                sum_ += sum(student.grades.get(course))
                i += len(student.grades.get(course))
        return round(sum_ / i, 2)
    print('Не верный тип аргумента students или course')


def avg_for_lectors(lectors, course):
    if (isinstance(course, str) and
            reduce(lambda x, y: x * y, [isinstance(lector, Lecturer) for lector in lectors]) != 0):
        sum_ = 0
        i = 0
        for lector in lectors:
            if lector.grades_for_lec.get(course) is not None:
                sum_ += sum(lector.grades_for_lec.get(course))
                i += len(lector.grades_for_lec.get(course))
        return round(sum_ / i, 2)
    print('Не верный тип аргумента lectors или course')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('A', 'B', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student2.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
cool_mentor2 = Reviewer('Any', 'Buddy')
cool_mentor2.courses_attached += ['Python']

cool_lec = Lecturer('Vasya', 'Pupkin')
cool_lec.add_course('Python')
cool_lec.add_course('Git')
cool_lec2 = Lecturer('Petya', 'Vas\'kin')
cool_lec2.add_course('Python')
cool_lec2.add_course('Git')

cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Git', 2)
cool_mentor.rate_hw(best_student, 'Git', 4)

best_student.rate_lec(cool_lec, 'Python', 5)
best_student.rate_lec(cool_lec, 'Python', 2)
best_student.rate_lec(cool_lec, 'Python', 5)
best_student2.rate_lec(cool_lec2, 'Python', 5)
best_student2.rate_lec(cool_lec2, 'Python', 5)
best_student2.rate_lec(cool_lec2, 'Python', 5)

best_student.rate_lec(cool_lec, 'Git', 2)
best_student.rate_lec(cool_lec, 'Git', 2)
best_student.rate_lec(cool_lec, 'Git', 2)
best_student2.rate_lec(cool_lec2, 'Git', 2)
best_student2.rate_lec(cool_lec2, 'Git', 2)
best_student2.rate_lec(cool_lec2, 'Git', 2)

print("Студенты:")
print(best_student)
print(best_student2)
print(best_student < best_student2)
print(best_student > best_student2)

print("Ревьюверы:")
print(cool_mentor)
print(cool_mentor2)

print("Лекторы:")
print(cool_lec)
print(cool_lec2)
print(cool_lec > cool_lec2)
print(cool_lec < cool_lec2)

print("Средний балл по Git у студентов:")
print(avg_for_students([best_student, best_student2], 'Git'))
print("Средняя оценка по Py у преподов:")
print(avg_for_lectors([cool_lec, cool_lec2], 'Python'))


# # print(dir(str))
#
# class Person:
#     # name = '' # все заначения класса можно инициализировать в методе init, тогда данные значения будут инициализироваться
#     # power = 0 # в момент создания объекта класса, а не при его объявлении в программе
#     # energy = 100
#     # hands = 2
#     # backpack = [] # значение инициализируется присоздании класса, а изменяемые типы ссылаются на один и тот же объект
#     #               в памяти, то есть они будут общими у экземпляра класса. Поэтому не нужно делать изменяемые типы
#     #               значением по умолчанию для аругментов. Аргумент backpack как раз укладывается в это описание.
#
#     # Аргумент методов (функций класса) self ссылается на кокретный экземпляр класса (который еще не создан)
#     # Его обязательно нужно указывать, что бы показывать то,
#     # что все действия выполняемые методом выполняются именно с тем объектом, для которого вызывается метод
#     def __init__(self, name, power, energy=100, hands=2): # инициализатор объекта класса
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = [] # в данном случае создается атрибут рюкзак уже для конкретного объекта класса
#     #                           и не будет являться атрибутом самого класса по умолчанию
#         self.hands = hands
#
#     def eat(self, food):
#         if self.energy <100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):
#         # print(self.alias)
#         self.alias = new_alias
#         print(self.alias)
#
#     # в методы класса можно передавать объекты класса и с ними работать
#     def beat_up(self, foe):
#         if not isinstance(foe, Person): # проверка на то, что foe является объектом класса Person
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
#
# # peter = Person() # такая инициализация испольщуется, когда нет метода __init__ у класса
# # peter.name = "Peter Parker"
# # peter.power = 70
# # peter.alias = 'Spider-Man' # можно добавлять атрибуты, которые не описаны в классе, для конкретного объекта этого класса
# # # print(peter.__dict__) # покажет атрибуты объекта, которые отличаются от атрибутов класса
# # # print(Person.__dict__) # покажет все атрибуты присущие классу
# # # print(type(peter))
#
# # bruce = Person()
# # bruce.name = "Bruce Wayne"
# # bruce.power =85
# # # bruce.alias = 'Batman'
# #
# # bruce.change_alias('Robin')
#
# peter = Person('Peter Parker', 70) # такая инициализация используется, в случае если у класса присутствует метод  __init__
# bruce = Person('Bruce Wayne', 85)
