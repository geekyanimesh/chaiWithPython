# Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> s = "geekForGeeks"
# >>> s[0]
# 'g'
# >>> s1 = "f";
# >>> s = s[0]+s1
# >>> s
# 'gf'
# >>> temp = "hey! this is a
#   File "<stdin>", line 1
#     temp = "hey! this is a
#            ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> temp = """ hey! this is 
# ... multi lined string """
# >>> temp
# ' hey! this is \nmulti lined string '
# >>> s[-1]
# 'f'
# >>> s[12]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>> temp[: : -1]
# ' gnirts denil itlum\n si siht !yeh '
# >>> temp[3:}
#   File "<stdin>", line 1
#     temp[3:}
#            ^
# SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
# >>> temp[:]
# ' hey! this is \nmulti lined string '
# >>> temp2 = " string to be deleted" 
# >>> temp2
# ' string to be deleted'
# >>> del temp2
# >>> temp2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'temp2' is not defined. Did you mean: 'temp'?
# >>> temp2 = "hello friend"
# >>> temp2 = "there"
# >>> temp2
# 'there'
# >>> temp3  = "hello friend"
# >>> temp4 = "H"  + temp3[1:}
#   File "<stdin>", line 1
#     temp4 = "H"  + temp3[1:}
#                            ^
# SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
# >>> temp4 = "H" + temp3[1:]
# >>> temp4
# 'Hello friend'
# >>> 
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython/04_Strings$ cd ..
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chaiAurPython$ cd ..
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop$ cd ..
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~$ pwd
# /home/animesh-kumar
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~$ ls
# barf          Documents                         node_modules       Postman  snap
# chaiProjects  Downloads                         package.json       Public   Templates
# com.whatsapp  mongodb-compass_1.45.4_amd64.deb  package-lock.json  python   Videos
# Desktop       Music                             Pictures           Raeth
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~$ cd Desktop/
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop$ mkdir
# mkdir: missing operand
# Try 'mkdir --help' for more information.
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop$ mkdir chatBot
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop$ cd cha
# bash: cd: cha: No such file or directory
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop$ cd chatBot/
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chatBot$ git init
# Initialized empty Git repository in /home/animesh-kumar/Desktop/chatBot/.git/
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chatBot$ git clone https://github.com/piyush-eon/mern-chat-app.git
# Cloning into 'mern-chat-app'...
# remote: Enumerating objects: 449, done.
# remote: Counting objects: 100% (236/236), done.
# remote: Compressing objects: 100% (75/75), done.
# remote: Total 449 (delta 182), reused 161 (delta 161), pack-reused 213 (from 1)
# Receiving objects: 100% (449/449), 5.03 MiB | 2.77 MiB/s, done.
# Resolving deltas: 100% (249/249), done.
# animesh-kumar@animesh-kumar-IdeaPad-1-15ADA7:~/Desktop/chatBot$ python3
# Python 3.12.3 (main, Jun 18 2025, 17:59:45) [GCC 13.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> s1 = "hello toBeReplaced"
# >>> s1
# 'hello toBeReplaced'
# >>> s1.replace("toBeReplaced", "replaced")
# 'hello replaced'
# >>> s2 = "done"
# >>> s3 = s1 + s2
# >>> s3
# 'hello toBeReplaceddone'
# >>> s2 = " done"
# >>> s3
# 'hello toBeReplaceddone'
# >>> s3 =  s1 + s2
# >>> s3
# 'hello toBeReplaced done'
# >>> del s2
# >>>  s2
#   File "<stdin>", line 1
#     s2
# IndentationError: unexpected indent
# >>> s2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 's2' is not defined. Did you mean: 's1'?
# >>> len(s3)
# 23
# >>> s3
# 'hello toBeReplaced done'
# >>> s3.upper()
# 'HELLO TOBEREPLACED DONE'
# >>> s3.lower()
# 'hello tobereplaced done'
# >>> tmp = "    hey    "
# >>> temp
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'temp' is not defined. Did you mean: 'tmp'?
# >>> tmp
# '    hey    '
# >>> len(tmp)
# 11
# >>> tmp.strip()
# 'hey'
# >>> len(tmp)
# 11
# >>> tmp = tmp.strip()
# >>> len(tmp)
# 3
# >>> name = "Alice"
# >>> age = 23
# >>> s = ("Name: {name}, Age: {age}")
# >>> s
# 'Name: {name}, Age: {age}'
# >>> s = (f"Name: {name}, Age: {age}")
# >>> s
# 'Name: Alice, Age: 23'
# >>> tmpN = ("My name is {} and I am {} years old".format("Animesh",20))
# >>> tmpN
# 'My name is Animesh and I am 20 years old'
# >>> 

