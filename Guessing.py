secret_word="purple"
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

while guess!= secret_word and not(out_of_guesses):
   if guess_count < guess_limit:
    guess=input("Guess a Color: ").lower()
    guess_count +=1
    Chances= 3-guess_count 
    if guess!= secret_word and Chances==1:
       print(str(Chances) + " Chance left")
    elif guess!= secret_word:
       print(str(Chances) + " Chances left")    
    else:
        break

   else:
    out_of_guesses=True   

if out_of_guesses:
    print("Sorry you are out of guesses.")
else:
    print("Bravo!!")    

