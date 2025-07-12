

animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAur
animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython$ ls
01_Intro  02_dataTypes
animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython$ cd 02_dataTypes/
animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython/02_dataTypes$ ls
dataType.md
animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython/02_dataTypes$ python3
Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> random.choice(2,1,4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Random.choice() takes 2 positional arguments but 4 were given
>>> random.choice([1,2,3,4,5])
2
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> username = "chai"
>>> len(username)
4
>>> username[0]
'c'
>>> username[0]= 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> dir(username_)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'username_' is not defined. Did you mean: 'username'?
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> capitalize(username)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'capitalize' is not defined
>>> myList = [123, "animesh", 3.14]
>>> myList
[123, 'animesh', 3.14]
>>> len(myList)
3
>>> myD = {1:"rose" , 2:"lily", 3:"lotus"}
>>> myD[2]
'lily'
>>> myD["lily"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'lily'
>>> myD['lily']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'lily'
>>> my[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my' is not defined. Did you mean: 'myD'?
>>> myD[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> myTuple = (12, "chai", 3.14)
>>> myTup[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myTup' is not defined. Did you mean: 'myTuple'?
>>> myTuple[0]
12
>>> 