import random

target = random.randint(0,1000)
small = ('1','2','3','5','8','10')

big = ('15','25','50','75','100','150')
smallselection = random.choice(small)
bigselection = random.choice(big)


firstanswer = int(input('How many small numbers would you like?: '))
if firstanswer == 1:
    print('Your small number is:', random.choice(small))
    
elif firstanswer == 2:
    print('Your small numbers are:', random.choice(small), 'and', random.choice(small))
    
elif firstanswer == 3:
    print('Your small numbers are:', random.choice(small),',',random.choice(small), 'and', random.choice(small))
    
elif firstanswer == 4:
    print('Your small numbers are:', random.choice(small),',',random.choice(small),',',random.choice(small) ,'and', random.choice(small))
    
elif firstanswer == 5:
    print('Your small numbers are:', random.choice(small),',',random.choice(small),',',random.choice(small),',',random.choice(small) ,'and', random.choice(small))



secondanswer = int(input('How many big numbers would you like?: '))
if secondanswer == 1:
    print('Your big number is:', random.choice(big))
    
elif secondanswer == 2:
    print('Your big numbers are:', random.choice(big), 'and', random.choice(big))
    
elif secondanswer == 3:
    print('Your big numbers are:', random.choice(big),',',random.choice(big), 'and', random.choice(big))
    
elif secondanswer == 4:
    print('Your big numbers are:', random.choice(big),',',random.choice(big),',',random.choice(big) ,'and', random.choice(big))
    
elif secondanswer == 5:
    print('Your big numbers are:', random.choice(big),',',random.choice(big),',',random.choice(big),',',random.choice(big) ,'and', random.choice(big))

print('Your target is', target)