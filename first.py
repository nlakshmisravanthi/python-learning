# Learning Python
print('python-learning')
print('explaining to thanvi')
''' Learing about statements , indentation 
and comments'''  
print('new block')
# program to calculate number of guides
a = 200
b = 400
c = 40
d = 20
oneguidecost = 110
total = (a+b+c+d)
#name = 'sravanthi'
print(total)
print(total / oneguidecost)
name = 'pradeep'
print(type(name))
'''python doesn't have constants but everyone uses captial letters to identify as constant 
like'''
NAME = 'Sravanthi'
sum =10
def calculate():
    global sum 
    sum = 30
    sum = sum + 20
    currentSum = 200
    totalSum = sum + currentSum
    print(totalSum)

calculate();
print(sum)
# program to demonstrate input and output
# input is a string  and whatever you enter in the input considered as string
# type() is used to know what type of variable we gave
pin ,cash = input('Enter your pin and cash:').split('@')
cashValue = int(cash)
atmAmount = 30000
remainingAmount = atmAmount - cashValue
print ('Type of cash is :', type(cashValue))
print ('Take your cash ',cash ,remainingAmount,sep ="====> ", end = '\n')
print ('Thank you  for using ATM ',end = '\t')
print ('These are called parameters')
#The end = '\n' is the escape character /escape sequeance which we use for seperating lines
#sep = ' ' for seperating sentences
# end = '\t' is a tab space
