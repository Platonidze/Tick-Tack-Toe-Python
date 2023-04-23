def display(board):
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')


def change_board(board, position, symbol):
    board[int(position[0])][int(position[1])] = symbol


def position_check(board, position):
    if int(position[0]) > 2 or int(position[0]) < 0 or int(position[1]) > 2 or int(position[1]) < 0:
        return True
    if board[int(position[0])][int(position[1])] == ' ':
        return False
    else:
        return True


def win_check(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return 'X'
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return 'X'
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return 'X'
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return 'X'
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return 'X'
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return 'X'
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'X'
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'X'
    elif board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
        return '0'
    elif board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':
        return '0'
    elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        return '0'
    elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
        return '0'
    elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
        return '0'
    elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':
        return '0'
    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
        return '0'
    elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':
        return '0'
    else:
        return 'continue'


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
counter = 0
display(board)
while True:
    position = []
    if counter % 2 == 0:
        position = input("Player's 1 move: ").split()
        while position_check(board, position):
            print("Wrong move!")
            position = input("Player's 1 move: ").split()
        change_board(board, position, 'X')
    else:
        position = input("Player's 2 move: ").split()
        while position_check(board, position):
            print("Wrong move!")
            position = input("Player's 2 move: ").split()
        change_board(board, position, '0')

    display(board)

    if win_check(board) == 'X':
        print('Player 1 won!')
        break
    elif win_check(board) == '0':
        print('Player 2 won!')
        break

    if counter >= 8:
        print('Draw!')
        break
    counter += 1