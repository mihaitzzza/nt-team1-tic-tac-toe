from .board import board_matrix as initial_board, get_options, show, update_board
from .status import check_status
from .player import get_current_player
import logging
import random
import copy


logger = logging.getLogger(__name__)


def find_winning_cell(board_matrix, available_options, sign):
    """
    Creates a copy of the current state of the board and tries all the available options with the sign argument.
    Checks if any choice wins.
    returns True or False if there is a winning choice, along with the the choice itself.
    """
    is_won = False
    choice = None
    for choice in available_options:
        board_copy = copy.deepcopy(board_matrix)
        new_board = update_board(board_copy, choice, sign)
        is_won, _ = check_status(new_board)
        if is_won:
            break
    return is_won, choice


def check_cell(cell_number, board):
    """
    returns the Data ('x', 'o' or None) from the given cell in the given board
    """
    row = int((cell_number-.5) // 3)
    col = (cell_number - row * 3) - 1
    return board[row][col]


def computer_move(available_options, board_matrix, last_move, difficulty):
    """
    difficulties: 'easy' picks randomly from the available options
    'medium' checks to for a winning move for itself, or blocks player from winning on next move. 
    if there is no winning move next move, it chooses a random available option
    'hard' checks for win or blocks player like the medium difficulty, but also strategically picks a move
    if there is no winning or blocking move
    
    return:: choice
    """
    if difficulty == 'easy':
        choice = random.choice(available_options)
        return choice

    elif difficulty == 'medium':
        found_cell, choice = find_winning_cell(board_matrix, available_options, 'o')
        if found_cell:
            return choice
        found_cell, choice = find_winning_cell(board_matrix, available_options, 'x')
        if found_cell:
            return choice
        return random.choice(available_options)

    winning, choice = find_winning_cell(board_matrix, available_options, 'o')
    if winning:
        return choice
    blocking_needed, choice = find_winning_cell(board_matrix, available_options, 'x')
    if blocking_needed:
        return choice

    if last_move % 2 == 1 and last_move != 5:
        if 5 in available_options:
            return 5
        opposite_corner = 10 - last_move
        if check_cell(opposite_corner, board_matrix) == 'x':     
            for choice in available_options:
                if choice % 2 == 0:
                    return choice
    if last_move % 2 == 0:
        if 5 in available_options:
            return 5
    corners = [x for x in available_options if x % 2 == 1 and x != 5]
    return random.choice(corners or available_options)


def player_move(board_matrix, available_options):
    is_correct_choice = False
    while not is_correct_choice:
        show(board_matrix)
        print('Pick a choice from available options: ', available_options)
        logger.info('Pick a choice from available options: %s' % available_options)

        choice = input('Pick your choice: ')
        logger.info('Pick your choice: ')
        try:
            choice = int(choice)
            if choice not in available_options:
                raise ValueError(f"Your choice '{choice}' is not an available option. ({available_options})")
            is_correct_choice = True
        except ValueError as e:
            print('Your choice is not an option.')
            logger.error('Your choice is not an option.')
            logger.exception(e)
            continue
        logger.info('Player choice: %s' % choice)
        return is_correct_choice, choice


def play(cpu=None):
    """
    This is the engine of the game.
    """
    is_over = False
    step = 0
    available_options = []
    is_correct_choice = True
    sign = 'x'
    board_matrix = initial_board.copy()
    winner = None
    player_name = None
    last_move = None
    print('Welcome and good luck!')
    logger.info('Welcome and good luck!')

    while not is_over:
        if is_correct_choice:
            player_name, sign = get_current_player(step, cpu)
            print('%s is your turn.' % player_name)
            logger.info('%s is your turn.' % player_name)

            available_options = get_options(board_matrix)
        if player_name == 'CPU':
            choice = computer_move(available_options, board_matrix, last_move, cpu)
        else:
            is_correct_choice, choice = player_move(board_matrix, available_options)

        board_matrix = update_board(board_matrix, choice, sign)
        last_move = choice

        # Check if the game is won or not.
        is_won, is_over = check_status(board_matrix)

        if is_won:
            winner = player_name
        step += 1

    return winner
