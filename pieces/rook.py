from config import ORTHOGONAL_DIRS
from pieces.base import Piece


class Rook(Piece):
    white_symbol = "♖"
    black_symbol = "♜"
    def  __init__(self, color: str):
        super().__init__(color)
        self.has_moved = False

    def on_move(self, from_pos, to_pos, board):
        self.has_moved = True

    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        answer = []
        for i in ORTHOGONAL_DIRS:
            r, c = row, col
            c += i[0]
            r += i[1]
            while board.is_inside(r, c):
                target = board.get_piece(r, c)
                if target is None:
                    answer.append((r, c))
                elif target.color != self.color:
                    answer.append((r, c))
                    break
                else:
                    break
                c += i[0]
                r += i[1]

        return answer

