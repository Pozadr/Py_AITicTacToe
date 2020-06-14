# Tic Tac Toe game ^^
import os
board = [' ' for x in range(10)]


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def insert_letter(letter, pos):
    # Insert letter on game board.

    board[pos] = letter


def space_is_free(pos):
    # Check if space in 'pos' position is free.

    return board[pos] == ' '


def print_board(board):
    # Display current status of a game on screen.

    # Below function to clear screen in windows console.
    # cls()  # Clear screen after every player move.
    # print('Welcome in Tic Tac Toe game!')

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(bo, le):
    # Check if there are some 'O' or 'X' in line: 123 456 789 147 258 369  or to the cross: 159 357.

    return (bo[1] == le and
            bo[2] == le and
            bo[3] == le) or (bo[4] == le and
                             bo[5] == le and
                             bo[6] == le) or (bo[7] == le and
                                              bo[8] == le and
                                              bo[9] == le) or (bo[1] == le and
                                                               bo[4] == le and
                                                               bo[7] == le) or (bo[2] == le and
                                                                                bo[5] == le and
                                                                                bo[8] == le) or (bo[3] == le and
                                                                                                 bo[6] == le and
            bo[9] == le) or (bo[1] == le and
                             bo[5] == le and
                             bo[9] == le) or (bo[3] == le and
                                              bo[5] == le and
                                              bo[7] == le)


def player_move():
    # Player interface.
    # Preventing from wrong data.

    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def comp_move():
    # Computer player logic.

    # Preparing a list of possible moves.
    # Write "x" (counter of enumerate) to list for all empty places ' ' in list "board" without "board[0]" (and x != 0).
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    move = 0  # Define variable 'move', which is later return to 'main' function.

    # Checking possibilities: 1st to win 'O' and 2nd to block player 'X'.
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]  # Creating a copy of the board.
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    # If there is no possibilities to win by program and player then check corners of a board.
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)  # Checking: is some corner in possible moves? Yes: create a list of that corners.
    if len(corners_open) > 0:  # If some of the corners are free, take a random of them and return move function 'main'.
        move = select_random(corners_open)
        return move

    # If before conditions aren't done check middle of a board.
    if 5 in possible_moves:
        move = 5
        return move

    # Last possible place to add a sign are edges.
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def select_random(li):
    # Return random value from list. Used in computer player logic comp_move().

    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(board):
    # Check if game continuing is possible.
    # Return True or False to main loop of the game.

    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome in Tic Tac Toe game!')
    global board
    print_board(board)

    # Main loop of the game.
    play_game = True
    while play_game:
        while not(is_board_full(board)):
            if not(is_winner(board, 'O')):
                player_move()
                print_board(board)
            else:
                print('Sorry, O\'s won this time!')
                break

            if not(is_winner(board, 'X')):
                move = comp_move()
                if move == 0:
                    print('Tie Game!')
                else:
                    insert_letter('O', move)
                    print('Computer placed an \'O\' in position ', move, ':')
                    print_board(board)
            else:
                print('X\'s won! Congratulations!')
                break

        if is_board_full(board) or is_winner(board, 'O') or is_winner(board, 'X'):
            play_again = 0
            while play_again != 'y' and play_again != 'Y' and play_again != 'N' and play_again != 'n':
                play_again = input('Do you want to play again? y/n: ')
                if play_again == 'y' or play_again == 'Y':
                    board = [' ' for x in range(10)]
                    print_board(board)
                    is_board_full(board)
                else:
                    play_game = False


main()
