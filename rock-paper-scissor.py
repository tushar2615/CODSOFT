print("\t\tWelcome to my Game!\n")

print("\t\tRules of this game")
print("Rock beats scissors, scissors beat paper, and paper beats rock.")
print("If you win, you will get 1 point.")
print("If you lose, your 1 point will be deducted.")
print("If the game is Tie, score remain same\n.")

print("You want to play with computer or with your friend")
print("Press 1 for computer & 2 for friend")
n=int(input())

if n==1:
    while n>0:
        print("Press 1 for 📃")
        print("Press 2 for ✂")
        print("Press 3 for 🪨\n")
        print("Press 4 for Quit")
        p1=int(input("Enter Player 1 choice: "))
        p2=int(input("Enter Player 2 choice: "))
        score1=0
        score2=0
        
        if p1==1:
            if p2==1:
                print("Both of you enter same input\n\t\tGame Tie")
                print("\t\tTry Again\n")
            elif p2==2:
                score2+=1
                print(f"\t\tPLayer 2 wins\nScore of Player1: {score1} & Score of Player2: {score2}")
            elif p2==3:
                score1+=1
                print(f"\t\tPLayer 1 wins\nScore of Player1: {score1} & Score of Player2: {score2}")
            else:
                raise ValueError("\t\tGiven input is incorrect\nPlease enter a no. again\n")
        
        elif p1==2:
            if p2==1:
                score1+=1
                print(f"\t\tPLayer 1 wins\nScore of Player1: {score1} & Score of Player2: {score2}")
            elif p2==2:
                print("Both of you enter same input\n\t\tGame Tie")
                print("\t\tTry Again\n")
            elif p2==3:
                score2+=1
                print(f"\t\tPLayer 2 wins\nScore of Player1: {score1} & Score of Player2: {score2}")
            else:
                raise ValueError("\t\tGiven input is incorrect\nPlease enter a no. again\n")
            
        elif p1==3:
            if p2==1:
                score2+=1
                print(f"\t\tPLayer 2 wins\nScore of Player1: {score1} & Score of Player2: {score2}")
            elif p2==2:
                score1+=1
                print(f"\t\tPLayer 1 wins\nScore of Player1: {score1} & Score of Player2: {score2}")
            elif p2==3:
                print("Both of you enter same input\n\t\tGame Tie")
                print("\t\tTry Again\n")
            else:
                raise ValueError("\t\tGiven input is incorrect\nPlease enter a no. again\n")
            
        elif p1==4 or p2==4:
            print(f"Score of Player1: {score1} & Score of Player2: {score2}")
        
        else:
            raise ValueError("\t\tGiven input is incorrect\nPlease enter a no. again\n")
        
        
elif n==2:
    while n>1:
        print("Press 1 for 📃")
        print("Press 2 for ✂")
        print("Press 3 for 🪨\n")
        print("Press 4 for Quit")
        p=int(input("Enter Player choice: "))
        score=0
        l=[3,3,3,1,2,1,2,3,3,1,1,3,1,2,2,1,1,1,2,2,3,1,1,2,3,2,2,1,2,3]
        for i in range(0,30):
            if p==4:
                print("Your Score: ",score,"\n")
                break
            
            elif p==l[i]:
                print("Both of you enter same input\n\t\tGame Tie\n")
                print("Your Score: ",score,"\n")
                
            elif p<l[i]:
                score-=1
                print("You lose this chance")
                print("Your Score: ",score,"\n")
                print("\t\tTry Again\n")
                
            elif p>l[i]:
                score+=1
                print("\t\tHurray!!\nYou won this chance\n")
                print("Your Score: ",score,"\n")
                
            else:
                raise ValueError("\t\tGiven input is incorrect\nPlease enter a no. again\n")
            
        else:
            print("\t\tWow!\nYou succesfully completed 30 round of our game")
            break
        
else:
    raise ValueError("\t\tGiven input is incorrect\nPlease enter a no. again\n")

