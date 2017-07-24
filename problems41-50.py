def problem48():
  totalSum = 0

  for x in range (1, 1001):
    totalSum += pow(x, x)

  print(str(totalSum)[-10:])
