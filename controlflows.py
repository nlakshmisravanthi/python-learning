#=============== Control flow program======================
'''lastball=4
if lastball==6:
    print('Won the Match')
else:
    print('Lost the match') 
lastball=6
if (lastball==6): # we can also enclose with ()
    print('Won the Match')
else:
    print('Lost the match') '''

# Program to check wheather  number is odd or even
number=int(input('Enter a Number:'))
if number%2==0:
   print('It is even number')
else:
    print('IT is odd number')   

print(' ============nested if===================')
number1=int(input('Enter a Number1:'))
if number1%2==0:
    if number1%4==0:
       print('It is divisible by 2 & 4')
    else:
         print('IT is not divided by 4')  
else:
    print('sorry')     

    




