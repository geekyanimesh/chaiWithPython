import math

# Q. Count positive numbers

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# count = 0
# for i in numbers:
#     if i>0:
#         count+=1

# print(count)

# Q. Sum of even numbers

# limit = 12
# sum=0

# for i in range(1,limit+1):
#     if i%2==0:
#         sum+=i

# print(sum)

# Q. Skip a number and write the table

# num = 5
# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(num, "*", i,"=" ,num*i)

# Q. Reverse a string

# str = "toBeReversed"
# revstr=""
# for i in range(len(str)-1,-1,-1):
#     revstr+=str[i]

#aliter

# revstr1=""
# for i in str:
#     revstr1=i+revstr1

# print(revstr)
# print(revstr1)

# Q. First non repeating character

# str3="teeter"

# for char in str3:
#     if(str3.count(char)==1):
#         result=char
#         break

# print(result)

# Q. Find factorial using while loop

# num = 5
# fact=1
# while num>0:
#     fact*=num
#     num-=1

# print(fact)

# Q. Keep checking until condition hits

# state = True
# while state:
#     num = int(input("Enter number between 1 to 10: "))
#     if num<11 and num>0:
#         state=False

# print(num)

# Q. Prime number check

# num = 12
# limit = int(math.sqrt(num))
# for i in range(2,limit):
#     if num%i==0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

# Q. Duplicate in list

# l1 = ["apple","banana","apple","grapes"]

# for i in range(len(l1)):
#     isUnique=True
#     for j in range(len(l1)):
#         if i!=j and l1[i]==l1[j]:
#             isUnique=False
#             print("Duplicate found!")
#             break
#     if isUnique==False:
#         break

