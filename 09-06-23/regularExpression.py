import re
text = "Hello I am Krishika Agarwal"
print("find all", re.findall("a",text))
print("find all", re.findall("bcd",text))
print("white space")
print(re.search("\s", text).start())
print("split", re.split("\s",text))
print("split only at 1st ", re.split("\s",text,1))
print("replace with number of times want to be replaced", re.sub("\s", "9", text,2))
print("find all", re.findall("[a-i]", text))
print("all", re.findall("He.o", text))
print("start", re.findall("^Hello", text))
print("end", re.findall("a$", text))
print("zero or more occurence", re.findall("He.*o",text))
print("zero or one occurence", re.findall("He.?o",text))
print("one or more occurence", re.findall("He.*o",text))
print("specific occurence", re.findall("He{3}o",text))
print("either or", re.findall("hello|Hello", text))

