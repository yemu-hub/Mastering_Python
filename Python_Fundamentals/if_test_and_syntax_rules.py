# Multiway Branching
# x = 'Killer rabbit'
# if x == 'roger':
#     print("Shave and a haircut")
  
# elif x == 'bugs':
#     print("What's up doc?")
# else:
#     print('Run away! Run away!')


 # A dictionary-based 'switch'
 # Use has_key or get for default
# choice = 'ham'     
# print({'spam': 1.25,
#        'ham': 1.99,  
#        'eggs': 0.99,
#        'bacon': 1.10}[choice])  # result : 1.99

# the alternative to above

# choice = 'ham'
# if choice == 'spam':
#     print(1.25)
# elif choice == 'ham':
#     print(1.99)
# elif choice == 'bacon':
#     print(1.10)
# else:
#     print('Bad choice')

# Handling switch defaults

# branch = {'spam' : 1.25,
#           'ham': 1.99,
#           'eggs': 0.99}
# print(branch.get('spam', 'Bad choice'))
# print(branch.get('bacon','Bad choice'))

# same result as above
# choice = 'bacon'
# if choice in branch:
#   print(branch[choice])
# else: 
#   print('Bad choice')


  # using try ....except
# choice = 'bacon'
# try:
#     print(branch[choice])
# except:
#     print('Bad choice')


# Handling Larger Errors
