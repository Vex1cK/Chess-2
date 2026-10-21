from config import ALL_DIRS
from pieces.base import Piece
from pieces.rook import Rook

class King(Piece):
    white_symbol = "♔"
    black_symbol = "♚"
    is_king = True

    # === ЗОНА ИГРОКА А (__init__ и get_moves) ===

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
