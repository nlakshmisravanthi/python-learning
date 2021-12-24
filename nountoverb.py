sentence='His expression went dark.'
index=-1
print(sentence.split(' ')[index])
noun = sentence.split(' ')[index]
print(noun)
if  noun[len(noun)-1]=='.':
    noun=noun[:len(noun)-1]
print(noun)
verb=noun+'en'
print(verb)
