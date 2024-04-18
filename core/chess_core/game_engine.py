from chess_board import ChessBoard, MoveCommand
from pieces import ChessPieceFactory

class GameEngine:
    def __init__(self):
        self.chess_board = ChessBoard()
        self.players = {'White': None, 'Black': None} 
        self.current_turn = 'White'

    def initialize_game(self):
        layout = ['R1', 'N1', 'B1', 'Q', 'K', 'B2', 'N2', 'R2']
        for i, piece in enumerate(layout):
            self.chess_board.place_piece(ChessPieceFactory.get_piece(piece, 'White', (7, i)), (7, i))
            self.chess_board.place_piece(ChessPieceFactory.get_piece(piece, 'Black', (0, i)), (0, i))
        for i in range(8):
            self.chess_board.place_piece(ChessPieceFactory.get_piece('P', 'White', (6, i)), (6, i))
            self.chess_board.place_piece(ChessPieceFactory.get_piece('P', 'Black', (1, i)), (1, i))

    def move_piece(self, from_pos, to_pos):
        piece = self.chess_board.board[from_pos[0]][from_pos[1]]
        if piece and piece.color == self.current_turn:
            if self.chess_board.is_valid_move(piece, from_pos, to_pos):
                move_command = MoveCommand(self.chess_board, piece, from_pos, to_pos)
                move_command.execute()
                self.switch_turn()
            else:
                print("Invalid move")
        else:
            print("It's not your turn or no piece at position")

    def switch_turn(self):
        self.current_turn = 'Black' if self.current_turn == 'White' else 'White'

    def check_status(self):
        pass
