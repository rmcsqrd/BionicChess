import pygame
import time

def DisplayBoard():
    def flipColor(color):
        white = (240,240,240)
        black = (100,100,100)
        if not color or color == white:
            color = black
        else:
            color = white
        return color

    width=480         # measurements for the window
    height=480
    block_size= 60
    window = pygame.display.set_mode((width,height))
    background_color = (0,0,0)     # This is how I make the lines
    window.fill(background_color)
    c = None
    pygame.draw.rect(window,(255,0,0),pygame.Rect(0,0,width,height)) # red background
    for y in range(0,height,block_size):
        c = flipColor(c)
        for x in range(0,width,block_size):
            c = flipColor(c)
            rect = pygame.Rect(x , y , x+block_size , y+block_size )
            pygame.draw.rect(window, c , rect, 0)   # Leaves space for lines to be visible.

    for i in range(0,height+1,block_size):
        pygame.draw.line(window,(233,33,187),(i,0),(i,width),2)
        pygame.draw.line(window,(233,33,187),(0,i),(height,i),2)

    pygame.draw.line(window,(240,240,240),(height-2,0),(height-2,width),2) # fix for out of window line
    pygame.draw.line(window,(240,240,240),(0,width-2),(height,width-2),2) # fix for out of wondow line

    # Figuur1 = pygame.image.load('/Users/riomcmahon/Programming/BionicChess/Resources/Pieces/kin.gif')
    # window.blit(Figuur1, (420, 420))
    pygame.display.flip()
    return window

# imports
import chess
import chess.engine

# global
engine = chess.engine.SimpleEngine.popen_uci("/Users/riomcmahon/programming/BionicChess/ChessBot_venv/stockfish-10-mac/Mac/stockfish-10-64")
limit = chess.engine.Limit(time=0.01)

def initial():
    board = chess.Board()
    return board

def ComputerMove(gamestate):
    ai_move = engine.play(gamestate, limit)
    return ai_move.move

def ProcessUserInput(user_piece, user_move):
    """
    processes UPC-A user input into usable string
    syntax : x[r][c]xxxxxxxxx, [r] is row (1-8) and [c] is col (A-H)

    :param user_piece: UPC-A code of selected piece
    :param user_move: UPC-A code of selected destination
    :return:
    """
    col_transfer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    user_move = str(col_transfer[int(user_piece[2])-1]) + str(user_piece[1]) + str(col_transfer[int(user_move[2])-1]) + str(user_move[1])
    print('Selected Move :',user_move)
    return user_move

def RenderPiece(window, pieces, board_state):

    # piece, x, y
    sprite_dir = '/Users/riomcmahon/Programming/BionicChess/Resources/Pieces/'
    x = -5
    y = -5
    cnt = 0
    if len(board_state) == 1:
        for position in board_state[0]:
            xinc = 58
            yinc = 58
            if position == ".":
                if cnt <= 6:
                    x = x + xinc
                    cnt = cnt + 1
                else:
                    x = 0
                    y = y + yinc
                    cnt = 0
                # print(x, y, cnt)
            else:
                sprite = pygame.image.load(sprite_dir + pieces[position])
                window.blit(sprite, (x, y))
                pygame.display.flip()
                if cnt <= 6:
                    x = x + xinc
                    cnt = cnt + 1
                else:
                    x = 0
                    y = y + yinc
                    cnt = 0
                # print(x, y, cnt)
    else:
        for position in board_state:
            xinc = 58
            yinc = 58
            if position == ".":
                if cnt <= 6:
                    x = x + xinc
                    cnt = cnt + 1
                else:
                    x = 0
                    y = y + yinc
                    cnt = 0
                # print(x, y, cnt)
            else:
                sprite = pygame.image.load(sprite_dir + pieces[position])
                window.blit(sprite, (x, y))
                pygame.display.flip()
                if cnt <= 6:
                    x = x + xinc
                    cnt = cnt + 1
                else:
                    x = 0
                    y = y + yinc
                    cnt = 0
                # print(x, y, cnt)


if __name__ == '__main__':
    board = initial()
    window = DisplayBoard()  # https://stackoverflow.com/questions/48129687/how-do-i-color-in-specific-blocks-for-a-chess-board
    pieces = {"p": "bP.png", "r": "bR.png", "n": 'bN.png', "b": "bB.png", "q": "bQ.png", "k": "bK.png",
              "P": "wP.png", "R": "wR.png", "N": 'wN.png', "B": "wB.png", "Q": "wQ.png", "K": "wK.png"}
    initial_state=["rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR"]
    RenderPiece(window, pieces, initial_state)
    while(1):
        board_state = str(board).replace(" ", "")
        board_state = board_state.replace("\n", "")
        window = DisplayBoard()  # https://stackoverflow.com/questions/48129687/how-do-i-color-in-specific-blocks-for-a-chess-board
        try:
            user_piece = input('Select Piece:')
            user_move = input('Select Target Spot:')
            board_state = str(board).replace(" ", "")
            board_state = board_state.replace("\n", "")
            window = DisplayBoard()
            RenderPiece(window, pieces, board_state)

        except SyntaxError:
            user_move = None

        if user_move != None and user_piece != None:
            user_move = ProcessUserInput(user_piece, user_move)
            user_move = chess.Move.from_uci(user_move)
            if user_move in board.legal_moves:
                board.push(user_move)
                RenderPiece(window, pieces, board_state)
            else:
                print('ILLEGAL MOVE')
                window = DisplayBoard()
                RenderPiece(window, pieces, board_state)
                continue

            ai_move = ComputerMove(board)
            ai_move = chess.Move.from_uci(str(ai_move))
            if ai_move in board.legal_moves:
                board.push(ai_move)
            else:
                continue

            print(board)

            board_state = str(board).replace(" ", "")
            board_state = board_state.replace("\n", "")
            window = DisplayBoard()
            RenderPiece(window, pieces, board_state)


