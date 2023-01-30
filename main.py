import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class pieces:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.taken = False

def create_objects():
    # creating two lists of objects containing the id and location of pieces using the piece_location list
    # returning list of objects for black and white =

    pieces_white = {'Ra': 'a1', 'Nb': 'b1', 'Bc': 'c1', 'Qd': 'd1', 'Ke': 'e1', 'Bf': 'f1', 'Ng': 'g1', 'Rh': 'h1',
                        'Pa': 'a2', 'Pb': 'b2', 'Pc': 'c2', 'Pd': 'd2', 'Pe': 'e2', 'Pf': 'f2', 'Pg': 'g2', 'Ph': 'h2'}
    pieces_black = {'Ra': 'a8', 'Nb': 'b8', 'Bc': 'c8', 'Qd': 'd8', 'Ke': 'e8', 'Bf': 'f8', 'Ng': 'g8', 'Rh': 'h8',
                        'Pa': 'a7', 'Pb': 'b7', 'Pc': 'c7', 'Pd': 'd7', 'Pe': 'e7', 'Pf': 'f7', 'Pg': 'g7', 'Ph': 'h7'}

    objects_white = []
    objects_black = []

    for id, location in pieces_white.items():
        a = pieces(id, location)
        objects_white.append(a)

    for id, location in pieces_black.items():
        a = pieces(id, location)
        objects_black.append(a)

    return objects_white, objects_black

objects_white, objects_black = create_objects()

def create_board():
    # creates the board dictionary taking the location of pieces from the piece objects
    
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

def draw_board():
    # draws the board onto the console using the dictionary created in the create_board function

    board = create_board()
    return     f"""
    8 |{board["a8"]}|{board["b8"]}|{board["c8"]}|{board["d8"]}|{board["e8"]}|{board["f8"]}|{board["g8"]}|{board["h8"]}|
    7 |{board["a7"]}|{board["b7"]}|{board["c7"]}|{board["d7"]}|{board["e7"]}|{board["f7"]}|{board["g7"]}|{board["h7"]}|
    6 |{board["a6"]}|{board["b6"]}|{board["c6"]}|{board["d6"]}|{board["e6"]}|{board["f6"]}|{board["g6"]}|{board["h6"]}|
    5 |{board["a5"]}|{board["b5"]}|{board["c5"]}|{board["d5"]}|{board["e5"]}|{board["f5"]}|{board["g5"]}|{board["h5"]}|
    4 |{board["a4"]}|{board["b4"]}|{board["c4"]}|{board["d4"]}|{board["e4"]}|{board["f4"]}|{board["g4"]}|{board["h4"]}|
    3 |{board["a3"]}|{board["b3"]}|{board["c3"]}|{board["d3"]}|{board["e3"]}|{board["f3"]}|{board["g3"]}|{board["h3"]}|
    2 |{board["a2"]}|{board["b2"]}|{board["c2"]}|{board["d2"]}|{board["e2"]}|{board["f2"]}|{board["g2"]}|{board["h2"]}|
    1 |{board["a1"]}|{board["b1"]}|{board["c1"]}|{board["d1"]}|{board["e1"]}|{board["f1"]}|{board["g1"]}|{board["h1"]}|
       a b c d e f g h
    """

def white_move():
    # takes a move from the player in the format "Ra1a4" = Rook a1 to a4
    move = input('white to move: ')

    for white in objects_white:

        black = objects_black[objects_white.index(white)]

        if move[0] == white.id[0] and move[1:3] == white.location:
            white.id = move[0:2]
            white.location = move[3:5]

        if white.location == black.location:
            black.taken = True

def black_move():
    # takes a move from the player in the format "Ra1a4" = Rook a1 to a4

    move = input('black to move: ')

    for black in objects_black:

        white = objects_white[objects_black.index(black)]

        if move[0] == black.id[0] and move[1:3] == black.location:
            black.id = move[0:2]
            black.location = move[3:5]

        if black.location == white.location:
            white.taken = True

def check_if_taken():

    for white in objects_white:
        if white.taken == True:
            white.location = 0

    for black in objects_black:
        if black.taken == True:
            black.location = 0

for i in range(9):
    cls()
    print(draw_board())
    white_move()
    check_if_taken()
    cls()
    print(draw_board())
    black_move()
    check_if_taken()
    cls()