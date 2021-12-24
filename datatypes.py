#Data Type programs
print('Datatypes:')

# Numeric Data Types (int , Float , Complex)
marks =379
percentage = (marks/600)*100
print('Tenth class percentage:',percentage)
print('Passed out year: 2006')
firstyearmarks =271
percentage =(firstyearmarks/500)*100
print('First year Inter marks percentage:',percentage)
secondyearmarks=269
percentage=(secondyearmarks/500)*100
print('Second Year Inter marks percentage:',percentage)
totalmarks =540
percentage=(totalmarks/1000)*100
print('Total Inter Marks percentage:',percentage)
print('Inter passedout 2008:')
firstyeardegreemarks =386
percentage =(firstyeardegreemarks/750)*100
print('First year Degree marks percentage:',percentage)
secondyeardegreemarks=558
percentage=(secondyeardegreemarks/750)*100
print('Second Year Degree marks percentage:',percentage)
thirdyeardegreemarks=844
percentage=(thirdyeardegreemarks/1000)*100
print('Third Year Degree marks percentage:',percentage)

print(type(marks))
print(type(percentage))

# int ----> 10,20,-30
# Float ------> 0.23,12.34,5.333
# complex ------>10+2j
x=10-5j
print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())

# Sequence types:
#Strings:
#Single , double and triple quotes:
#Single and Double quotes is used as per the requirement of string.
#Triple quote will use in multiple lines of string. 
completeWomen=  "lakshmi Sravanthi"
print(completeWomen)
#Length of string: len(string)
#space can be taken as length 
#len() function calculates the length of any Object that has a size(lists dictionaries etc)
print(len(completeWomen))
print('Accessing Elements from string:')
#indexing:
print(completeWomen[5])
print(completeWomen[-3])
print('Slicing:')
#step 
#[start:end:step]
print(completeWomen[1:5])
print(completeWomen[0:7:2])
print(completeWomen[3:5:-3])
print(completeWomen[::-1])
print(completeWomen[::])
print(completeWomen[3:5:-3])
print(completeWomen[::-1])
print(completeWomen[3:5:-2])
completeWomen= "Amma"
print(completeWomen)
#string is collection of characters
#string is immutable
# we can not delete /update string 
# But we can change entire string 
# we can delete entire string by using del name
#only new strings can be assigned to the same name
#name ="sravanthi"
#name[2] = "a"-not possible
#name= "lakshmi" -possible
#Deleting entire string: we can delete all together
#name="sravanthi"
#del name [0]-not possible
#del name-possible
del completeWomen
learningPy ="Sravanthi you're  Awesome" 
#concatenation:combining two or more strings: +  ---->will help in adding statement together ,*----> this sign will help in repeating the statement
print(learningPy)
learningPy =("Sravanthi you're  Awesome"+"let's try to finish")*3
print(learningPy)
#Learning about in and not in :these are called membership operators
print("finish" in learningPy)
print("polo" in learningPy)
print("polo" not in learningPy)

#=======List========
print('=========List=========')
#Telugu ,english,math,science,social,hindi
#Holds Heterogenous data(different types of data) 
marks=[88,60,86,48,68,29,"Sravanthi"]
print(type(marks))
marks1=[88,60,86,48,68,29]
print(marks1)
family=["Pradeep","Chaitanya","Amma","Nana garu"]
#Ordered collection of items
print('family',len(family))
print(family)
#mutable
#Allows duplicate items like [88,88,90,40,40]
#create list starts with []
#Empty List
empty=[]
print(len(empty))
# one list inside another list
biodata=[31,"Sravanthi",3124639636,"address",family]
print(biodata)
print('Second family member',family[2])
print('Last family member',family[-1])
print(biodata[4][1])
# Change the list by using '=' assignment operator, similary we can use concatenation & reapeating list by use '+' and '*'
marks[5]=50
print(marks)
print(marks+family)
print((marks+family)*2)
'''Add item/items to the list'''
# using .append () for adding one item 
# using .extend(for multiple items but we have to add more than one item print.extend([]) to work
family.append("Anusha")
print(family) 
family.extend(["Sri","Jo","duthi","charan","mammya","attya","friend"])
print(family)
# How to add one specific position in the list
# By using .insert(position,value)
# insert multiple elements at specific postion using slicing[::]
family.insert(1,"Anusha")
print(family)
family[1:1]=["Sravanthi","mamya","attaya"]
print(family)
print("=============================")
# Delete / remove List items
del family[1:3]
print(family)
family.remove("attaya")
print(family)
#Learing about .remove(),pop(index),pop()
print(family.pop(6))#will use .pop(index)by giving item in the index place
print(family.pop())#if you leave the .pop() empty it will automatically delete last item
print('=================================================')
# Tuple
#----> similar as list#
#  ordered collection of items
# Immutable
#allows duplicate items
#tuple will use like this ex:'()'<-------called parenthesis, any number of iem and they may be any type
marks=(29,50,50,78,67,45)
print(type(marks)) 
friends=("pavan ","pranav","pradeep","raju",[20,30,40,50])#with '()'
family="pradeep","jo","sri"#without '()'
print(type(family))
print(marks[4])
print(friends[2])
print(family[2])
friend="nandhu"# Tuple can also be created with out '()'
print(type(friend)) # If only one item in the list it will consider type as string
friend=("Nandhu",)# if you want that one item in the list as tuple you have to add "," next to the item then it shows as type ---->tuple
print(type(friend))
print('=====================================')
#Accessing tuple elements
# indexing, index error, type error ,nested tuples,negative indexing ,slicing
#similar as previous ones
print(friends[3])
print(friends[-1])
#print(friends[-1.09])
#changing tuple: we cannot be changed  the tuple but it the element itself is a mutable data type  like  list inside the tuple  #
# then we can change 
#ex: 
friends[4][0]=40
print(friends)
# Deleting a Tuple
 # we can't delete tuple it's  immutable but we can delete entire tuple by using del() keyword
