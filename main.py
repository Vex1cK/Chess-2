from config import BLACK, WHITE
from board import Board
from engine import Engine
from ui import render_board,parse_board

def main():
    board = Board()
    engine = Engine()
    current_color = WHITE

    print("Добро пожаловать в шахматы")
    print("Вводите ход как 'e2 e4'. Для выхода введите 'exit")

    while True:
        render_board(board)
        status = engine.get_game_status(board, current_color)
        if status == "checkmate":
            if current_color == WHITE:
                print("Мат! Победили белые")
            else:
                print("Мат! Победили черные")
            break

        if status == "stalemate":
            print("Пат! Ничья")
            break

        if status == "check":
            print("Шах!")

        if current_color == WHITE:
            print("Ходят белые")
        else:
            print("Ходят черные")

        text = input("твой ход:")
        if text == "exit":
            print("Пока!")
            break


        move = parse_move(text)
        if move == None:
            print("Повторите ввод")
            continue

        from_pos = move[0]
        to_pos = move[1]
        from_row = from_pos[0]
        from_col = from_pos[1]


        piece = board.get_piece(from_row, from_col)
        if piece == None:
            print("Пусто")
            continue

        if piece.color != current_color:
            print("Это не твоя фигура")
            continue



        legal_moves = engine.get_legal_moves(board, from_row, from_pos)
        if to_pos not in legal_moves:
            print("Так ходить нельзя!")
            continue


        board.make_move(from_pos, to_pos)

        if current_color == WHITE:
            current_color = BLACK
        else:
            current_color = WHITE



if __name__ == "__main__":
    main()





