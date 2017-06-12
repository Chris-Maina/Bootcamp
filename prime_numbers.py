#number=raw_input()

def printPrimeNumbers(number):
     """
     Code to output prime numbers
     """
     listPrime=[]
     if isinstance(number,basestring):
           raise Exception
     if isinstance(number,float):
           raise Exception
     if number is None:
           raise Exception
     if number < 0:
           raise Exception
     for prime in range (0,number+1):
          if prime > 1:
               for num in range(2,prime):
                    if(prime%num)==0:
                         break
               else :
                          listPrime.append(prime)
      
           
     return listPrime
     
     
     
#print(printPrimeNumbers(10))
#print(printPrimeNumbers(-10))
         
    


