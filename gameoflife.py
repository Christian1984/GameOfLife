from time import sleep

X = 'X' # alive
O = '.' # dead

def cls():
    print '\n' * 100


def validate_board(board):
    n_lines = len(board)

    #Check if board is larger than 0
    if n_lines <= 0:
        return False


    for b_line in board:
        #Check if board is square
        if len(b_line) != n_lines:
            return False

        #Check if only X and 0 (zero!) are used
        for l_element in b_line:
            if not (l_element == X or l_element == O):
                return False

    return True


def print_board(board, i):
    cls()
    #print 'Livetime: ' + str(i)

    l_string = 'Livetime: ' + str(i) + '\n'
    for b_line in board:
        #l_string = ''
        for l_element in b_line:
            l_string += l_element + ' '
        l_string += '\n'

    print l_string


def copy_board(board):
    copy_board = []

    i = 0    
    for i in range(0, len(board)):
        copy_board.append([])

        j = 0
        for j in range(0, len(board[i])):
            copy_board[i].append(board[i][j])

    return copy_board


def evauluate_neighbours(board, x, y):
    alive_neighbours_count = 0

    #print '================'
    #print 'Evalauting cell X, Y: ' + str(x) + ', ' + str(y)

    for i in range(0, 9):
        eval_x = ((x - 1) + (i / 3)) % len(board)
        eval_y = ((y - 1) + (i % 3)) % len(board)

        #print 'Value ' + board[eval_y][eval_x] + ' at cell eval_x, eval_y = ' + str(eval_x) + ', ' + str(eval_y)

        if not (eval_x == x and eval_y == y):
            if board[eval_y][eval_x] == X:
                alive_neighbours_count += 1

    return alive_neighbours_count


def next_generation(board):
    i = 0
    new_board = copy_board(board)

    for l in board:
        j = 0        
        for e in l:
            #Evaluate cell and neighbours

            neighbours_alive = evauluate_neighbours(board, j, i)
            #print 'Cell X/Y : ' + str(j) + '/' + str(i) + ' has alive neighbours: ' + str(neighbours_alive)

            #Update cell
            cell_update = e

            if e == O: #if cell dead
                if neighbours_alive == 3:
                    cell_update = X
            else: #if cell alive
                if (neighbours_alive < 2) or (neighbours_alive > 3):
                    cell_update = O

            new_board[i][j] = cell_update

            j += 1
        i += 1

    return new_board


def game_of_live(board, n, ms):
    # board = gameboard
    # n = numbers of iterations
    # ms = time to wait between iterations

    if validate_board(board):
        for i in range(0, n + 1):
            print_board(board, i)
            board = next_generation(board)
            sleep(ms / 1000.)
    else:
        print 'Board is not valid!'




# =============
# TEST-CODE
# =============

blinker = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, X, X, X, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
    ]

block = [
    [O, O, O, O],
    [O, X, X, O],
    [O, X, X, O],
    [O, O, O, O]
    ]

toad = [
    [O, O, O, O, O, O],
    [O, O, O, O, O, O],
    [O, O, X, X, X, O],
    [O, X, X, X, O, O],
    [O, O, O, O, O, O],
    [O, O, O, O, O, O],
    ]

spaceship = [
    [O, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [X, X, X, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]
    ]

killer = [
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]
    ]

explosion = [
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, X, X, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, X, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, X, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
    [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]
    ]

game_of_live(explosion, 200, 100)
