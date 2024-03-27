heading="welcome to stickman game"
print(heading.title().center(80))
print("\n\n")
movie_name="devi".lower()
mn1=['d','e','v','i']
mn2=[]
print("_   _   _   _   _".center(80))
print("\n\n")
print("clue:...It is a movie name....")
chance=5
while True:
  guess=input("enter your guess:").lower()
  if guess == "":
    print("please enter any letter")
  elif guess in movie_name:
    print("your guess is correct")
    if guess not in mn2:
      mn2.append(guess)
  else:
    if chance>1:
      print("your guess is wrong")
      chance=chance-1
      print(f"you have {chance} chance ")
    else:
      print("you lose the game")
      break
  if len(mn1)==len(mn2):
    print("you won the game")
    print("The movie name is devi")
    break

  

      
