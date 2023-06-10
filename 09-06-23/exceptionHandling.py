#Type Error

x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")


#Raising Exception
try:
	raise NameError("Hi there")
except NameError:
	print ("An exception")
	raise



try:
    print("code start")

    print(1 / 0)

except:
    print("an error occurs")

finally:
    print("Final block")

