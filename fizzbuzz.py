#Fizz Buzz

# Print till 20.
#Print Fizz if divisible by 3
#Buzz if divisible by 5
#FizzBuzz if divisible by 3 & 5
for count in range(1,21):
    if ((count%3==0) & (count%5==0)):
        print("FizzBuzz")
    elif count %5==0:
       print('Buzz') 
    elif count %3==0:
        print('Fizz')
    else:
        print (count)   


