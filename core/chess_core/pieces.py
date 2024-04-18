class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
    def move(self, position):
        pass

class King(ChessPiece):
    def move(self, position):
        print(f"Moving King to {position}")

class Queen(ChessPiece):
    def move(self, position):
        print(f"Moving Queen to {position}")

class Rook(ChessPiece):
    pass

class Knight(ChessPiece):
    pass

class Bishop(ChessPiece):
    pass

class Pawn(ChessPiece):
    pass

class ChessPieceFactory:
    @staticmethod
    def get_piece(type, color, position):
        if type == 'K':
            return King(color, position)
        elif type == 'Q':
            return Queen(color, position)
        elif type == 'R1':  # Première tour
            return Rook(color, position)
        elif type == 'R2':  # Seconde tour
            return Rook(color, position)
        elif type == 'N1':  # Premier cavalier
            return Knight(color, position)
        elif type == 'N2':  # Second cavalier
            return Knight(color, position)
        elif type == 'B1':  # Premier fou
            return Bishop(color, position)
        elif type == 'B2':  # Second fou
            return Bishop(color, position)
        elif type == 'P':
            return Pawn(color, position)
        else:
            raise ValueError("Unknown piece type")
