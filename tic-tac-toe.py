board = [' ' for _ in range(9)]
def print_board():
    for i in range(3):
        print(board[3*i] + ' | ' + board[3*i+1] + ' | ' + board[3*i+2])
        if i < 2:
            print('--+---+--')
def check_winner(player):
    wins = [(0,1,2), (3,4,5), (6,7,8), 
            (0,3,6), (1,4,7), (2,5,8),  
            (0,4,8), (2,4,6)]           
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)
def game():
    player = 'X'
    for _ in range(9):
        print_board()
        move = int(input(f"Player {player}, choose position (0-8): "))
        if board[move] != ' ':
            print("Taken! Try again.")
            continue
        board[move] = player
        if check_winner(player):
            print_board()
            print(f"Player {player} wins!")
            return
        player = 'O' if player == 'X' else 'X'
    print_board()
    print("It's a tie!")
game()