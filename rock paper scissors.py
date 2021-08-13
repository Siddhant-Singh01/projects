import random
print("Winning rules of the rock paper scissor game:\n"+"Rock v/s paper->paper wins \n"+"Rock v/s scissor->Rock wins \n"+"paper v/s scissor->scissor wins \n ")
while True:
    print("Enter the choice \n 1.Rock \n 2.Paper \n 3.Scissor \n")
    #take the input from the user
    choice=int(input("User Enter your choice:"))
    #looping to check a valid input is entered
    while choice>3 or choice<1:
        choice=int(input("ENter a valid input:"))
    #assigning a choice name to each number
    if choice==1:
        choice_name='Rock'    
    if choice==2:
        choice_name='Paper'
    if choice==3:
        choice_name='Scissor'
    print("User choice1 is: ", choice_name)
    print("\n Now it's computer turn........")
    #computer chooses randomly between 1 and 3
    comp_choice=random.randint(1,3) 
    #looping until comp_choice value is equal to choice value
    while comp_choice==choice:
        comp_choice=random.randint(1,3)       
    if comp_choice==1:
        comp_choice_name='Rock'    
    if comp_choice==2:
        comp_choice_name='Paper'
    if comp_choice==3:
        comp_choice_name='Scissor'
    print("Computer choice is: ", comp_choice_name)
    print(choice_name, "V/S", comp_choice_name) 
    #winning's condition
    if((choice==1 and comp_choice==2)or(choice==2 and comp_choice==1)):
        print("Paper wins =>")
        result="Paper"
    elif((choice==2 and comp_choice==3)or(choice==3 and comp_choice==2)):
        print("Scissor wins =>")
        result="Scissor"
    else:
        print("Rock wins =>")
        reult="Rock"
    #Printing either computer or user wins
    if(result==choice_name):
        print("<==User wins==>")
    else:
        print("<==Computer wins==>")
    print("Do you want to play again? (Y/N)")
    ans=input()
    if(ans=='N' or ans=='n'):
        break
#coming out odf while loop we print thanks for playing
print("\nThanks for playing")

        

        