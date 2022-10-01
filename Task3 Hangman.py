hangman_word="HANGMAN"
guessletter=""
guess_count=0
guess_limit=8
out_of_guesses=False
word="-------"
H=A=N=G=M= False

while word != hangman_word and not(out_of_guesses):
   if guess_count < guess_limit:
    guessletter=input("Guess a Letter: ").upper()
    guess_count +=1
    Chances= 8-guess_count 

    if guessletter not in "HANGMAN" and Chances==1:
       print(str(Chances) + " Chance left")
       print(word) 

    elif guessletter not in "HANGMAN":
       print(str(Chances) + " Chances left")    
       print(word)

    elif guessletter in "HANGMAN":
        guess_count -=1
        if guessletter== "H": 
          if not H:
           word = word[:0] + "H" + word[1:]
           print(word)
           H=True
          else:
           print("Error, Guess a different letter!")  
           
        elif guessletter== "A":
          if not A:
            word = word[:1] + "A" + word[2:]
            word = word[:5] + "A" + word[6:]
            print(word)
            A=True
          else:
           print("Error, Guess a different letter!")  
          

        elif guessletter== "N":
          if not N:
            word = word[:2] + "N" + word[3:]
            word = word[:6] + "N" + word[7:] 
            print(word)   
            N=True
          else:
           print("Error, Guess a different letter!")  
           

        elif guessletter== "G":
          if not G:
            word = word[:3] + "G" + word[4:]
            print(word)
            G=True
          else:
           print("Error, Guess a different letter!")  
           

        elif guessletter== "M":
          if not M:
            word = word[:4] + "M" + word[5:] 
            print(word)
            M=True
          else:
           print("Error, Guess a different letter!")  

        else:
          break    
       
    else: 
       break

   else:
    out_of_guesses=True   

if out_of_guesses:
    print("Sorry you are out of chances.")
else:
    print("Bravo!!!!!!!")    
    print("The word is: HANGMAN")




    