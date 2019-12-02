#create a new dictionary/map
tel={'jack' : 4098 , 'sape' : 4139}
print("\nKey Jack, value : " + str(tel['jack']) )

#add a new key-value pair
tel['guido']=4127 
print("\n\'guide\' added with key value " + str(tel['guido']))

#print the map
print(tel)

#delete an entry
del tel['sape']
print("\nDeleting entry for \'sape\'")
print(tel)


"""
    Looping Techniques
"""

#iterate over the map - Technique 1
print("\nLooping technique 1")
for x in tel:
    print("Key is " + str(x) + ", value is " + str(tel[x]))


# Technique 2
print("\nLooping Technique 2")
for k,v in tel.items():
    print(k,v)


#initialize empy dictionary
empty = dict()

#intialize another dictionary - with dict function
print()
a=dict(one=1, two=2, three=3)
print(a)

# initialize another dictionary - without dict constructor
print()
b={'one' : 1, 'two' : 2 , 'three' : 3}
print(b)

#intialiaze another dictionary 
print()
c=dict(zip(['one','two','three'],[1,2,3]))
print(c)

#intialize another dictionary
print()
d=dict([('two',2),('one',1),('three',3)])
print(d)

#initialize another dictionary
print()
e=dict({'three':3, 'one':1, 'two' :2})
print(e)

# dictionary check equivalency
print()
print("Dictionary equivalent : ", a==b==c==d==e)


#extract set of keys
keys=list(d)
print('\nKeys : ',keys)


# length/number of items in dictionary
length=len(d)
print("\nLength : ", length)


#get an element from the dictionary - Exception handling
try:
    value=a['one']
    print("\nValue found - 'one' ", value)
except KeyError:
    print("\nValue not found for 'one'")

#get an element from the dictionary
try:
    value=a['five']
    print("\nValue found - 'five' ", value)
except KeyError:
    print("\nValue not found for 'five'")

# Subclassing a dictionary and __missing__ method
class Counter(dict):
    """ example of subclassing a dictionary"""

    # __missing__ method handles if a key is not present
    def __missing__(self,key):
        return 0

c=Counter()
print("\nexample of __missing__ method use\nc['red'] : ",c['red'])
#set the value of a key
c['red']+=1
print("\nSet the value of the key \nc['red'] : ",c['red'])

#delete a key
del c['red']

#check the presense of key
print("\nIs'red' present in c? ",'red' in c)
print("\nIs'red' not present in c? ",'red' not in c)

#iterate over keys in dictionary
for i in iter(d):
    print(i)

#clear a dictionary
e.clear()
print("\ndictionary after clearing", e)

#restoring the value of e to original - shallow copy
e=a.copy() 
print("\ndictionary after shallow copy ", e)

#get the value from key without raising exception KeyError
print("\nValue for 'one' is : " ,c.get('one',99))
print("\nValue for 'four' is : (returns default value))" ,c.get('one',99))
print("\nValue for 'five' is : (returns None as no default value provided)" ,c.get('one'))

# items() - iterating over items
print("items() - iterating over items")
for key,value in a.items():
    print(key,value)
for x in a.items():
    print(x)

# keys() - iterating over keys
print("\nkeys() -- iterating over keys")
for key in a.keys():
    print(key)

# removing a key element from dictionary - pop()
print("\na['one'] is removed and returned - ", a.pop('one',98))
print("\na['five'] is removed and returned - (default value is returned)", a.pop('five',98))
try:
    print("\na['six'] is removed and returned - (default value is returned)", a.pop('six'))
except KeyError:
     print("\nException caught as a['six'] doesn't exist and pop() was not given default value")

#popitem - remove an arbitrary item - arbitrary removal - raises KeyError if empty dictionary
print("e dictionary before popitem() = " , e)
e.popitem()
print("e dictionary after popitem() = " , e)

#update the dictionary with key/value pair
e.update(seven=7, eight=8)
print("Updated e dictionary " , e)

