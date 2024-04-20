# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)



# ROCK=["ROCK","rock","R"]
# PAPER=["PAPER","paper","P"]
# SCISSOR=["SCISSOR","scissor","S"]

print("WELCOME TO ROCK, PAPER, SCISSOR GAMEPLAY\nSELECT ONE OF THE OPTIONS\n1.START\n2.NEW GAME\n3.EXIT\n")


userip=int(input("CHOICE: "))

if(userip==3):
    print("See You Later")
else:
    playername1=input("Enter Player 1 name : ")
    playername2=input("Enter Player 2 name : ")



while (userip==1):
    

    player1=input("{}'s Choice: ".format(playername1))
    player2=input("{}'s Choice: ".format(playername2))
    
    
    
    if(player1== "ROCK"):
        if(player1==player2):
            print("Game Tied")
        elif (player2=="SCISSOR"):
            print("{} WINNER!!".format(playername1))
        elif(player2=="PAPER"):
            print("{} WINNER!!".format(playername2))

        
        elif(player2=="Q"):
            print("See You Later")
            break
        

    elif(player1=="SCISSOR"):
        if (player2=="PAPER"): 
            print("{} WINNER!!".format(playername1))
        elif(player2=="ROCK"):
            print("{} WINNER!!".format(playername2))
        elif(player2=="Q"):
            print("See You Later")
            break
        
        
    elif(player1=="PAPER"):
        if (player2=="ROCK"):
            print("{} WINNER!!".format(playername1))
        elif(player2=="SCISSOR"):
            print("{} WINNER!!".format(playername2))
        elif(player2=="Q"):
            print("See You Later")
            break
        

    elif(player2=="Q") or (player1=="Q") :
        print("See You Later")
        break
        
    
    else:
        print("Invalid Choice")

    
        



