
def largestAndSmallest():

    print(" Largest and Smallest finder")
    numInt = int(input('enter the number of numbers in the list: '))

    lst = []

    for i in range(0,numInt):
        left = numInt-i
        num = int(input(f'enter {left} number of digits: '))
        lst.append(num)
    lst.sort()
    print(f'your list is: {lst}')
    print(f'largest num is {lst[-1]}')
    print(f'smallest num is {lst[0]}')



def rickRoll():
    print("palindrome Finder")
    str = input("Enter a string: ")
    if str[::-1] == str:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome!")
    




def main():
    print("**** Main Menu ****")
    print("1. largest and smallest numbers in a list")
    print("2. Palindrome Finder")

    Choice = input("choose: ")

    if(Choice == "1" ):
        print("\n"*30  )
        largestAndSmallest()
    elif Choice == "2":
        print("\n"*30  )
        rickRoll()
    elif Choice == "quit()":
        quit()
    else:
        print("\n"*30  )
        print(" enter a correct value")
        main()

main()
