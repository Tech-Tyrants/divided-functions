def reverse_number():
    num = int(input("Enter the integer number: "))  
    rev_num = 0 
    while (num > 0):  
        remainder = num % 10  
        rev_num = (rev_num * 10) + remainder  
        num = num // 10  
        
    print("The reverse number is : {}".format(rev_num))  

reverse_number()