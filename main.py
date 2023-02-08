import os
from chess_rules import check_if_legal_white, check_if_legal_black

class pieces:
    def __init__(self, id, location, value):
        self.id = id
        self.location = location
        self.value = value
        self.taken = False
        self.coordinate = 0

dict_white = {'Ra': 'a1', 'Nb': 'b1', 'Bc': 'c1', 'Qd': 'd1', 'Ke': 'e1', 'Bf': 'f1', 'Ng': 'g1', 'Rh': 'h1',
                        'Pa': 'a2', 'Pb': 'b2', 'Pc': 'c2', 'Pd': 'd2', 'Pe': 'e2', 'Pf': 'f2', 'Pg': 'g2', 'Ph': 'h2'}
dict_black = {'Ra': 'a8', 'Nb': 'b8', 'Bc': 'c8', 'Qd': 'd8', 'Ke': 'e8', 'Bf': 'f8', 'Ng': 'g8', 'Rh': 'h8',
                        'Pa': 'a7', 'Pb': 'b7', 'Pc': 'c7', 'Pd': 'd7', 'Pe': 'e7', 'Pf': 'f7', 'Pg': 'g7', 'Ph': 'h7'}
previous_moves = []

def create_objects(objects):

    # creating two lists of objects containing the id and location of pieces using the piece_location list
    # returning list of objects for black and white

    values = {'R': 5, 'N': 3, 'B': 3, 'Q': 10, 'P': 1, 'K': 0}

    object_list = []

    for id, location in objects.items():
        value = values[id[0]]
        a = pieces(id, location, value)
        object_list.append(a)

    return object_list

objects_white, objects_black = create_objects(dict_white), create_objects(dict_black)

def create_board():

    # creates the board dictionary taking the location of pieces from the piece objects in pairs like: 'a1': '+'

    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    minus_columns = ['b', 'd', 'f', 'h'] 
    board = {}
    counter = 2

    for column in columns:
        # iterating through the columns and rows to create coordinate pairs which get added to the
        # dictionary together with a '+' for a white field or '-' for a black field
        if column in minus_columns:
            counter = 2
            for row in range(1,9):
                if counter % 2 == 1:
                    board[column + str(row)] = '+'
                else:
                    board[column + str(row)] = '-'
                counter += 1
        else:
            for row in range(1,9):
                if counter % 2 == 0:
                    board[column + str(row)] = '+'
                else:
                    board[column + str(row)] = '-'
                counter += 1
    
    for field in board:
        for piece in objects_white:
            if field == piece.location:
                board[field] = piece.id[0]

    for field in board:
        for piece in objects_black:
            if field == piece.location:
                board[field] = piece.id[0]

    return board

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def player_move(my_pieces, opponent_pieces, player):

    # takes a move from the player in the format "Ra1a4" = Rook a1 to a4, takes the first letter of the piece to move, the field where it is on,
    # and the field where it's supposed to go. 

    move = input(player + ' to move: ')
    piece_locations = [i.location for i in my_pieces]
    opponent_locations = [i.location for i in opponent_pieces]
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    successful = False

    while not successful:
        for my_piece in my_pieces:

            # successful move and checks if piece was taken, changing '.location' to 0 and '.taken' to True
            if all([move[0:2] == my_piece.id, move[1:3] == my_piece.location, move[3:5] not in piece_locations]):

                if (player == 'White' and check_if_legal_white(move, my_pieces, opponent_pieces)) or (player == 'Black' and check_if_legal_black(move, my_pieces, opponent_pieces)):
                    my_piece.id = move[0] + move[3]
                    my_piece.location = move[3:5]
                    successful = True

                    if len(previous_moves) < 8:
                        previous_moves.append(f'{my_piece.id[0]}{my_piece.location}')
                    else:
                        previous_moves.pop(0)
                        previous_moves.append(f'{my_piece.id[0]}{my_piece.location}')

                    if my_piece.location in opponent_locations:
                        opponent = opponent_pieces[opponent_locations.index(my_piece.location)]
                        opponent.taken = True
                        opponent.location = 0
                        previous_moves[-1] = f'{my_piece.id[0]}x{my_piece.location}'
                else:
                    print('not a legal move.\n')
                    move = input('Try again: ')

            # checks if the move is proper format
            elif len(move) != 5 or move[0].islower():
                print('not proper format.\n')
                move = input('Try again: ')
            # checks if coordinates exist
            elif any([int(move[2]) > 8, int(move[2]) < 1, int(move[4]) > 8, int(move[4]) < 1, move[1] not in columns, move[3] not in columns]):
                print('Coordinates don\'t exist\n ')
                move = input('Try again: ')
            # checks if piece exists on field
            elif move[1:3] not in piece_locations:
                print('None of your pieces on that field.\n')
                move = input('Try again: ')
            # checks if there is already a piece on the field to move to
            elif move [3:5] in piece_locations:
                print('There is already one of your pieces on that field.\n')
                move = input('Try again: ')

