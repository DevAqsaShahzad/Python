player1=str(input())
player2=str(input())

if(player1=='S' or player1=='s' and player2=='S' or player2=='s'):
    print("Game Draw")
if(player2=='R' or player2=='r' and player1=='R' or player1=='r'):
    print("Game Draw")
if(player2=='P' or player2=='p' and player1=='P' or player1=='p'):
    print("Game Draw")
if(player1=='R' or player1=='r' and player2=='S' or player2=='s'):
    print("Player 1 is winner")
if(player1=='P' or player1=='p' and player2=='S' or player2=='s'):
    print("Player 2 is winner")
if(player2=='R' or player2=='r' and player1=='S' or player1=='s'):
    print("Player 2 is winner")
if(player2=='P' or player2=='p' and player1=='S' or player1=='s'):
    print("Player 1 is winner")
if(player2=='P' or player2=='p' and player1=='R' or player1=='r'):
    print("Player 2 is winner")
if(player1=='P' or player1=='p' and player2=='R' or player2=='r'):
    print("Player 1 is winner")
