primeNumberEnd = int(input("Input End Number "))

primeNumbers = []
def primeNumber(primeNumber):
    for  i in range(0,primeNumber):
        if i > 1:
            for j in range(2, int(i/2)+ 1):
                if i % j == 0:
                    break
            else:
                    primeNumbers.append(i)
        else:
            pass

primeNumber(primeNumberEnd)   

print("Set of Prime Numbers below: ")
print(f'List/Array Form: {primeNumbers}')
for i in primeNumbers:
     print(i)


        
  


