sqr = lambda x: x * x
print('square root of 5  ', sqr(5))
print('\n swap numbers')
# to swap two numbers a and b
a, b = 5, 7
a, b = b, a
print('a', a, '\t b', b)
print('\n print even numbers ')
evenNumbers = [x for x in range(11) if x % 2 == 0]
print(evenNumbers)
print('\n pass fucntion')
m = []
if m in [1, 2, 3]:
    pass
print('\n reverse string')
lis = [1, 2, 3]
lis.reverse()
print(lis)
print('\n pyramid')
n = 5
# one liner code for half pyramid pattern
print('\n'.join('* ' * i for i in range(1, n + 1)))
print('\n walrus example')
# walrus define variable in between of function
review = "good"
if (n := len(review)) < 10:
    print("Minimum 10 characters required")
print('\n nested loops')
x, y = [1, 2, 3], [4, 5, 6]
coordinates = [(xcor, ycor) for xcor in x for ycor in y]
print(coordinates)
print('\n printing all values')
nums = [1, 2, 3]
print(*nums)
print('\n variable name using fstring')
number1 = 5
number2 = 7
print(f"{number1=} {number2=}")
print("\n FizzBuzz")
print(['FizzBuzz' if i % 3 == 0 and i % 5 == 0
	   else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 20)])
