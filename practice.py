#R1- Read users name
#R2- Read users age
#R3- Print Hi user name ! YOU are 30 years old.
#R4- Print the year when was the user born."you were born in the year 1990"
#R5- Read a random statement from the user and print the number of characters in that statement.
print('Hi,')
UserName =input('what is your name?')
Age =input('How old are you?')
CurrentYear=('2021')
print('Hi,',UserName,'! You are',Age,'years old.')
print('You were born in',int(CurrentYear)-int(Age))
Statement=input('Write your Statement,' " ")
print(len(Statement))


