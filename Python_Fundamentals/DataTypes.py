#NUMBER DATA TYPES

#numbers with thier operatons
print(123 + 222) 
print(2*3)
print(2 **3)

#STRING DATA TYPES

#Strings and thier operations
S = 'Spam'
print(len(S))

# fetch elements using indexing and slicing
  #forward indexing
print(S[0])
print(S[1])
  #backward indexing
print(S[-1])
print(S[-2])

 #slicing
 print(S[1:3])
 print(S[1:])
 print([0:3])
 print([:3])
 print([:-1])
 print([:])

 #String concatenation
 print(S + 'xyz')
 print(S * 8) #repetition

 #String immutability
 S[0] = 'Z'
 print(S[0]) #raises error

 S = 'z' + S[1:]
 print (S) # works because S becomes new object
 
 #change data in place by extending into lists then join it
 S = 'shrubbery'
 L = list(S)
 print(L)
 L[1] = 'c'
 print(' '.join(L))  # result is 'scrubbery'

 #Type specific String methods
 print(S.find('pa') # find the offset of a substring in S
 print(S.replace('pa','xyz') #Replace occurences of a string in S with another
 print(s.upper()) # Converts to upper case
 print(S.isalpha()) #content test

 line = 'aaa,bbb,cccc,dd'
 print(line.split(',') #Split on a delimiter into a list of substrings
 
 line = 'aaa, bbb,ccc, dd\n'
 print(line.rstrip()) #Remove whitespace characters on the right side
 print(line.rstrip().split(',') # remove whitespace followed by split on a delimiter
 
 #Formatting
 print('{},eggs, and {}'.format('spam','SPAM!')
 print('{:,.2f}'.format(2963456.2546) #Separate decimal digits

 #LIST DATA TYPES

 L = [123,'spam',1.23] #A list of three different-type objects
 print(len(L)) #Number of items in the list
 print(L[0]) #Indexing by postion
 print(L[:-1]) # Slicing a list returns a new list
 print(L + [4,5,6]) # Concatination  make new list
 print(L*2) # repeat make new list

 #Type Specific Operations
 print(L.append('NI')) # Growing: add object at the end of list
 print(L.pop(2)) # Shrinking: delete an item in the middle

 M = ['bb','aa','cc']
 print(M.sort()) # sorts alphabetically in ascending
 print(M.reverse()) # reverses the order alphabeticlly in descending

 # List comprehension experession--an advanced operation
 M = [[1,2,3],
      [4,5,6],
      [7,8,9]]
 print([row[1] for row in M]) # Collect the items in column 2
 print([row[1] for row in M if row[1]%2 == 0] # Filter out odd items

 diag = [M[i][i] for i in [0,1,2]] # Collect a diagonal from matrix
 print(diag)
 doubles = [c*2 for c in 'spam'] # Repeat characters in a string
 print(doubles)

 # List Basic Operations

 print(len([1,2,3])) # Length
 print([1,2,3] + [4,5,6]) # Concatination
 print(['NI!']*4 ) # Repetition
 print([1,2,3] + "34") # Raise error, convert "34" into list or the list into string.
  
  # List Iteration and Comprehensions
  print( 3 in [1,2,3]) # Check membership
  for x in [1,2,3]:    # Iteration
      print(x,end='')
  print (c * 4 for c in 'SPAM') # List Comprehension
  
  # Index and slice assignments
  L = ['spam', 'Spam', 'SPAM']
  L[1] = 'eggs' # Index assignment
  L[0:2] = ['eat', 'more'] # Slice assignment
   
   # Common List methods
  L = [1,2]
  L.extend([3,4,5]) # Add many items at end
  L.pop()  # Delete and return last item
  L.reverse() # In-place reversal method
  L = ['spam','eggs','ham']
  L.index('eggs')  # Index of an object(serach/find)
  L.insert(1,'toast') # Insert at position
  L.remove('eggs') # Delete by by value
  L.pop(1) # Delete by position
  L.count('spam') # Number of occurrences
  del L[0] # Delete one item
  del L[1:] # Delete an entire section

  L = ['Already','got','one']
  L[1:] = [] # Result is ['Alerady']

 #DICTIONARY DATA TYPES

 D = {'food': 'Spam', 'quantitiy':4, 'color': 'pink'}
 print(D['food']) # Fetch value of key 'food'
 print(D['quantity'] += 1) # Add 1 to 'quanitity' value

 # build dictionary begining from empty
 D = {}
 D['name'] = 'Bob'  # Create keys by assignment
 D['job'] = 'dev'
 D['age'] = 40
 print(D)
 print(D['name'])

  #nested dictionary
 rec = {'name' : {'first':'Bob', 'last': 'Smith'},
        'jobs': ['dev', 'mgr'],
        'age': 40}
 print(rec['name']) # prints 'first' and 'last' names
 print(rec['name']['last']) # Index the nested dictionary
 print(rech['jobs'][-1]) # Index the nested list
 print(rec['jobs'].append('janitor')) # Exapnad Bob's job description in place

 # checking key before accessing dic.
 D = {'a':1, 'b': 2, 'c': 3}
 if not 'f' in D:
    print('missing')
 
    # Sorting keys: for loops
ks = list(D.keys()) # Unordered keys list
ks.sort() # Sorted keys list
for key in ks:
    print(key, '=>', D[key]) # Iterate through sorted keys
# Or
for key in sorted(D):
    print(key, '=>', D[key])

# Changing Dectionary in Place
D = {'eggs':3, 'spam':2, 'ham':1}
D['ham'] = ['girl','bake','fry'] # Change entry(vlaue=list)
del D['eggs'] # Delete entry
D['brunch'] = 'Bacon'  # Add new entry

D = list(zip(['a', 'b', 'c']), [1,2,3])) # Zip together keys and values
D = dict(zip(['a', 'b', 'c']), [1,2,3])) # Make a dict from zip result
D = {x: x ** 2 for x in [1,2,3,4]} # Dictionary comprehension 
D = {c: c * 4 for c in 'SPAM'}    # Loop over any iterable
D = {k: v for (k,v) in zip(['a','b','c'], [1,2,3,4])}
D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS','HAM']}


# TUPPLE DATA TYPES

T = (1,2,3,4)
print(len(T)) 
print(T + (5,6)) # print concatinated values
print(T[0]) # print value at a given index

#Type specific methods
print(T.index(4)) # prints index of '4' 
print(T.count(4)) # prints frequency of '4'

T[0] = 2
print(T[0]) # raise error, tuple is immutable

T = (2,) + T[1:]
print(T) # print without error, because new tuple object is created

T = 'spam', 3.0, [11,22,33]
print(T[1])# prints '3.0'
print( T[2][1]) # prints '22'
print(T.append(4)) # raise error, tuple is immutable

print((1,2) + (3,4)) # Concatenation
print((1,2)*2) # Repetition
T = (1,2,3,4)
print(T[0], T[1:3]) # Indexing and slicing

T = ('cc','aa','dd', 'bb')
tmp = list(T) # Make a list from a tuple's items
tmp.sort()    # Sort the list
T = tuple(tmp) # Make a tuple from the list's items
sorted(T)     # Or use the sorted built-in, and save two steps
L = [x + 20 for x in T] # Comprehension converts tuple to list
T = (1,[2,3],4)
T[1] = 'spam' # This fails: can't change tuple itself
T[1][0] = 'spam' # This works: can change mutables inside

# Named Tuples
bob = ('Bob',40.5,['dev','mgr']) # Tuple record
bob[0], bob[2] # Access by positon


# FILES

f = open('data.txt', 'w') # Make a new file in output mode
f.write('Hello\n')  # Write strings of characters to it
f.close()  # Close to flush output buffers to disk

f = open('data.txt') 
text = f.read() # Read entire file into a string
print(text)

text.split() # File content is always a string

for line in open('data.txt') : print(line) # Automatically reads line by line and prints

