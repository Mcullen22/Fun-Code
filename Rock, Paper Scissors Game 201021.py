import random
result = ('rock','paper','scissors')
selection1 = input('What do you choose?: ')
selection2 = random.randint(0, 2)
print('I choose: ',selection1)
print('Player 2 result is: ',result[selection2])