def add(a,b):
    return a+b


def add(a,b,c):
    return a+b+c

def add(a,b,c,d):
    return a+b+c+d


# print(add(10,3,4))

#function overloading
# we cannot have explicit return statement in the __init__method by default it will return none
# we can create the any number of __init__ method inside a single class but the returns will  be from the latest fun def __init pointing to the func object

class demo:
    def __init__(self,a,b): #here the __init__is pointing to the  function objects with 2 arguments
        self.a = a
        self.b = b

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


class point:
    def __init__(self,a=0,b=0,c=0,d=0):   #now the __init__ with a variable name which pointing to the latest function defined
        self.a = a
        self.b = b
        self.c = c
        self.d = d

     # here we wont get any exception when created multiple __init method follows latest for output

# p1 = point()
# p2 = point(1,2)
# p3 = point(1,2,3)
# p4 = point(1,2,3,4,)
# print(p4.__class__)
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
# print(p4.__dict__)
# print(p4.__init__)
# print(point.__dict__)
#
#
#2. what is callable
#  when function call operator infront of th object which is called callable
# any object if it has defined __call__ method then it is callable

#function call operator
def add(a,b):
    return a+b

# print(add(1,2))
# print(dir(add))
# a= 10
# print(a())
# dir(a)   # theres no __call method where we cant call an integer object

dir(point)


# class greeting:
#     def __init__(self, name):
#         self.name = nmae



#     def __call__(self):
#     return f"hello {self.name}"
#
#
# class greeting:
#     def __call__(self, name):



class squares:
    def __call__(self, numbers):
        return [numbers ** 2 for numbers in numbers]


#


class even:
    def __call__(self, numbers):
        return [numbers ** 2 for numbers in numbers]

    def





