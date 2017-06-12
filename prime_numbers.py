#number=raw_input()

def printPrimeNumbers(number):
     """
     Code to output prime numbers
     """
     listPrime=[]
     if isinstance(number,basestring):
           return "Invalid input"
     if isinstance(number,float):
           return "Invalid input"
     if number is None:
           return "Invalid input"
     if number < 0:
          return "Invalid input"
     for prime in range (0,number+1):
          if prime > 1:
               for num in range(2,prime):
                    if(prime%num)==0:
                         break
               else :
                          listPrime.append(prime)
      
           
     return listPrime
     
     
     
#print(printPrimeNumbers('one'))
#print(printPrimeNumbers(-10))
         
    


