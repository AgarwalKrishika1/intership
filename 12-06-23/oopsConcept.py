class Person:
    def __init__(self, name):
        self.name = name

    def method1(self):
        print("Hi, my name is ", self.name)


p = Person('Krishika')
p.method1()

print("\n")
print("scope test:")
#scope
#Global(globally)      Non-local(in scope)        Local(to instant)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

print('\n\n')


class Dog:
    #defining here creates only 1 instance
    trick = []

    def __init__(self, name):
        self.name = name
        #this creates instatnce for each call
        self.trick = []

    def add_trick(self, trick):
        self.trick.append(trick)


d = Dog('abc')
e = Dog('def')
d.add_trick('pull')
e.add_trick('push')
print(d.trick)
print(e.trick)

print('\n\n')
#same instance with different values


class A:
    purpose = 'learn'
    language = 'python'


a1 = A()
print(a1.purpose,  a1.language)
a2 = A()
a2.language = 'Java'
print(a2.purpose,  a2.language)

print('\n\n')


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,  self.lastname)


print("using parent class")
x = Person('Krishika', 'Agarwal')
x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        print(self.firstname, self.lastname, 'graduation year', self.graduationyear)


print("using student class")
y = Student('Student', 'abc', 2025)
y.printname()

print('\n\n', 'iterators')


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 4:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

print("\n\n", 'polymorphism')


class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")


class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

print('\n\n Encapsulation(private variables)')
#to create private variable use __ in variable name


class Base:
	def __init__(self):
		self.a = "variable"
		self.__c = "private variables"


class Derived(Base):
	def __init__(self):

		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


obj1 = Base()
print('normal variable prints')
print(obj1.a)
#can't use this as can't call private variables
#print(obj1.c)

#error as derived class called private variable
# not defined in derived class
#obj2 = Derived()
#print(obj2.c)

print('\n access private variable')


class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 10

# Driver code


myObject = MyClass()
print(myObject._MyClass__hiddenVariable)

#functions
print('\n')


class Calculation1:
    def summation(self, a, b):
        return a+b


class Calculation2:
    def multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b


d = Derived()
print(isinstance(d, Derived))
