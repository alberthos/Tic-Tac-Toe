# cleaning the terminal window
import os

clear = lambda: os.system('cls')


class player(object):
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.score = 0


# nice way to display list
def display(board):
    for row in board:
        for symbol in row:
            print(symbol, end=' ')
        print()


# check for correctness of input and returning x,y touple
def check_coordinates(input, board):
    if len(input) != 2:
        print('Incorrect length of entry.')
        return -1
    # Checking x coordinate and make adaptation
    if input[0] in 'abc':
        if input[0] == 'a':
            x = 3
        elif input[0] == 'b':
            x = 9
        else:
            x = 15
    else:
        print('Wrong input of X coordinate! It can only be -> a b c')
        return -1

    # check y coordinate and make adaptation
    if 0 < int(input[1]) < 4:
        if input[1] == '1':
            y = 2
        elif input[1] == '2':
            y = 5
        else:
            y = 8
    else:
        print('Wrong input of Y coordinate! It can only be 1-3')
        return -1

    # Checking if the coordinate is already taken
    if board[y][x] != '-':
        print('Spot is already taken.')
        return -1

    return x, y


# entering the signs on board and displaying the board
def boardWrite(currentPlayer, board, score):
    while True:
        entered = input('{} enter coordinates(xy): '.format(currentPlayer.name))
        if check_coordinates(entered, board) != -1:
            x, y = check_coordinates(entered, board)
            board[y][x] = currentPlayer.sign
            clear()
            print(score)
            display(board)

            break


# check for winner
def check_board(board) -> bool:
    grid = []
    winner = False
    # extract grid without coordinates
    for row in range(2, 9):
        grid.append(board[row][3:16])

    # check row strike
    j = 0
    for i in range(0, 7, 3):
        if grid[i][j] == grid[i][j + 6] == grid[i][j + 12] != '-':
            winner = True

    # check column strike
    for i in range(0, 13, 6):
        if grid[0][i] == grid[3][i] == grid[6][i] != '-':
            winner = True

    # check diagonal strike
    if grid[0][0] == grid[3][6] == grid[6][12] != '-' or grid[0][12] == grid[3][6] == grid[6][0] != '-':
        winner = True

    if winner:
        return True


def draw_board() -> list:
    board = [
        ['   a     b     c  '],
        ['      |     |     '],
        ['1  -  |  -  |  -  '],  # 2
        [' _____|_____|_____'],
        ['      |     |     '],
        ['2  -  |  -  |  -  '],  # 5
        [' _____|_____|_____'],
        ['      |     |     '],
        ['3  -  |  -  |  -  '],  # 8
        ['      |     |     '],
    ]
    # transfer in 2d array
    twoDboard = []
    # every row is one big string
    # and each that string is transformed in
    # list and appended in twoDboard and
    # then we have 2d array which is easier to handle
    for row in board:
        for string in row:
            l = list(string)
            twoDboard.append(l)
    return twoDboard


def firstPlayer(player1, player2):
    while True:
        draw = input('Who is gonna play first {}({}) or {}({}): '.format(player1.name, player1.name[0], player2.name,
                                                                         player2.name[0]))

        # whose first letter is entered he/she is first player

        if draw.lower() == player1.name[0].lower():
            first = player1
            second = player2
            print('{} plays first'.format(first.name))
            return first, second
        elif draw.lower() == player2.name[0].lower():
            first = player2
            second = player1
            print('{} plays first'.format(first.name))
            return first, second
        else:
            print('Wrong entry!')


def times_of_play():
    while True:
        n = input('how many wins? ')
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('Wrong entry! Need to be number.')

def score_board(player1, player2):
    return 'Total Score \n{} -> {}\n{} -> {}\n'.format(player1.name, player1.score, player2.name, player2.score)

def chech_for_win(turn, board, player):
    # check for winer after third move
    if turn >= 3:
        winner = check_board(board)
        if winner:
            player.score += 1
            clear()
            print('\n!!!!  {} is winner of this round !!!!\n'.format(player.name))
            return True


def main():
    # Create players
    p1 = player(input('Players of X: '), 'X')
    p2 = player(input('Player of O: '), 'O')

    # Create map
    main_board = draw_board()

    # who is going to be first
    # 0-th element 1st player
    # 1-th element 2nd player
    order = firstPlayer(p1, p2)

    # how many time will game loop
    scoreToWin = times_of_play()

    turn = 1
    # to swamp players for moves
    playerC = 0
    clear()
    print(score_board(order[0],order[1]))
    display(main_board)
    while order[0].score < scoreToWin and order[1].score < scoreToWin:
        boardWrite(order[playerC], main_board, score_board(order[0],order[1]))
        if chech_for_win(turn, main_board, order[playerC]):
            main_board = draw_board()
            print(score_board(order[0],order[1]))
            display(main_board)
        if playerC < 1:
            playerC += 1
        else:
            playerC = 0
        turn += 1

def again():
    while True:
        loop = input('Wanna play again? (y/n)')
        if loop == 'n':
            return False
        elif loop == 'y':
            return True
        else:
            print('Wrong answer')

gameon = True
while gameon:
    main()
    gameon = again()
