class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
