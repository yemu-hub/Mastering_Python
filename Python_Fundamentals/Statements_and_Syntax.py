 # A simple interactive loop with multiple statements
   # while statemnet, and other 3 compound statements
# while True:
#     reply = input("Enter text: ")
#     if reply == 'stop' : break
#     print(reply.upper())
  

# Doing Math on User Inputs    
# while True:
#     reply = input("Enter text: ")
#     if reply == 'stop' : break
#     # print(print(reply ** 2))  # rise error: unsupported oprand
#     print(int(reply) ** 2) # cast to int. now works!
# print('Bye')

# Handling Errors by Testing
# while True:
#     reply = input("Enter text: ")
#     if reply == 'stop' :
#         break
#     # print(int(reply) ** 2) # if input is  invalid,eg. 'xxx',  rise error!
#     elif not reply.isdigit():  # handling for invalidity!
#         print("Bad!" * 5)
#     else: 
#         print(int(reply) ** 2)
# print('Bye')

# Handlig Errors with try Statements
# while True:
#     reply = input("Enter text: ")
#     if reply == 'stop' : break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!'*5)
#     else:
#         print(num **2)
        
# print('Bye')

# Supporting floating-point numbers
while True:
    reply = input("Enter text: ")
    if reply == 'stop' : break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!'*5)        
print('Bye')