from config import DIAGONAL_DIRS
from pieces.base import Piece


class Bishop(Piece):
    white_symbol = "♗"
    black_symbol = "♝"

    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        answer = []
        for i in DIAGONAL_DIRS:
            r, c = row, col
            cnt = 1
            c += i[0]
            r += i[1]
            while board.is_inside(r, c):
                target = board.get_piece(r, c)
                if target is None:
                    answer.append((r, c))
                elif target.color != self.color:
                    board.append((r, c))
                    break
                else:
                    break
                c += i[0] * cnt
                r += i[1] * cnt
                cnt += 1

        return answer
