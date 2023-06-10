#define and call
def func():
    print("hello this is normal function")
func()

#function with argument
def func(name):
    print("name ", name)
print("function with argument")
func("krishu")
func("Krishika")

#arbitary arguments
def funct(*name):
    print(name[2])
print("fucntion with arbitary arguments")
funct("krishu", "k1", "k2")

#key with value
def func1(name1, name2, name3):
    print("name using key:", name2)
print("function with key value")
func1(name1="k1", name2="k2", name3='3')

#key arbitary variables (**)
def func(**name):
    print("last name using key arbitary:", name["lastname"])
print("key arbitary")
func(firstname  = 'krishika', lastname = 'agarwal')

#default parameters
def func(city = 'Rajkot'):
    print('from', city)
func("Ahmedabad")
print("due to default parameter")
func()


#list arguments
def func(food):
    for i in food:
        print(i)
print("list as argument")
fruits = ['mango', 'apple', 'pear', 'peach']
func(fruits)

#returning value
def square(a):
    return a*a
print("square using return functionm")
print(square(4))

#pass for empty function
def func():
    pass

#recursion
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

x = int(input("enter number for factorial: "))
print (f'factorial of {x} :', factorial(x))

#Tail recursiom (recusrsion func called at the end)
def facto(n, a=1):
    if n == 1:
        return a
    else:
        return facto(n-1, n*a)

print('factorial using tail recursion', facto(6))


