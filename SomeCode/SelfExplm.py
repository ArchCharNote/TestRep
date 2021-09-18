
f = lambda x: x+3
g = (lambda a,b: a(b) * a(b*2))(f, 7)

# print(f(7))
# print(f(7*2))
print(g)


class MyClass:

    def say(self):
        print(self)


MyClass.say('нечто')
# my_1 = MyClass()  # Создаём объект класса.
# my_1.say()  # <__main__.MyClass instance at 0x7f8e8c6383f8>

class MyClassys():
    i = 123

    def __init__(self):
        self.i = 345


a = MyClassys()
print("a.i = ",a.i)
print("MyClass.i = ",MyClassys.i)


class Rectangle:
    default_color = "green"
    def __init__(self, width, height):
        self.width = width
        self.height = height

print(Rectangle.default_color)
rect = Rectangle(10, 20)
print(rect.width)
print(rect.height)
rect = Rectangle(11, 21)
print(rect.width)
print(rect.height)

class Human:
    def __init__(self):
        self.blood = 7000


    def add_blood(self, volume):
        self.blood += volume

xxx = Human()
xxx.add_blood(2000)
xxx.r = 12
xxx.o = 12
print(xxx.blood)
Human.add_blood(xxx,1000)
print(xxx.blood)
Human.add_blood(xxx,2000)
print(xxx.blood)
xxx.add_blood(2000)
print(xxx.blood)
print(xxx.r)
print(xxx.__dict__)
# Human.blood

# for att in dir(xxx):
#     print (att, getattr(xxx,att))

class Point:
    pass