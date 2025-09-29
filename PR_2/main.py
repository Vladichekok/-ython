from student import Student
from success import RealSuccess, DesiredSuccess
from data_student import StudentData
from save_data import SaveToJSON

if __name__ == "__main__":
    # 1. створюємо студента
    student = Student("Василенко Василь Васильович", "PD44", "2001-11-11", "Київ")

    # 2. реальна успішність
    subjects = ["Математика", "КДС", "Програмування"]
    grades = [90, 100, 60]
    real_success = RealSuccess(subjects, grades)

    # 3. бажана успішність
    desired_success = DesiredSuccess(subjects, [100, 100, 100], 100)

    # 4. формуємо дані
    student_data = StudentData(student, real_success, desired_success)
    data_dict = student_data.to_dict()

    # 5. збереження у файл
    saver = SaveToJSON()
    saver.save(data_dict, "Vasul_PD44.json")

    print("Дані збережено у JSON!")