# we can't update tuple as well
# converting a list to tuple 
# yes we can convert list as tuple by using ----->tuple(list) like this
# build-in methods: Index(value)-returns index of the given value.
# count(value)- returns the frequency of occurence of a specified value.
print('==========================================================')
# Boolean:true,false, compare
print('=================Boolean==========================')
learning =True
print(type(learning))
notpayingattention=False
print(type(notpayingattention))
#compare
a=20
b=-30
c=0
print(type(a==b))
print(bool(c))
print(bool(b))
print(bool(a))
print('================set==================')
languages={"Go","Git","Python","c &c++","Java"}
print(type(languages))
emptySet={} # This data type will shown as dictionaries
print(type(emptySet))
emptySet=() # This data type will shown as Tuple
print(type(emptySet))
# If the data type has to be emtySet we have use function like this emptySet=set()
emptySet=set()
print(type(emptySet))
print(languages)
#Accessing elements for set 
#Indexing : NO, we cannot use Indexing or slicing since they are unordered but, we can iterate over set by using "Loops"
#=====Add/Update========== in set
languages.add("kotlin") #To add one element to set ".add()"
print(languages)
languages.update(["Swift","PHP","Matlab","C","Ruby","Data Science","r"]) #To add multiple elements to set ".update([])"
print(languages)
# Difference between ".discard()" and ".remove()" is both does the same work
# But if we place the the wromg item / element in ".discard()" fuction it won't show error,".remove()" will show as 'key error'
languages.discard("r") 
print(languages)
languages.remove("Data Science")
print(languages)
languages.discard("loop") #   IT won't show any Error if we give the wrong item.
print(languages)
#languages.remove("loops") #it shows 'keyError' if we give wrong item.
print(languages)
print(languages.pop())# Remove and returns an item from the set.
# set is unordered so you never know what iem is going to be popped up. It can pop any item.
# Clear() : To remove all items from  the set.
languages.clear()
print(languages)
print('=====================Set Operations=================')
print('===Union===')
a={10,40,30,50,30}# set won't allow duplicate elements.
b={60,100,0,70,80}
abUnion= a.union(b)
print(abUnion)
abUnion= a|b #we can implement in both ways "a|b" or "a.union(b)" both will give the same result.
print(abUnion)# Sets are unodered
print('=====Intersection=======')
a={10,40,30,50,30}
b={60,100,30,70,50}
abIntersection=a.intersection(b)# we can also use "a&b" 
print(abIntersection)
abIntersection=a&b # we can also use "a.intersection(b)"
print(abIntersection) # the result will be the common elements in the  both sets
print("========Difference=======")
abDifference= a-b #set of elements that are only in 'a' set but not in 'b' set.
print(abDifference)
print('=========Symmetric Difference===========')
absymmetricdiff=a.symmetric_difference(b)
absymmetricdiff=a^b
print(absymmetricdiff)
print('=================================================================')
print('========================Dictionary=================================')
#Creating Dictionary
familyMembers={1:"pradeep",2:'sravanthi',3:"Sri",4:"Joshita"}
print(type(familyMembers))
print(familyMembers)
#Nested Dictionary
information={"Total Members":4,"Names":familyMembers}
print(information)
# Accessing Elements from Dictionary
print(information["Total Members"]) 
'''we will use keys'[]'by using square braces to get the values.if use '[]' if the key didn't found the result shows as KeyError.'''
print(information.get("Names"))# we can use .get()method to get the values.
'''if we use '.get()' the result will show as 'None'.'''
#print(familyMembers.get("followers"))
#print(familyMembers.get["followers"])
# Accessing Elements for "nested" dictionary
print(information.get("Names").get(3))
familyMembers["In-Laws"]="mammaya,Attaya"
#To add/update dictionary elements,we use assignment operator '=' for this.
#If key is present ,the value gets updated.
#If key is not present, then key:value pair will be added.
print(familyMembers)
D1={12:{'class':'B.sc','subject':'Math','percentage':50.5},
15:{"class":'B.sc','subject':'statistics','percentage':60.90},
16:{"class":'B.sc','subject':'ComputerScience','percentage':30.09}}
rollNumber= int(input('Enter your Roll Number:'))
percentage = D1[rollNumber]['percentage']
print('percentage is :',percentage)
subject=D1[rollNumber]['subject']
print('Subject is:',subject )
if (percentage>40):
    print('passed')
else:
    print('Failed')
