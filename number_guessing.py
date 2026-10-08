import random

print(" 🎯 NUMBER GUESSING GAME 🎮")
print("---------------------")

number=random.randint(1,100)
attempts=0

while True:
   try:
     guess=int(input("Guess A Number  Between 1 To 100 \n"))
     attempts+=1

     if guess< 1 or guess> 100:
        print("please enter a number between 1 to 100")
        continue

     if guess<number:
        print("Too low! Guess again..🤞")   

     elif guess>number:
        print("Too High! Try again..✌️")

     else:
        print("🎉Correct!You won!🙌")
        print("You guessed it in",attempts,"attempts.")
        break

   except ValueError:
    print("Please enter a valid number.")
