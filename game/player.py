def get_current_player(step, cpu):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration.
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        name = 'Player 1'
        sign = 'x'
    else:
        sign = 'o'
        if not cpu:
            name = 'Player 2'
        else:
            name = 'CPU'

    return name, sign


def display_winner(winner, logger):
    print('Game Over!')
    logger.info('Game Over!')

    if winner:
        print(f'{winner} has won the game.')
        logger.info(f'{winner} has won the game.')
    else:
        print('Game ended as a draw.')
        logger.info('Game ended as a draw.')