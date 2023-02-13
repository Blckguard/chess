def testing(my_pieces):

    move = input('Command: ')

    if move == '':
        return 0
    elif move[0] == '$':
        for my_piece in my_pieces:
            if move[1:3] == my_piece.id and move[2:4] == my_piece.location:
                my_piece.id = move[1] + move[4]
                my_piece.location = move[4:6]