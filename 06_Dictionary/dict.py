# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython/06_Dictionary$ python3
# Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> chai_type = {"Masala":"Spicy", "Gold":1,true:"Honesty"}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> chai_type = {"Masala":"Spicy", "Gold":1 , True:"Hone
# sty"}
# >>> chai_type
# {'Masala': 'Spicy', 'Gold': 1, True: 'Honesty'}
# >>> chai_type[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 0
# >>> chai_type['Gold']
# 1
# >>> chai_type['Masala']
# 'Spicy'
# >>> chai_type.get(True)
# 'Honesty'
# >>> chai_type.get('Honesty')
# >>> for chai in chai_type:
# ...     print(chai)
# ... 
# Masala
# Gold
# True
# >>> for i in chai
#   File "<stdin>", line 1
#     for i in chai
#                  ^
# SyntaxError: expected ':'
# >>> for i in chai:
# ...     print(chai, chai[i])
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'bool' object is not iterable
# >>> for i in chai_type:
# ...     print(chai_type, chai_type[i])
# ... 
# {'Masala': 'Spicy', 'Gold': 1, True: 'Honesty'} Spicy
# {'Masala': 'Spicy', 'Gold': 1, True: 'Honesty'} 1
# {'Masala': 'Spicy', 'Gold': 1, True: 'Honesty'} Honesty
# >>> 
#  *  History restored 

# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython/06_Dictionary$ 
#  *  History restored 

# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython/06_Dictionary$ python3
# Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> dict1 = ["Animesh":6,"Kumar":7,"raju":12]
#   File "<stdin>", line 1
#     dict1 = ["Animesh":6,"Kumar":7,"raju":12]
#                       ^
# SyntaxError: invalid syntax
# >>> dict1 = ['Animesh':6,"Kumar":7,"raju":12]
#   File "<stdin>", line 1
#     dict1 = ['Animesh':6,"Kumar":7,"raju":12]
#                       ^
# SyntaxError: invalid syntax
# >>> dict1 =  {"Animesh" : 6, "Kumar" : 12, "Raju" : 34}
# >>> for i in dict1:
# ...     print(i)
# ... 
# Animesh
# Kumar
# Raju
# >>> for i, ele in dict1:
# ...     print(ele)
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 2)
# >>> for i in dict1:
# ...     print(dict1[i])
# ... 
# 6
# 12
# 34
# >>> for  i in dict1:
# ...     print(i,dict1[i])
# ... 
# Animesh 6
# Kumar 12
# Raju 34
# >>> for key,values in dict1.items():
# ...     print(key, values)
# ... 
# Animesh 6
# Kumar 12
# Raju 34
# >>> if "Animesh" in dict1:
# ...     print("Yayy")
# ... 
# Yayy
# >>> print(len(dict1))
# 3
# >>> dict1["Ram"]=27
# >>> dict1
# {'Animesh': 6, 'Kumar': 12, 'Raju': 34, 'Ram': 27}
# >>> dict1.pop("Kumar")
# 12
# >>> dict1
# {'Animesh': 6, 'Raju': 34, 'Ram': 27}
# >>> dict1.popitems()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
# >>> dict1.popitem()
# ('Ram', 27)
# >>> dict1
# {'Animesh': 6, 'Raju': 34}
# >>> square_num  = {x=x**2 for i in range(10)}
#   File "<stdin>", line 1
#     square_num  = {x=x**2 for i in range(10)}
#                    ^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# >>> dict2 = {x:x**2 for i in range(7)}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'x' is not defined
# >>> dict2 = {x:x**2 for x in range(7)}
# >>> dict2
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# >>> 