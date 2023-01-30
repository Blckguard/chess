# classes created already but not in use yet, will later use to assign unique id and
# location coordinates in pairs f.e. (4,1) = d1 
class pieces:
    def __init__(self, id, location):
        self.id = id
        self.location = location

piece_location = [['R', 'a1'], ['N', 'b1'], ['B', 'c1'], ['Q', 'd1'], ['K', 'e1'], ['B', 'f1'], ['N', 'g1'], ['R', 'h1'], ['P', 'a2'], ['P', 'b2'],
                  ['P', 'c2'], ['P', 'd2'], ['P', 'e2'], ['P', 'f2'], ['P', 'g2'], ['P', 'h2'],
                  ['R', 'a8'], ['N', 'b8'], ['B', 'c8'], ['Q', 'd8'], ['K', 'e8'], ['B', 'f8'], ['N', 'g8'], ['R', 'h8'], ['P', 'a7'], ['P', 'b7'],
                  ['P', 'c7'], ['P', 'd7'], ['P', 'e7'], ['P', 'f7'], ['P', 'g7'], ['P', 'h7']]

def create_objects(piece_location):
    # creating a list of objects containing the id and location of pieces using the piece_location list
    # returning list of objects 
    piece_objects = []

    for i in range(32):
        a = pieces(piece_location[i][0], piece_location[i][1])
        piece_objects.append(a)
    return piece_objects

def create_board():
    # creates the board dictionary without pieces yet

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

print(draw_board())