# program for B-Tech Admissions:
eamcetRank=int(input('Enter your Eamcet Rank:'))
if (eamcetRank<=1000): print('You are eligible for C-1') # for single statements we can use shorthand operation.
elif(eamcetRank>=1000 and eamcetRank<=10000):
    print('You are eligible for C-2')
elif eamcetRank>=10000 and  eamcetRank<=40000:
    print('you are eligible for C-3')
else:
    print('Sorry no colleges avsilable for your Rank')


