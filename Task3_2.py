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
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
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



# Создаем студентов
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.grades['Python'] = [10, 10, 10]

student2 = Student('Ivan', 'Ivanov', 'male')
student2.courses_in_progress += ['Python']
student2.grades['Python'] = [8, 7, 9]

# Создаем лекторов
lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Another', 'Person')
lecturer2.courses_attached += ['Python']

# Студенты оценивают лекторов
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

# Сравнение студентов
print("=== Сравнение студентов ===")
print(f"{student1.name} {student1.surname}: средняя оценка = {student1._get_avg_hw_grade():.1f}")
print(f"{student2.name} {student2.surname}: средняя оценка = {student2._get_avg_hw_grade():.1f}")
print(f"{student1.name} > {student2.name}: {student1 > student2}")
print(f"{student1.name} < {student2.name}: {student1 < student2}")
print(f"{student1.name} == {student2.name}: {student1 == student2}")

# Сравнение лекторов
print("\n=== Сравнение лекторов ===")
print(f"{lecturer1.name} {lecturer1.surname}: средняя оценка = {lecturer1._get_avg_lecture_grade():.1f}")
print(f"{lecturer2.name} {lecturer2.surname}: средняя оценка = {lecturer2._get_avg_lecture_grade():.1f}")
print(f"{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")
print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")