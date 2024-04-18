class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]


    def move_piece(self, from_pos, to_pos):
        piece = self.board[from_pos[0]][from_pos[1]]
        target = self.board[to_pos[0]][to_pos[1]]
        if target is not None and target.color != piece.color:
            self.capture_piece(from_pos, to_pos)
        self.board[to_pos[0]][to_pos[1]] = piece
        self.board[from_pos[0]][from_pos[1]] = None
        piece.position = to_pos

    def capture_piece(self, from_pos, to_pos):
        piece = self.board[from_pos[0]][from_pos[1]]
        captured_piece = self.board[to_pos[0]][to_pos[1]]

        print(f"{piece} captures {captured_piece} at position {to_pos}")
        
        
class MoveCommand:
    def __init__(self, board, piece, from_pos, to_pos):
        self.board = board
        self.piece = piece
        self.from_pos = from_pos
        self.to_pos = to_pos

    def execute(self):
        self.board.move_piece(self.piece, self.from_pos, self.to_pos)

    def undo(self):
        self.board.move_piece(self.piece, self.to_pos, self.from_pos)
        print(f"Move undone: {self.piece} back to {self.from_pos}")
        
        
        