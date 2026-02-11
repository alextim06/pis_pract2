class Lesson():
    def __init__(self, date, auditorium, teacher, ):
        self.date = date
        self.auditorium = auditorium
        self.teacher = teacher

    def __str__(self):
        return f'Дата: {self.date}, Аудитория: {self.auditorium}, Имя преподавателя: {self.teacher}'

lessons = []
with open('date_prac1.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        parts = line.split('"')

        lesson = Lesson(
        date=parts[0].strip(),
        auditorium=parts[1],
        teacher=parts[3],
        )

        lessons.append(lesson)

for i in lessons:
    print(i)



