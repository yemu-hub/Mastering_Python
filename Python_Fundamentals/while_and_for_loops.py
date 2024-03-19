# Infinite loop
while True:
  print('Type Ctrl-C to stop me!')


# Slicing off the first character
x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
    
# Counts from the value of 'a' up to, but not include,'b'
a=0; b=10
while a < b:
    print(a, end=' ')
    a += 1

# 'pass' as a placeholder
while True: pass    # infinite loop that does nothing!

# 'continue' statement
x = 10
while x:
  x -= 1
  if x % 2 != 0: continue
  print(x, end= ' ')

 # Aternative to the above code(better!)
x = 10
while x:
    x -= 1
    if x  % 2 == 0:
      print(x, end= ' ')

# Interactive loop
while True:
  name = input("Enter name:")
  if name == 'stop' : break
  age = input("Enter age:")
  print('Hello', name, '=>', int(age) ** 2)

# Loop 'else' .... alternative to setting 'flag'
y = 9
x = y // 2
while x > 1:
  if y % x == 0:
    print(y, 'has factor', x)
    break
  x -= 1
else: print(y, 'is prime')


# Search a list for a value
found = False
while x and not found:
  if match(x[0]):
    print('NI!')
    found = True
  else:
    x = x[1:]
if not found:
  print('not found')

# Alternative to the above code(better!)
while x:
  if match(x[0]):
    print('NI!')
    break
  x = x[1:]
else: print('Not found')


# For loops

# traverse and print items in the list
for x in ["spam", "eggs", "ham"]:
  print(x, end='')



# Compute sum of items in the list
sum = 0
for x in [1,2,3,4]:
  sum += x
print(sum)

# Tuple assignment in for loops
T = [(1,2), (3,4), (5,6)]
for (a,b) in T:
  print(a,b)

# Iterating over dictionary using key as a target
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
  print(key,'=>', D[key])


#Iterating over dictionary using both key & values as a target
for (key,value) in D.items():
  print(key, '=>', value)

# Tuple assignment in 'for loops'
T = [(1,2),(3,4),(5,6)]
for both in T:
  a,b = both
  print(a,b)

# Using 'for loop' with nested structures
for ((a,b),c) in [((1,2),3), ((4,5),6)]: print(a,b,c)

# Using 'for loop' for any nested structure
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)

# Python 3.X extended sequence assignment in for loops
for (a, *b, c) in [(1,2,3,4), (5,6,7,8)]: print(a,b,c)


# Nested 'for loops'
items = ['aaa', 111, (4,5), 2.01] # Set of objects
tests = [(4,5),3.01]     # Keys to search for

for key in tests:
  for item in items:
    if item == key:
      print(key, 'was found')
      break
  else:
    print(key, 'not found')


# Alternative code to the above(better!)
for key in tests:         # for all keys
  if key in items:        # Let Python check for a match
    print(key, 'was found')
  else:
      print(key, 'not found')


# Build a list as it goes for later use
seq1 = 'spam'
seq2 = 'scam'

res = []
for x in seq1:
  if x in seq2:
    res.append(x)
print(res)

# Alternative to the above code (better!)
print([x for x in seq1 if x in seq2]) # list comprehension


# Counter Loops: range
print(list(range(5), list(range(2,5)), list (range(0,10,2))))

# Using 'range' function in 'for' loops
for i in range(3):
  print(i, 'Pythons')

# Sequence Scans: 'while' and 'range' vs 'for'
X = 'spam'
for item in X : print(item,end= ' ') # simple iteration and 'for' loop handles every thing automatically.

   # taking over the indexing logic explicitly
i = 0 
while i < len(X):     # while loop iteration
  print(X[i], end=' ')
  i += 1

  # manual range/len iteration(Not best option!)
for i in range(len(X)): print(X[i], end=' ')


# Sequence Shufflers: range and len
S = 'spam'
for i in range(len(S)):
  S = S[1:] + S[:1]  # Move front item to end
  print(S, end=' ')

for i in range(len(S)):
  X = S[i:] + S[:i]  # Rear part + front part
  print(X, end= ' ')

# Nonexhaustive Traversals: range VS Slices

 # range not best practice, but saves memory for large data
S = 'abcdefghijk'
for i in range(0, len(S), 2): print(S[i], end= ' ')

 # Slicing(copy) is better, but memory issues for large data)
for c in S[::2]: print(c, end=' ')


# Changing Lists: range VS Comprehensions
  
L = [1,2,3,4]

  # loop changes 'x', but not the list 'L'
for x in L:
  x += 1     # Changes x, not L

   # loop that change a list as it is being traversed
for i in range(len(L)):
  L[i] += 1              # Add one to each item in L
                         
  

   # List comprehension run faster without changing the orginal list in place!
[x + 1 for x in L]



# Parallel Traversals: zip and map
L1 = [1,2,3,4]
L2 = [5,6,7,8]

for (x,y) in zip(L1,L2):
  print(x,y, '--', x + y)


# Dictionary construction with zip
keys = ['spam', 'eggs', 'toast']
vals = [1,3,5]

D2 ={}
for (k,v) in zip(keys,vals): D2[k] = v
print(D2)


# Alternative to the above(better!)
D3 = dict(zip(keys,vals))
print(D3)


# Generate Both Offsets and Items: enumerate
S = 'spam'
offset = 0
for item in S:
  print(item, 'appears at offset', offset)
  offset += 1

  # Alternate to the above(better!)
S = 'spam'
for (offset, item) in enumerate(S):
  print(item, 'appears at ofset', offset)
