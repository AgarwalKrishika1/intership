# Strings
print("String")
a = '''You will do this
Believe in yourself , You can do it'''
print(a)
print(a[:2])
print('length ', len(a))
print('using lopp ')
for i in 'krishu':
    print(i)
print('check for string')
print('You'  in a)
print('Hi' not in a)
print('SLICING')
print('for range', a[2:8])
print('from start', a[:9])
print('till end', a[45:])
print('negative index', a[-3:-9])

print("methods")
print('upper', a.upper())
print('lower', a.lower())
print('strip remove white space', a.strip())
print('replace', a.replace("Y", 'y'))
print('split', a.split(' '))
a = 'hii'
b = 'krishu'
c = a + "  " + b
print('concate\n', c)
print('capitalise', a.capitalize())
print('string to lower', a.casefold())
print('number of time', a.count(i))
print('center', a.center(12))
print('encode', a.encode())
print('ends', a.endswith('h'))
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.isdecimal())
print(a.isidentifier())
print(a.islower())
print(a.isprintable())
print(a.isnumeric())
print(a.isspace())
print(a.istitle())
print(a.isupper())
#print(a.maketrans())
print(a.swapcase())
print(a.title())
#print(a.translate())
#print(a.zfill())
print('Format ')
age = 21
name = 'krishika'
passmark = 90.9
text = 'hi my age is {1} and name is {2} with marks {0}'
print(text.format(age, name, passmark))

text = 'hi \"Krishika\"'
print(text)
print('special characters')
print('single quote \'oh\'')
print('black slash \\oh\\')
print('new line \n oh')
print('tab \t oh')
print('carraige \r oh')
print('backspace \b ohh')

