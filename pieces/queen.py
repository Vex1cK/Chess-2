from pieces.base import Piece
from config import ALL_DIRS

class Queen(Piece):
    white_symbol = "♕"
    black_symbol = "♛"
    def __init__(self, color: str):
        super().__init__(color)
    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        answer = []
        for x1, y1 in ALL_DIRS:
            x, y = row, col
            while board.is_inside(x - x1, y - y1) and not board.get_piece(x - x1, y - y1):
                answer.append((x - x1, y - y1))
                x -= x1
                y -= y1
        return answer
    def on_move(self, from_pos: tuple[int, int], to_pos: tuple[int, int], board) -> None:
        pass
    