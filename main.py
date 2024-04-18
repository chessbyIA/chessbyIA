from core.chess_core.game_engine import GameEngine

def main():
    game = GameEngine()

    print("État initial du plateau:")
    for row in game.chess_board.board:
        print(row)

    print("\nPions avancent:")
    game.move_piece((6, 4), (4, 4)) 
    game.move_piece((1, 4), (3, 4))

    print("\nÉtat du plateau après mouvement des pions:")
    for row in game.chess_board.board:
        print(row)

    print("\nMouvement du cavalier blanc:")
    game.move_piece((7, 6), (5, 5)) 

    print("\nÉtat du plateau après mouvement du cavalier:")
    for row in game.chess_board.board:
        print(row)

    print("\nCapture par la reine blanche:")
    game.move_piece((7, 3), (3, 7))

    print("\nÉtat final du plateau après la capture par la reine:")
    for row in game.chess_board.board:
        print(row)

if __name__ == "__main__":
    main()