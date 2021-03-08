from game.board import board_matrix as initial_board, get_options, show, set_choice
from game.status import check_status
from game.player import get_current_player
from game.loggers import get_logger

logger, file_logger = get_logger(__name__)


def start():
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

    logger.info('Welcome and good luck!')

    while not is_over:
        if is_correct_choice:
            player_name, sign = get_current_player(step)
            logger.info('%s is your turn.' % player_name)

            available_options = get_options(board_matrix)

        show(board_matrix)
        logger.info('Pick a choice from available options: %s' % available_options)

        choice = input('Pick your choice: ')
        file_logger.info(f"{player_name} typed {choice}")

        try:
            choice = int(choice)

            if choice not in available_options:
                raise ValueError()
        except ValueError as e:
            logger.error('Your choice is not an option.')
            logger.exception(e)
            is_correct_choice = False
            continue
        else:
            is_correct_choice = True
            file_logger.info('Player choice: %s' % choice)

        board_matrix = set_choice(board_matrix, choice, sign)

        # Check if the game is won or not.
        is_won, is_over = check_status(board_matrix)

        if is_won:
            winner = player_name

        step += 1

    logger.info('Game Over!')

    if winner:
        logger.info(f'{winner} has won the game.')
    else:
        logger.info('Game ended as a draw.')
