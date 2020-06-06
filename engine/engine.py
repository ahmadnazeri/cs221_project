

import chess

class Engine:
    def __init__(self, board, color, depth=5):
        """
        Chess engine that finds a sequence of moves base
        board: chess.Board
        color: string "black" or "white"
        depth: integer
        """
        self._board = board
        self._color = color
        self._moves = []
        self._opponent = "white" if color=="black" else "black"
        self._depth = 4
        # 1=PAWN, 2=KNIGHT, 3=BISHOP, 4=ROOK, 5=QUEEN, 6=KING
        self._piece_type_values = {1: 1, 2: 3, 3: 3, 4: 5, 5:9, 6:100}

    def find_next_move(self):
        """
        finds the sequence of moves based on the board
        """

        _, board, moves = self._minimax(self._board, self._color, self._depth)

        return moves[0]


    def _minimax(self, board, color_turn, depth):
        """
        Utilizes minimax algorithm to find the best sequence of moves for the puzzle
        board: chess.Board
        color: string "black" or "white"
        depth: integer

        return: position_value, board, sequence_of_moves
        """

        if depth == 0 or board.is_checkmate():
            return (self._heuristic_function(board, color_turn), board, [])

        if color_turn == self._color:
            best_move_value = -float("inf")
            best_move = None
            best_boards = None

            for move in board.legal_moves:
                new_board = board.copy()
                new_board.push(move)

                move_value, move_board, move_boards = self._minimax(new_board, self._opponent, depth-1)

                if move_value >= best_move_value:
                    best_move_value = move_value
                    best_move = move
                    best_boards = move_boards


            # print(f"best_move: {new_board}, move: {move}, best_value: {best_move_value}, color: {color_turn}, depth: {depth}")
            best_boards.insert(0, best_move)
            return (best_move_value, best_move, best_boards)


        elif color_turn != self._color:
            best_move_value = float("inf")
            best_move = None
            best_boards = None

            for move in board.legal_moves:
                new_board = board.copy()
                new_board.push(move)

                move_value, move_board, move_boards = self._minimax(new_board, self._color, depth-1)

                if move_value <= best_move_value:
                    best_move_value = move_value
                    best_move = move
                    best_boards = move_boards

            # print(f"best_move: {new_board}, move: {move}, best_value: {best_move_value}, color: {color_turn}, depth: {depth}")
            best_boards.insert(0, best_move)
            return (best_move_value, best_move, best_boards)



    def _heuristic_function(self, board, color):
        """
        the heuristic function that determines value at the position
        """

        if color == self._color:
            multipler = -1
        else:
            multipler = 1

        if board.is_checkmate():
            return 10000*multipler
        elif board.is_check():
            return 100*multipler
        elif board.is_insufficient_material():
            return -10*multipler
        else:
            pieces = board.piece_map()

            total_value = 0

            for piece_position, piece in pieces.items():
                piece_type = piece.piece_type
                piece_color = piece.color

                if piece_color and self._color == "white":
                    piece_multipler = 1
                elif piece_color and self._color == "black":
                    piece_multipler = -1
                elif not piece_color and self._color == "white":
                    piece_multipler = -1
                elif not piece_color and self._color == "black":
                    piece_multipler = 1

                total_value += self._piece_type_values[piece_type]*piece_multipler

            return total_value
