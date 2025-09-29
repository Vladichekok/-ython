class Student:
    def __init__(self, pib, group, birthdate=None, address=None):
        self.__pib = pib
        self.__group = group
        self.__birthdate = birthdate
        self.__address = address

    def get_pib(self):
        return self.__pib

    def set_pib(self, pib):
        self.__pib = pib

    def get_group(self):
        return self.__group

    def set_group(self, group):
        self.__group = group

    def get_birthdate(self):
        return self.__birthdate

    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
