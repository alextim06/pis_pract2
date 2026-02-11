class Lesson():
    def __init__(self, date, auditorium, teacher, lesson_type):
        self.date = date
        self.auditorium = auditorium
        self.teacher = teacher
        self.lesson_type = lesson_type

    def __str__(self):
        return f'Дата: {self.date}, Аудитория: {self.auditorium}, Имя преподавателя: {self.teacher}, Тип: {self.lesson_type}'

class Lecture(Lesson):
    def __init__(self, date, auditorium, teacher, lesson_type, topic, students_count):
        super().__init__(date, auditorium, teacher, lesson_type)
        self.topic = topic
        self.student_count = students_count

    def __str__(self):
        base_str = super().__str__()
        return f'{base_str}, Тема: {self.topic}, Кол-во студентов: {self.student_count}'


class Practice(Lesson):
    def __init__(self, date, auditorium, teacher, lesson_type, task_count):
        super().__init__(date, auditorium, teacher, lesson_type)
        self.task_count = task_count

    def __str__(self):
        base_str = super().__str__()
        return f'{base_str}, Кол-во задач: {self.task_count}'