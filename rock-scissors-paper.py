print("WELCOME to our ROCK-PAPER-SCISSOR GAME")

rounds = 0
moves =  []

movePlayer1 = 1
movePlayer2 = 2
movePlayer3 = 3

def rsp2(moves, player1, player2):
    if moves[player1-1] == moves[player2-1]:
        print("Tie between Player {} and Player {}.".format(player1, player2))
        return

    ##player1 win cases
    elif moves[player1-1] == "rock" and moves[player2-1] == "scissor" or moves[player1-1] == "paper" and moves[player2-1] == "rock" or moves[player1-1] == "rock" and moves[player2-1] == "scissor":
         return player1, player2

    ##player2 win cases
    elif moves[player1-1] == "rock" and moves[player2-1] == "paper" or moves[player1-1] == "paper" and moves[player2-1] == "scissor" or moves[player1-1] == "scissor" and moves[player2-1] == "rock":
        return player2, player1

    else:
        print("Invalid input.")
        return

while rounds != 5:
    
    i = 0
    while i != 3:
        input_move = input("Player {}'s move: ".format(i+1))
        if input_move == "rock" or input_move == "paper" or input_move == "scissor" or input_move == "Taylor Swift":
            moves.append(input_move)
            i += 1
        else: 
            print("Enter valid command.")

    if moves[2] == "Taylor Swift":
        try:
            a, b = rsp2(moves, movePlayer1, movePlayer2)
            print("Player {} won against Player {}.".format(a, b))
            rounds = 5
        except:
            print("Replay needed in case of Tie!")
            rounds += 1

    else:
        try:
            a, b = rsp2(moves, movePlayer1, movePlayer2)
            print("Player {} won against Player {}.".format(a, b))
            a, b = rsp2(moves, movePlayer1, movePlayer3)
            print("Player {} won against Player {}.".format(a, b))
            a, b = rsp2(moves, movePlayer2, movePlayer3)
            print("Player {} won against Player {}.".format(a, b))
            rounds = 5
        except:
            print("Replay needed in case of Tie!")
            rounds += 1