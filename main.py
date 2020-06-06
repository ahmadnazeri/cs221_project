
import chess
import chess.svg

from engine.engine import Engine

def main():
    fen = "r1b2k1r/ppp1bppp/8/1B1Q4/5q2/2P5/PPP2PPP/R3R1K1"
    color = "white"
    board = chess.Board(f"{fen} {color[0]}")

    print(board)
    
    chess_engine = Engine(board, color)

    board = chess_engine.find_next_move()

    print("-"*15)
    print(board)





if __name__ == '__main__':
    main()