import math
for i in range(1000,10000):
           sqrtno=int(math.sqrt(i))
           if sqrtno*sqrtno==i:
               if all(int(digit)%2==0 for digit in str(i)):
                  print(i)
