# class Book:
#     def __init__(self,pages):
#         self.pages = pages
# b1 = Book(100)
# print(b1.pages)
# b1.pages = 200
# print(b1.pages)
# b1.pages = -99
# print(b1.pages)

# class student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#
# s1 = student("chandu",22)
# print(s1.age)
# print(s1.__name)


class student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def setter(self,age,name):
        if age > 18 and name =="chandu":
            self.__age = age
            self.__name = name

    def getter(self):
        return self.__age,self.__name

s1 = student("chaya",23)
res = s1.getter()
for i in res:
    print(i)
s1.setter(22,"chanu")
res1 = s1.getter()
print(res1)


# normal Encapsulation

class Student:
    def __init__(self):
        self.__name = ""

    def setter(self,val):
        self.__name = val

    def getter(self):
        return self.__name
s1 = Student()
s1.setter("chandu")
res = s1.getter()
print(res)

#property function in Encapsulation

class student:
    def __init__(self):
        self.__name = ""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name = val
    gs = property(getter,setter)

s1 = student()
s1.gs = "Nayana"
res = s1.gs
print(res)


# @Decorator property function in Encapsulation

class Student:
    def __init__(self):
        self.__age = 0

    @property
    def data(self):
        return self.__age


    @data.setter
    def data(self,val):
        self.__age = val



s2 = Student()
s2.data_val = 9
res = s2.data
print(res)


#public method into private method

class dog:
    def __init__(self):
        self.__bread = "husky"
    def __bark(self):
        print(self.__bread)
        print("husky is barking")

    def helper(self):

        self.__bark()


d1 = dog()
d1.helper()
