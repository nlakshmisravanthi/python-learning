# program using if and else if , if :---->if ,else:-----> else if
pin=input('Enter your pin number:')
if (pin == '22'):
    cash =input('Enter your cash:')
    cashValue = int (cash)
    if (cashValue > 5000):
        print('cash limit is 5000')
    else:
        atmAmount = 240000
        remainingAmount = atmAmount - cashValue
        print ('Take your cash ',cash ,remainingAmount ,sep ='==>>>')
        print ('Thank you for ',sep='')
        print ('using ATM')
else:
    print ('Wrong pin!!!!')    