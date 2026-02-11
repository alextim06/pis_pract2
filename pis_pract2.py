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

class ManagerLesson():
    def __init__(self):
        self.lessons = []

    def ManageLessons(self):
        with open('date_prac1.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                parts = line.split('"')
                date = parts[0].strip()
                auditorium = parts[1]
                teacher= parts[3]
                lesson_type = parts[5]
                
                if lesson_type == 'Лекция':
                    topic = parts[7]
                    students_count = int(parts[9])
                    lesson = Lecture(date, auditorium, teacher, lesson_type, topic, students_count)
                elif lesson_type == 'Практика':
                    task_count = int(parts[7])
                    lesson = Practice(date, auditorium, teacher, lesson_type, task_count)
                else:
                    lesson = Lesson(date, auditorium, teacher, lesson_type)
                
                self.lessons.append(lesson)
    
    def ShowManage(self):
        for lesson in self.lessons:
            print(lesson.__str__())