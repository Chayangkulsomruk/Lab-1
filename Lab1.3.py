def even_odd(L):
    if(L % 2 == 0):
        return True
    elif(L %2 != 0):
        return False
    else:
        return even_odd(L)
num = 6
if(even_odd( num )):
    print("This Number",num ,"is even")
else:
    print("This Number",num ,"is odd")

