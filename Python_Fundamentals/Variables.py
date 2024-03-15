# Creating variable of type Number
a = 3
b = 4

# Using objects in expressions
print(a+1 , a-1)
print(b*3, b/2)
print(a%2, b**2)
print(2 + 4.0, 2.0**b)
# print(c*2) #raise error, variable 'c' not assigned value

# Numeric Display Formats
print(b/(2.0 + a)) #print round off digits
print(1/2.0)

num = 1/3.0
print(num)
print('%e' % num) # String formatting expression
print('%4.2f' % num) # Floating point format
print('{0:4.2f}'.format(num)) # String foramtting method

# Comparisons: Normal and Chained
 # Normal comparison
print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

 #Chained comaprison
x = 2
y = 4
z = 6
print(x < y < z)
print(x < y and y < z)
print( x < y > z)
print( x < y and y > z)
print( 1.1 + 2.2 == 3.3) # False because 1.1 + 2.2 is not exactly 3.3.
print( int(1.1 + 2.2) == (3.3)) # True

 # Division: Classic,Floor and True
print(10/4)  # performs true division, result ='2.5'
print(10 // 4) # performs floor division, result = '2'
print(10 // -4) # performs floor divison, result = '-3'

 #Integer Precision
print(99999999999999999999999999999999 +1  ) # Adds and prints normlay in Python 3.X, but adds L in Python 2.X



#Creating String varialbles and operations
s = 'abc'
print(len(s))  # Length: number of items
c = 'abc' + 'def'
print(c) # prints the concatinated strings
b = 'NI!' * 4
print(b) # prints 'NI!' four times

myjob = "hacker"
for c in myjob:
  print(c, end="")

print("k" in myjob) # print 'True'
print("z" in myjob) # print 'False'
print("spam" in "abcspamdef") # print 'True'

