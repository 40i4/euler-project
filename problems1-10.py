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

