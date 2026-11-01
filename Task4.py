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

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_avg_hw_grade(self):
        """Вспомогательный метод для вычисления средней оценки за ДЗ."""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._get_avg_hw_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __eq__(self, other):
        """Сравнение на равенство (по средней оценке за ДЗ)."""
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_hw_grade() == other._get_avg_hw_grade()

    def __lt__(self, other):
        """Сравнение 'меньше' (по средней оценке за ДЗ)."""
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_hw_grade() < other._get_avg_hw_grade()

    def __gt__(self, other):
        """Сравнение 'больше' (по средней оценке за ДЗ)."""
        if not isinstance(other, Student):
            return NotImplemented
        return self._get_avg_hw_grade() > other._get_avg_hw_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}

    def _get_avg_lecture_grade(self):
        """Вспомогательный метод для вычисления средней оценки за лекции."""
        all_grades = []
        for grades_list in self.lectures_grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._get_avg_lecture_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __eq__(self, other):
        """Сравнение на равенство (по средней оценке за лекции)."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_lecture_grade() == other._get_avg_lecture_grade()

    def __lt__(self, other):
        """Сравнение 'меньше' (по средней оценке за лекции)."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_lecture_grade() < other._get_avg_lecture_grade()

    def __gt__(self, other):
        """Сравнение 'больше' (по средней оценке за лекции)."""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._get_avg_lecture_grade() > other._get_avg_lecture_grade()


# --- Функции для подсчета средних оценок ---

def get_avg_hw_grade_for_course(students_list, course_name):
    """
    Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса.

    :param students_list: список объектов класса Student
    :param course_name: название курса
    :return: средняя оценка или сообщение об отсутствии оценок
    """
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])

    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return f"Нет оценок за ДЗ по курсу '{course_name}'"


def get_avg_lecture_grade_for_course(lecturers_list, course_name):
    """
    Подсчет средней оценки за лекции всех лекторов в рамках конкретного курса.

    :param lecturers_list: список объектов класса Lecturer
    :param course_name: название курса
    :return: средняя оценка или сообщение об отсутствии оценок
    """
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.lectures_grades:
            all_grades.extend(lecturer.lectures_grades[course_name])

    if all_grades:
        return sum(all_grades) / len(all_grades)
    else:
        return f"Нет оценок за лекции по курсу '{course_name}'"


# Студенты
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Bash']

student2 = Student('Ivan', 'Ivanov', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git', 'Bash']

# Эксперты
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('John', 'Doe')
reviewer2.courses_attached += ['Python', 'Bash']

# Лекторы
lecturer1 = Lecturer('Alice', 'Smith')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Bob', 'Johnson')
lecturer2.courses_attached += ['Python', 'Bash']


# Эксперты оценивают ДЗ студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 8)

# Студенты оценивают лекторов
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 8)

student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

# --- Вывод информации о всех объектах ---

print("=== Студенты ===")
print(student1)
print()
print(student2)
print()

print("=== Эксперты ===")
print(reviewer1)
print()
print(reviewer2)
print()

print("=== Лекторы ===")
print(lecturer1)
print()
print(lecturer2)
print()


print("=== Сравнение студентов ===")
print(f"{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} < {student2.name}: {student1 < student2}")
print(f"{student1.name} == {student2.name}: {student1 == student2}")
print()

print("=== Сравнение лекторов ===")
print(f"{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")
print()


print("=== Средние оценки по курсам ===")

# Создаем списки объектов
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

# Подсчет средних оценок за ДЗ по курсам
print(f"Средняя оценка за ДЗ по курсу 'Python': {get_avg_hw_grade_for_course(students_list, 'Python'):.1f}")
print(f"Средняя оценка за ДЗ по курсу 'Git': {get_avg_hw_grade_for_course(students_list, 'Git')}")
print(f"Средняя оценка за ДЗ по курсу 'Bash': {get_avg_hw_grade_for_course(students_list, 'Bash')}")
print()

# Подсчет средних оценок за лекции по курсам
print(f"Средняя оценка за лекции по курсу 'Python': {get_avg_lecture_grade_for_course(lecturers_list, 'Python'):.1f}")
print(f"Средняя оценка за лекции по курсу 'Git': {get_avg_lecture_grade_for_course(lecturers_list, 'Git')}")
print(f"Средняя оценка за лекции по курсу 'Bash': {get_avg_lecture_grade_for_course(lecturers_list, 'Bash')}")