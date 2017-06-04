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
