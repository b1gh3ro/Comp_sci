
def largestAndSmallest():
    
    try:
        print("\033[1;32m Largest and Smallest finder")
        numInt = int(input('enter the number of numbers in the list: '))

        lst = []

        for i in range(0,numInt):
            left = numInt-i
            num = int(input(f'enter {left} number of digits: '))
            lst.append(num)

        print(f'your list is: {lst}')
        print(f'largest num is {max(lst)}')
        print(f'smallest num is {min(lst)}')

    except ValueError:
        print("\n"*30, '\u001b[31m Please enter an integer')
        largestAndSmallest()

    




def main():

    print("\033[1;32m 1. print largest and smallest numbers in a list")

    Choice = input("choose: ")

    if(Choice == "1" ):
        print("\n"*30  )
        largestAndSmallest()
    else:
        print("\n"*30  )
        print("\u001b[31m enter a correct value")
        main()

main()
