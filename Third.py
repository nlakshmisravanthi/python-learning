# explanation about .split(' ')
pin, cash = input ('Enter your pin and cash:').split('@')
pinValue = int(pin)
if(pinValue == 22):
    cashValue = int (cash)
    if(cashValue > 5000):
        print('limit is 5000')
    else:    
        remainingAmount = 40000
        print ('Take your cash:{},balance in your account is :{}'.format(cashValue, remainingAmount),sep ="@@",end ='==========')
        print ('Thanks for using ATM')
else:
    print('wrong pin !!!') 
       
