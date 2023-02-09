conversion = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}

def piece_blocking(new_coord, piece, my_coords, opponent_coords):

    # checks if there is a piece blocking the lane or column
    # NOTE ONLY WORKS FOR STRAIGHT MOVES FOR NOW! NOT DIAGONAL!

    all_coords = my_coords + opponent_coords
    y_to_move = [str(i)+piece.coordinate[1] for i in range(int(piece.coordinate[0])+1, int(new_coord[0]))]
    x_to_move = [piece.coordinate[0]+str(i) for i in range(int(piece.coordinate[1])+1, int(new_coord[1]))]

    for i in all_coords:
        if i[0] in y_to_move or i[1] in x_to_move:
            print(x_to_move, y_to_move)
            return True
    print(x_to_move, y_to_move)
    return False

def check_if_legal_white(move, my_pieces, opponent_pieces):

    # checks if the move taken, was a legal move. this function is for pawns specifically since they are the only pieces who can't move backwards
    # so i had to make two separate function for black and white

    new_coord = conversion[move[3]] + move[4]
    new_coord_x, new_coord_y = int(new_coord[0]), int(new_coord[1])
    opponent_coords = [i.coordinate for i in opponent_pieces]
    my_coords = [i.coordinate for i in my_pieces]

    for piece in my_pieces:
        coord_x, coord_y = int(piece.coordinate[0]), int(piece.coordinate[1])

        if piece.id == move[0:2]:
            if piece.id[0] == 'P':
                if not piece_blocking(new_coord, piece, my_coords, opponent_coords):
                    if coord_x == new_coord_x and coord_y - new_coord_y == -1 and new_coord not in opponent_coords:
                        return True
                    elif coord_x != new_coord_x and coord_y - new_coord_y == -1 and new_coord in opponent_coords:
                        return True
                    elif coord_y == 2 and coord_x == new_coord_x and coord_y - new_coord_y == -2 and new_coord not in opponent_coords:
                        return True
    return False

def check_if_legal_black(move, my_pieces, opponent_pieces):

    new_coord = conversion[move[3]] + move[4]
    new_coord_x, new_coord_y = int(new_coord[0]), int(new_coord[1])
    opponent_coords = [i.coordinate for i in opponent_pieces]
    my_coords = [i.coordinate for i in my_pieces]

    for piece in my_pieces:
        coord_x, coord_y = int(piece.coordinate[0]), int(piece.coordinate[1])

        if piece.id == move[0:2]:
            if piece.id[0] == 'P':
                if not piece_blocking(new_coord, piece, my_coords, opponent_coords):
                    if coord_x == new_coord_x and coord_y - new_coord_y == 1 and new_coord not in opponent_coords:
                        return True
                    elif coord_x != new_coord_x and coord_y - new_coord_y == 1 and new_coord in opponent_coords:
                        return True
                    elif coord_y == 7 and coord_x == new_coord_x and coord_y - new_coord_y == 2:
                        return True
    return False

def check_if_legal_uni(move, my_pieces, opponent_pieces):

    new_coord = conversion[move[3]] + move[4]
    new_coord_x, new_coord_y = int(new_coord[0]), int(new_coord[1])
    opponent_coords = [i.coordinate for i in opponent_pieces]
    my_coords = [i.coordinate for i in my_pieces]

    for piece in my_pieces:
        coord_x, coord_y = int(piece.coordinate[0]), int(piece.coordinate[1])

        if piece.id == move[0:2]:
            if not piece_blocking(new_coord, piece, my_coords, opponent_coords):
                # adding move rules for Rooks
                if piece.id[0] == 'R':
                    if coord_x == new_coord_x and coord_y != new_coord_y:
                        return True
                    elif coord_x != new_coord_x and coord_y == new_coord_y:
                        return True
                # adding move rules for Bishops
                if piece.id[0] == 'B':
                    if coord_x != new_coord_x and coord_y != new_coord_y:
                        return True
