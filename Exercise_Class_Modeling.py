#Exeercise Class Modeling

class Animal:

    """Animal"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Getting Name")
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Setting Name")
        self.__name = new_name

    def move(self):
        print('Moving')




class Book:

    """Book"""

    def __init__(self, author):
        self.__author = author

    @property
    def author(self):
        print("Getting Author")
        return self.__author

    @author.setter
    def name(self, new_author):
        print("Setting author")
        self.__name = new_author

    def move(self):
        print('Moving')


class Vehicle:

    """Vehicle"""

    def __init__(self, model):
        self.__author = model

    @property
    def model(self):
        print("Getting Model")
        return self.__author

    @Model.setter
    def name(self, new_Model):
        print("Setting Model")
        self.__name = new_Model

    def move(self):
        print('Moving')
