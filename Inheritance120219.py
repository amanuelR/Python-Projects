class Boat:
    def __init__(self):  #self is a refference to the current object
        self.__builder = ""
        self.__year = 1900
    def __init__(self,builder,yr):
        self.__builder = builder #__ hides the attributes
        self.__year = yr
    def set_type(self,ty):
        self.__builder = ty
    def set_yesr(self,yr):
        self.__year = yr
    def get_type(self):
        return self__builder
    def get_yesr(self):
        return self.__year
    def __str__(self):
        return "Builder: " + self.__builder + "\nYear: " + str(self.__year)
class Vessel(Boat):
    def __init__(self,builder = "U.S.A",year = 2019):
        Boat.__init__(self,builder,year)
        self.__builder = builder
        self.__year = year
    def _str__(self):
        return Boat.__str__(self)