def taken_list(opponent_pieces):

    # takes list of objects and returns list of taken pieces and score of these pieces

    score = 0
    taken_pieces = []

    for piece in opponent_pieces:
        if piece.taken:
            score += piece.value
            taken_pieces.append(piece.id[0])

    return taken_pieces, score

def get_coordinates():

    all_objects = objects_white + objects_black
    conversion = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}

    for piece in all_objects:
        if piece.location == 0:
            piece.coordinate = '00'
        else:
            piece.coordinate = conversion[piece.location[0]] + piece.location [1]


def draw_board():

    # draws the board onto the console using the dictionary created in the create_board function and draws a list of taken pieces + the players score

    taken_white, score_white = taken_list(objects_black)
    taken_black, score_black = taken_list(objects_white)

    board = create_board()
    return     f"""
    {' '.join(previous_moves)}

    Black: {score_black} {' '.join(taken_black)}
    
    8 |{board["a8"]}|{board["b8"]}|{board["c8"]}|{board["d8"]}|{board["e8"]}|{board["f8"]}|{board["g8"]}|{board["h8"]}|
    7 |{board["a7"]}|{board["b7"]}|{board["c7"]}|{board["d7"]}|{board["e7"]}|{board["f7"]}|{board["g7"]}|{board["h7"]}|
    6 |{board["a6"]}|{board["b6"]}|{board["c6"]}|{board["d6"]}|{board["e6"]}|{board["f6"]}|{board["g6"]}|{board["h6"]}|
    5 |{board["a5"]}|{board["b5"]}|{board["c5"]}|{board["d5"]}|{board["e5"]}|{board["f5"]}|{board["g5"]}|{board["h5"]}|
    4 |{board["a4"]}|{board["b4"]}|{board["c4"]}|{board["d4"]}|{board["e4"]}|{board["f4"]}|{board["g4"]}|{board["h4"]}|
    3 |{board["a3"]}|{board["b3"]}|{board["c3"]}|{board["d3"]}|{board["e3"]}|{board["f3"]}|{board["g3"]}|{board["h3"]}|
    2 |{board["a2"]}|{board["b2"]}|{board["c2"]}|{board["d2"]}|{board["e2"]}|{board["f2"]}|{board["g2"]}|{board["h2"]}|
    1 |{board["a1"]}|{board["b1"]}|{board["c1"]}|{board["d1"]}|{board["e1"]}|{board["f1"]}|{board["g1"]}|{board["h1"]}|
       a b c d e f g h

    White: {score_white} {' '.join(taken_white)}
    """

for i in range(20):
    cls()
    print(draw_board())
    get_coordinates()
    player_move(objects_white, objects_black, 'White')
    cls()
    print(draw_board())
    get_coordinates()
    player_move(objects_black, objects_white, 'Black')
