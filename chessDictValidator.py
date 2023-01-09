import pprint

# Rules:

# for each player
totalPieces = 16
totalPaws = 8

# valid spaces in the board
validSpace = [
    '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', 
    '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', 
    '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
    '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', 
    '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', 
    '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
    '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g', 
    '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h'
    ]
# valid pieces names
validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
white = 'w'
black = 'b'

# Example of chess board:
board = {'1h': 'bking', '6c': 'wqueen', '7g': 'bbishop', '5h': 'bqueen', '3e': 'wking',
        '2h': 'bpawn', '3h': 'bpawn', '4h': 'bpawn', '6h': 'bpawn', '7h': 'bpawn', 
        '8h': 'bpawn', '1a': 'bpawn', '1b': 'bpawn', '1c': 'bpawn', '1d': 'bpawn', '1e': 'bpawn', 
        '1f': 'bking', '1g': 'bking'}
pprint.pprint(board)

# Board validation function:
def isValidChessBoard(board):
    '''
    Function to determine if given chess board is valid, according to rules.
    '''
    numOfWhites = 0
    numOfBlacks = 0
    numbOfWhitePawns = 0
    numbOfBlackPawns = 0
    numbOfWhiteKings = 0
    numbOfBlackKings = 0
    
    # valid spaces:
    for i in list(board.keys()):
        if i not in validSpace:
            quit('\nInvalid board! Space ' + i + ' out of bounds.')
    print('\nValid spaces.')

    # valid if only white or black:
    for i in list(board.values()):
        if i[0] != white and i[0] != black:
            quit('\nInvalid board! Space ' + i + ' out of bounds.')
        
        # counting number of white pieces.
        if i[0] == white:
            numOfWhites = numOfWhites + 1
            if i[1:] == 'pawn':
                numbOfWhitePawns = numbOfWhitePawns + 1
            if i[1:] == 'king':
                numbOfWhiteKings = numbOfWhiteKings + 1

        # counting number of black pieces.
        elif i[0] == black:
            numOfBlacks = numOfBlacks + 1
            if i[1:] == 'pawn':
                numbOfBlackPawns = numbOfBlackPawns + 1
            if i[1:] == 'king':
                numbOfBlackKings = numbOfBlackKings + 1
    print('Valid colors')
    
    # checking if each player is within the total number of pieces.renb/
    if numOfWhites > totalPieces or numOfBlacks > totalPieces:
        quit('\nInvalid board! Number of pieces out of bounds.')
    
    # checking if each player has 1 king
    if numbOfWhiteKings != 1 or numbOfBlackKings != 1:
        quit('\nInvalid board! Number of Kings out of bounds.')

    # checking if each player is within the total number of pawns.
    if numbOfWhitePawns > totalPaws or numbOfBlackPawns > totalPaws:
        quit('\nInvalid board! Too many Pawns.')
        
isValidChessBoard(board)