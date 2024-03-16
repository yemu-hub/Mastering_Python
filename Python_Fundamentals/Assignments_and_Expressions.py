# Sequence Assignments
nudge = 1 
wink = 2  # Basic assignment

A,B = nudge, wink # Tuple assignment
[C, D] = [nudge, wink] # List assignment
[a,b,c] = 1,2,3  # Assign tuple of values to list of names
(a,b,c ) = "ABC" # Assign string of characters to tuple

# Advanced sequence assignment patterns
string = 'SPAM' 
a,b,c,d = string  # Same number on both sides
a,b,c = string   # rise error, not equal in both sides
a,b,c = string[0], string[1], string[2:] # Index and slice

a,b = string[:2]
c = string[2:]
print(a,b,c) # result is : ('S','P','AM')

(a,b), c = string[:2],string[2:] # Nested sequences
print(a,b,c) # result is : ('S','P','AM')

((a,b),c) = ('SP', 'AM')  # Paired by shape and position
print(a,b,c) #  result is : ('S','P','AM')

red,green, blue = range(3) # assigning an integer series to a set of variables
print(red, blue) # result: (0,2)

# Extended Sequence Unpacking in Python 3.X
seq = [1,2,3,4]
a,b,c,d = seq
print(a,b,c,d) # result is: 1,2,3,4

a,b = seq 
print(a,b) # rise error!

a, *b = seq  # Python 3.X
print(a) # result : 1
print(b) # result : [2,3,4], not result is in list!

*a, b = seq
print(a) # result: [1,2,3]
print(b) # result : 4

a,*b,c = seq
print(a) # result: 1
print(b) # result: [2,3]
print(c) # result : 4

# Applciation to "for loops"
for (a,*b,c) in [(1,2,3,4), (5,6,7,8)]:
          print(a,*b,c)


for all in [(1,2,3,4), (5,6,7,8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a,b,c ) # The same effect as the above!


# Multiple-Target Assignments
a = b = c = 'spam'
print(a,b,c) # result: ('spam', 'spam', 'spam')

 # Multiple-target assignment and shared references
a = b = 0  # Attention: object assigned is immutable!
b = b + 1
print(a,b) # result is : (0,1)

a = b = [] # object assigned is mutable!
b.append(42)
print(a,b) # result is : ([42], [42])

a = [] 
b = []   # Protect shared object reffernce effect!
b.append(42)
print(a,b) # result is : ([], [42])

# Augmented Assignments

X = Y = 0
X = X + Y # Traditional form
X += Y    # Newer augmented form

S = 'spam'
S += 'SPAM'
print(S) # result is : 'spamSPAM'

L = [1,2]
L = L + [3]  # Concatenate: slower
print(L)     # result is : [1,2,3]
L.append(4)  # Faster, but in-place!
print(L)     # result is : [1,2,3,4]

L = L + [5,6] # Concatenate : slower
print(L)  # result is : [1,2,3,4,5,6] 
L.extend([7,8])  # Faster, but in place
# Attention: conatenation is less prone to the side effectts of shared object references!

L += [9,10]    # Mapped to L.extend([9,10])
print(L) # result is : [1,2,3,4,5,6,7,8,9,10]

# Augmented assignment and shared references
L = [1,2]
M=L      # L and M references the same object
L = L + [3,4] # Concatenation makes a new object
print(L,M)    # Changes L but not M

L = [1,2]
M = L
L += [3,4]  # But += really means extend
print(L,M)  # M sees the in-place change too!

# Expression Statements
eggs = ham = ''
spam(eggs,ham)  # Functions calls as expression stetemnet
spam.ham(eggs)  # Method calls as expression statement 
spam            # printing varaibles as expression statement
print(a,b,c,sep = '') # printing operation as expression st.
# yield x ** 2  # Yielding expression statemnts

x = print('spam') # print is a function call experessio in 3.X, result is 'spam'
print(x) # But it is coded as an expression statement, result is : None

#Expression Statements and In-place Changes
L = [1,2]
L.append(3)   # Append is an in-place change
print(L )   # result is : [1,2,3]

L = L.append(4)   # But append returns None, not L
print(L) # So we lose our list!
