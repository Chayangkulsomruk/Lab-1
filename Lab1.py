L = 9
for j in range(1, L + 1):
  j = j - (L//2 +1)
  if j < 0:
    j = -j
    
  print(" " * j + "*" * (L - j * 2) + " " * j)


