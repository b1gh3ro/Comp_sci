#1



#2

# firstNum = int(input("Enter First Number: "))
# secondNum = int(input("Enter Second Number: "))

# if firstNum > secondNum:
#     print(f"{firstNum} is greater")
# else:
#     print(f"{secondNum} is greater")




#3

# firstNum = int(input("Enter First Number: "))
# secondNum = int(input("Enter Second Number: "))
# thirdNum = int(input("Enter Third Number: "))


# if firstNum > secondNum > thirdNum:
#     print(f"{firstNum} is greater")
# if secondNum > firstNum > thirdNum :
#     print(f"{secondNum} is greater")
# else:
#     print(f"{thirdNum} is greater")



#4

# for i in range(0, 6):
#     for j in range(0,i):
#         print("*", end="")
#     print()

# print()

#OR

# for i in range(5,0, -1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()



#5

# x = int(input("Enter Number x: "))
# n = int(input("Enter Power n: "))
# print(f"x^n = {x**n}")


#6

# x = int(input("Enter Number x: "))
# n = int(input("Enter Number n: "))

# sum = 0

# for i in range(0, n+1):
#     print(f"{x**i} x = {x} n = {i}")
#     sum += x**i
#     print(sum)
# print(sum)

#OR

# x = int(input("Enter Number x: "))
# n = int(input("Enter Number n: "))

# sum = 0

# for i  in range(0,n+1):
#     if i%2 == 0:
#         sum += x**i
#     else:
#         sum -= x**i
#     print(f"{x}^{i} , sum = {sum}")
# print(sum)


#7

# num = int(input("Enter Number To Check: "))
# factorsAdded = 0
 
# for i in range(1, num):
#     if num%i == 0 :
#         factorsAdded += i
# print(f"{num} = {factorsAdded}")

# sum = 0
# singleDigits = 0
# temp = num
# while temp > 0:
#     singleDigits = temp % 10
#     temp = temp // 10
#     sum += singleDigits**3
# print(sum)

# if num == factorsAdded:
#     print("perfect number!")
# if num == sum:
#     print("armstrong!")
# if str(num) == str(num)[::-1]:
#     print("pallindrome!")



#8

# num = int(input("Enter Number: "))
# prime = True
# for i in range(2, num+1):
#     for j in range(2, num+1):
#         if i*j == num:
#             prime = False  
# if prime:
#     print("prime!")
# else:
#     print("not a prime!")



#9

# num = int(input("Enter number of terms in fibinocci series: "))
# first = 0
# second = 1
# third = None
# for i in range(num):
#     if i == 0:
#         print(0, end = ' ')
#     elif i == 1:
#         print(1, end = ' ')
#     else:
#         third = first + second
#         print(third, end = ' ')
#         first = second
#         second = third



#10

# numOne = int(input("Enter First Num: "))
# numTwo = int(input("Enter Second Num: "))
# commonFactors = [1]
# factorsOfOne = [1,numOne]
# factorsOfTwo = [1, numTwo]
# for i in range(numOne+1):
#     for j in range(numTwo+1):
#         if i*j == numOne:
#             factorsOfOne.append(i)
# for i in range(numTwo+1):
#     for j in range(numOne+1):
#         if i*j == numTwo:
#             factorsOfTwo.append(i)
# for i in factorsOfOne:
#     if i in factorsOfTwo:
#         commonFactors.append(i)

# hcf = max(commonFactors)
# lcm = (numOne*numTwo)/hcf
# print(f"hcf = {hcf}")
# print(f"lcm = {lcm}")



#11

# input = input("Enter a sentence, word: ")

# vowels = 0
# consonants = 0
# uppercase = 0
# lowercase = 0
# for i in input:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         vowels += 1
#     else:
#         consonants += 1
    
#     if i.isupper():
#         uppercase += 1
#     if i.islower():
#         lowercase += 1

# print(f"uppercase: {uppercase} lowercase: {lowercase} vowels: {vowels} consonants: {consonants}")



#12

# str = input("Enter a string: ")
# if str[::-1] == str:
#     print("This is a palladrome!")
# else:
#     print("This is not a pallandrome!")



#13

# lst = [1, 2, 3, 432 ,342 ,32423 ,32, 543 ,23,  534 ,2123 , 432]
# print(f"largest number in list {max(lst)}")
# print(f"smallest number in a list {min(lst)}")


#14

# listNum = int(input("enter number of elements in list: "))

# Array = []

# for i in range(0, listNum):
#     listEle = int(input("enter elements: "))
#     Array.append(listEle)

# for i in range(0,listNum,2):
#     Array[i],Array[i+1]=Array[i+1],Array[i]

# print("List after swapping :",Array)



#15

# listNum = int(input("enter number of elements in list: "))
# Array = []

# for i in range(0, listNum):
#     listEle = input("enter elements: ")
#     Array.append(listEle)

# element = input("enter what to search for: ")
# for i in range(0, listNum):
#     if element == Array[i]:
#         print(f"element found at index ${i}")



#16

# listNum = int(input("enter number of elements in list: "))
# Array = []
# for i in range(0, listNum):
#     listEle = int(input("enter elements: "))
#     Array.append(listEle)

# for i in Array:
#     digits = 0
#     sum = 0
#     temp = i
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#     if sum == i:
#         print(f"{i} is a perect number!")
# print(f"largest num is {max(Array)}")
# print(f"smallest num is {min(Array)}")



#17

# dict = {"Never":(1, 89), "Gonna": (2, 45), "Give": (3, 90), "You": (4, 78)}

# for i in dict:
#     if dict[i][1] >= 75:
#         print(f"{i} got more than 75")
