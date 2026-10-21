from config import ALL_DIRS
from pieces.base import Piece
from pieces.rook import Rook

class King(Piece):
    white_symbol = "♔"
    black_symbol = "♚"
    is_king = True

    # === ЗОНА ИГРОКА А (__init__ и get_moves) ===
    def __init__(self, color: str):
        super().__init__(color)
        self.has_moved = False

    def get_moves(self, row: int, col: int, board):
        rez: list[tuple[int, int]] = []
        for r,c in ALL_DIRS:
            r += row
            c += col
            if not board.is_inside (r, c):
                continue
            p = board.get_piece(r, c)
            if p is not None and p.color == self.color:
                continue
            rez.append((r, c))

        if self.has_moved:
            return rez

        if board.get_piece(row, col + 1) is None and board.get_piece(row, col + 2) is None:
            r = board.get_piece(row, 7)
            if r is not None and isinstanse(r, Rook) and not rook.has_moved and rook.color == self.color:
                rez.append((r, col + 2))

        if board.get_piece(row, col - 1) is None and board.get_piece(row, col - 2) is None and board.get_piece(row, col - 3) is None:
            r = board.get_piece(row, 0)
            if r is not None and isinstanse(r, Rook) and not rook.has_moved and rook.color == self.color:
                rez.append((r, col - 2))
        return rez

    # === ЗОНА ИГРОКА Б (on_move) ===
    
    def on_move(
        self, 
        from_pos: tuple[int, int], 
        to_pos: tuple[int, int], 
        board,
    ) -> None:
        fr, fc = from_pos
        _, tc = to_pos

        self.has_moved = True
        if tc - fc == 2:
            rook = board.get_piece(fr, 7)
            board.set_piece(fr, 7, None)
            rook.has_moved = True
            board.set_piece(fr, 5, rook)
        elif tc - fc == -2:
            rook = board.get_piece(fr, 0)
            board.set_piece(fr, 0, None)
            rook.has_moved = True
            board.set_piece(fr, 3)
