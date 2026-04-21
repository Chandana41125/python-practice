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
