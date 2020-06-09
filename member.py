class Member():
    def __init__(self, name="", surname="", age=0, phone=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def surname(self):
        return self.surname

    @surname.setter
    def surname(self, surname):
        self.surname = surname

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, phone):
        self.phone = phone
