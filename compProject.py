
# def largestAndSmallest():

#     print(" Largest and Smallest finder")
#     numInt = int(input('enter the number of numbers in the list: '))

#     lst = []

#     for i in range(0,numInt):
#         left = numInt-i
#         num = int(input(f'enter {left} number of digits: '))
#         lst.append(num)
#     lst.sort()
#     print(f'your list is: {lst}')
#     print(f'largest num is {lst[-1]}')
#     print(f'smallest num is {lst[0]}')



# def rickRoll():
#     print("palindrome Finder")
#     str = input("Enter a string: ")
#     if str[::-1] == str:
#         print("This is a palindrome!")
#     else:
#         print("This is not a palindrome!")
    




# def main():
#     print("**** Main Menu ****")
#     print("1. largest and smallest numbers in a list")
#     print("2. Palindrome Finder")
    
#     print("type quit() to exit")

#     Choice = input("choose: ")

#     if(Choice == "1" ):
#         print("\n"*30  )
#         largestAndSmallest()
#     elif Choice == "2":
#         print("\n"*30  )
#         rickRoll()
#     elif Choice == "quit()":
#         quit()
#     else:
#         print("\n"*30  )
#         print(" enter a correct value")
#         main()

# main()


def largestAndSmallest(): 
    print(" Largest and Smallest finder") 
    numInt = int(input('enter the number of elements in the list: ')) 
    lst = [] 
    for i in range(0,numInt): 
        left = numInt-i 
        num = int(input(f'enter the {left}. element of list: ')) 
        lst.append(num) 
    lst.sort() 
    print(f'your list is: {lst}') 
    print(f'largest num is {lst[-1]}') 
    print(f'smallest num is {lst[0]}') 
import math 
def powercalc_() : 
    print("POWER CALCULATOR") 
    x = float(input("enter base number : ")) 
    n = float(input("enter power to raise: ")) 
    print("base number",x,"raised to the power",n,"is",math.pow(x,n))
def PALINDROME_(): 
    print("PALINDROME CHECKER") 
    str = input("Enter a string: ") 
    if str[::-1] == str: 
        print("This is a palindrome!") 
    else: 
        print("This is not a palindrome!")
print("******MAIN MENU****** ") 
print("1.Find the largest and smallest numbers in a list") 
print("2.Given two integers X and N, computer x to the power n") 
print("3.Find whether a string is a palindrome or not") 
choice_ = int(input("enter choice (1,2,3): ")) 
if choice_==1 :
    largestAndSmallest()
elif choice_== 2 :
    powercalc_()
elif choice_==3 :
    PALINDROME_()
else:
    print("enter a choice out of (1,2,3)")