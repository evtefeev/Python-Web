from models import Student, Session, ExamResult


def add_student(name: str, university: str, specialty: str, group: str):
    with Session() as session:
        new_student = Student(
            name=name,
            university=university,
            specialty=specialty,
            group=group
        )
        session.add(new_student)
        session.commit()

# add_student("Олег", "Львівська політехніка", "Комп'ютерні науки", "КН-23")

# add_student()


def add_exam_result():
    with Session() as session:
        new_result = ExamResult(
            student_id=2,
            subject="Python Web",
            grade=97,
            passing_grade=60,
            passed=True,
        )
        session.add(new_result)
        session.commit()


add_exam_result()


def get_all_students():
    with Session() as session:
        students = session.query(
            Student
        ).all()  # Взяття усієї інформації з таблиці студентів
        for student in students:
            print(
                f"ID: {student.id}, Ім'я: {student.name}, Університет: {student.university}, Спеціальність: {student.specialty}, Група: {student.group}"
            )
            print("Результати екзаменів:")
            if student.exams:
                for exam in student.exams:
                    print(
                        f"Предмет: {exam.subject}, Оцінка: {exam.grade}, Пройшов: {exam.passed}"
                    )
            else:
                print("  Немає оцінок")

# get_all_students()

def update_exam_grade(id, grade):
    with Session() as session:
        exam = session.query(ExamResult).filter_by(id=id).first()

        exam.grade = grade
        session.commit()


update_exam_grade(1, 95)


def delete_grades():
    with Session() as session:
        student = session.query(ExamResult).filter_by(id=1).first()

        session.delete(student)
        session.commit()
