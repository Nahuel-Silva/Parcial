class Book():
    def __init__(self, name="", authorName="", memberLegajo=""):
        self.name = name
        self.authorName = authorName
        self.memberLegajo = memberLegajo

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def authorName(self):
        return self.authorName

    @authorName.setter
    def authorName(self, authorName):
        self.authorName = authorName

    @property
    def memberLegajo(self):
        return self.memberLegajo

    @memberLegajo.setter
    def memberLegajo(self, memberLegajo):
        self.memberLegajo = memberLegajo
