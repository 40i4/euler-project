import math

def problem1():
    curr = 1
    sumMul = 0

    while curr < 1000:
        if curr % 3 == 0 or curr % 5 == 0:
            sumMul += curr
        curr += 1

    print(sumMul)


def problem2():
    prev = 1
    curr = 2
    sumEven = 0

    while curr < 4000000:

        nextN = prev + curr
        if curr % 2 == 0:
            sumEven += curr
        prev = curr
        curr = nextN

    print(sumEven)

    
    
def problem3():
    num = 600851475143
    div = 2
    biggestPrime = 0

    while div < math.sqrt(num):
        while num % div == 0:
            num //= div
        div += 1

    if num > 1:
        biggestPrime = num

    print(biggestPrime)


def problem4():
    maxProduct = 0
   
    for x in range (1, 1000):
        for y in range (1, 1000):
            product = x * y
            productBackwards = (str(product))[::-1]
            ifPalindrome = False
            
            ifPalindrome = True if str(product) == productBackwards else False
            
            if (ifPalindrome and product > maxProduct):
                print("new maxprod")
                maxProduct = product              
                
    print(str(maxProduct))    
    


def problem7():
    primes = [2, 3]
    primesCounter = 2

    def checkIfPrime(number, divider):

      global primesCounter

      if number % divider != 0:
        divider += 2
        if divider <= math.sqrt(number):
          checkIfPrime(number, divider)
        else:
          # print(number)
          primesCounter += 1
          primes.append(number)
          # print("primesCounter: ", str(primesCounter))

            
    def findNthPrime():
      divider = 3
      # primesCounter = 1

      for number in range(3, 100000000):
        if number % 2 != 0 and primesCounter < 10001:
            # print("heyy")
            checkIfPrime(number, divider)

      print("primesCounter: ", str(primesCounter))
      print("primes: ", primes)

    findNthPrime()


