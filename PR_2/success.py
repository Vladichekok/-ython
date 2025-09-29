from abc import ABC, abstractmethod

class Success(ABC):
    def __init__(self, subjects, grades):
        self._subjects = subjects
        self._grades = grades

    @abstractmethod
    def average_grade(self):
        pass


class RealSuccess(Success):
    def average_grade(self):
        return sum(self._grades) / len(self._grades)


class DesiredSuccess(Success):
    def __init__(self, subjects, grades, desired_average):
        super().__init__(subjects, grades)
        self.__desired_average = desired_average

    def average_grade(self):
        return self.__desired_average 
