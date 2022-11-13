def ABC(L):
   for i in range(L):
      for j in range(L - i - 1):
         print("", end = " ")
      for j in range(2 * i + 1):
         print("*", end = "")
      print()
   for i in range(L - 1):
      for j in range(i + 1):
         print("", end = " ")
      for j in range(2 * (L - i - 1) - 1):
         # print stars
         print("*", end = "")
      print()

n = int(input('Enter number: '))
ABC(n)

