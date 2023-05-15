
def largestNumber():
    list = []
    for i in range(5):
        addToList = int(input("Add a number to the list "))
        list.append(addToList)
        list.sort()
    print(f'Largest number in the list is {list[-1]}')

largestNumber()