import random        # imports the random module, which contains a variety of things to do with random number generation.
number = random.randint(1,10)      #If we wanted a random integer, we can use the randint function Randint accepts two parameters: a lowest and a highest number.
for i in range(0,3):
    user = int(input("guess the number"))
         if user == number:
         print("Hurray!!")
               print(f"you guessed the number right it's {number}")
         break
if user != number:
print(f"Your guess is incorrect the number is {number}")
