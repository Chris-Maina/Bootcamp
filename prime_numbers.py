#number=raw_input()

def printPrimeNumbers(number):
     """
     Code to output prime numbers
     """
     listPrime=[]
     try:
          if isintance(number,basestring):
               raise Exception
          for prime in range (0,number+1):
               if prime > 1:
                     for num in range(2,prime):
                           if(prime%num)==0:
                               break
                     else :
                          listPrime.append(prime)
     except :
          
          print('Invalid output')
     else:
          return listPrime
     
     
     

#print(printPrimeNumbers('one'))
         
     


