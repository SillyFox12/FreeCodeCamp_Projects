def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    #All posible winning combinations
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    #Prints Tic Tac Toe Board
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()


    def p1():
        n = choose_number()
        #Checks if a player has already played in that spot
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
                a = input()
                try:
                    a = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                #Runs when the input entered is not a number value
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue


    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congrats!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            #Checks if 9 plays have been made and if so calls a tie
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    #While the game is still playing
    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        p2()
        print()
   
    #Runs when the game endss
    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

#Runs the game
tic_tac_toe()
