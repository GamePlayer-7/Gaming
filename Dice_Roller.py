import random     # imports the random module, which contains a variety of things to do with random number generation.
while True:     
     print(''' 1. roll the dice             2. exit     ''')    
     user = int(input("what you want to do\n"))
     if user==1:         
        number = random.randint(1,6)
        print(number)     
    else:         
        break
