from student import Student
from success import RealSuccess, DesiredSuccess
from data_student import StudentData
from save_data import SaveToJSON

if __name__ == "__main__":
    student = Student("Василенко Василь Васильович", "PD44", "2001-11-11", "Київ")
    
    subjects = ["Математика", "КДС", "Програмування"]
    grades = [90, 100, 60]
    real_success = RealSuccess(subjects, grades)

    desired_success = DesiredSuccess(subjects, [100, 100, 100], 100)

    student_data = StudentData(student, real_success, desired_success)
    data_dict = student_data.to_dict()

    saver = SaveToJSON()
    saver.save(data_dict, "Vasul_PD44.json")

    print("Дані збережено у JSON!")
