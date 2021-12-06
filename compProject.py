
def largestAndSmallest():
    
    try:
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

    except ValueError:
        print("\n"*30, '31m Please enter an integer')
        largestAndSmallest()

    




def main():

    print("1. print largest and smallest numbers in a list")

    Choice = input("choose: ")

    if(Choice == "1" ):
        print("\n"*30  )
        largestAndSmallest()
    else:
        print("\n"*30  )
        print(" enter a correct value")
        main()

main()
