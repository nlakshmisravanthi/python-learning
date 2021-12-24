from datetime import date
birthYear=int(input('Enter your year of birth:'))
currentYear=(date.today().year)
age=currentYear - birthYear
print('Your age is:', age)
