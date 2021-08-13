import random
name= input("What's your name?")
print("Good luck champ! ",name)
words=['barcelona','real madrid','psg','manchester united','tottenham','arsenal','liverpool','bayern','juventus','inter','manchester ciy','sevilla']
#function to choose a random word
word=random.choice(words)
print("Guess the characters based on club football")
guesses=''
#any no. of turns can be used
turns=12
while turns>0:
    #counts no. of times failed
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            #for every failure +1 in failed    
            failed+=1
    if failed==0:
        print(f"{name} WINS")
        print("The correct word is ", word) 
        break       
    #if the user has input the wrong character then 
    guess=input("guess a character:")
    #every input character will be stored in guesses 
    guesses+=guess
    if guess not in word:
        turns-=1
        #if the character does not match the word
        print("WRONG")
        print("You have",+turns,"more guesses available")
        if turns==0:
            print("You lost") 
