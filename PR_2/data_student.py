class StudentData:
    def __init__(self, student, real_success, desired_success):
        self.student = student
        self.real_success = real_success
        self.desired_success = desired_success

    def to_dict(self):
        return {
            "student": {
                "ПІБ": self.student.get_pib(),
                "Група": self.student.get_group(),
                "Дата народження": self.student.get_birthdate(),
                "Адреса": self.student.get_address()
            },
            "успішність": {
                "Предмети": self.real_success._subjects,
                "Оцінки": self.real_success._grades,
                "Середній бал": self.real_success.average_grade()
            },
            "бажана_успішність": {
                "Предмети": self.desired_success._subjects,
                "Бажані оцінки": self.desired_success._grades,
                "Бажаний середній бал": self.desired_success.average_grade()
            }
        }

