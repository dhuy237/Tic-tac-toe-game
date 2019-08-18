import random

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']

def player_input():
    player = ''
    while player != 'X' and player != 'O':
        player = input("Please pick a marker 'X' or 'O' for player 1: ").upper()
    if player == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[2] == board[5] == board[8] == mark) or 
            (board[3] == board[5] == board[7] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark))

def choose_first():
    return str(random.randint(0,1))

def space_check(board, position):
    return not(board[position] == 'X' or board[position] == 'O')

def full_board_check(board):
    for i in range(1,10):
        if board[i] != 'X' and board[i] != 'O':
            return False
    return True

def player_choice(board):
    pos = input('Choose your next postion: ')
    if space_check(board, int(pos)):
        return int(pos)
    else:
        return 0
    
def replay():
    ans = input('Do you want to play again ? (Y|N) ').upper()
    return ans == 'Y'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' '] * 10
    player = player_input()
    ch = int(choose_first())
    player1 = player[ch]
    if ch == 0:
        player2 = player[ch + 1]
    else:
        player2 = player[ch - 1]
    
    print('Player {turn} go first!'.format(turn = ch + 1))
    
    while not full_board_check(board):
        # Player 1 turn
        p1_pos = player_choice(board)
        if p1_pos != 0:
            place_marker(board, player1, p1_pos)
        elif p1_pos == 0:
            print('Please choose another position!')
            p1_pos = player_choice(board)
            place_marker(board, player1, p1_pos)
        elif win_check(board, player1):
            print('Player 1 win!')
            break
        display_board(board)

        # Player2 turn
        p2_pos = player_choice(board)
        if p2_pos != 0:
            place_marker(board, player2, p2_pos)
        elif p2_pos == 0:
            print('Please choose another position!')
            p2_pos = player_choice(board)
            place_marker(board, player2, p2_pos)
        elif win_check(board, player2):
            print('Player 2 win!')
            break
        display_board(board)

    if not replay():
        break
