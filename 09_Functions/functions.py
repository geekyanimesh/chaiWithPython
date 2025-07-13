import math

# Q1. Square

def squareNum(a):
  return a**2
 
res=squareNum(4)
print(res)

# Q2. Sum

def sumNum(a,b):
  return a+b;

res2=sumNum(2,5)
print(res2)

# Q3. Multiply int and string

def multiply(a,b):
    return a*b

print(multiply(5,3))
print(multiply(5,'def'))

# Q4. area and circumference

def areaCircum(r):
    area=math.pi*r**2
    circum=2*math.pi*r
    return area,circum

print(areaCircum(3))

# Q5. Default value

def greet(name="User"):
    print("Hey! ",name)

greet()
greet("Animesh")

# Q6. Lambda function : cube of a number

cube = lambda x:x**3
print(cube(3))

# Q7. Multiple arguments

def sumAll(*args):
   return sum(args)

print(sumAll(1,2))
print(sumAll(1,2,3,4,5,6))

# Q8. Recursive functions

def fact(num):
   if num==1 or num==0:
      return 1
   else:
    return num*fact(num-1)
 
print(fact(5))