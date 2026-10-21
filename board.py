from config import BLACK, BOARD_SIZE, WHITE
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
import copy

class Board:
    def __init__(self, setup=True):
        self.grid = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.history = []
        if setup:
            self.setup_board()

    def is_inside(self, row: int, col: int) -> bool:
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

    def get_piece(self, row: int, col: int):
        if self.is_inside(row, col):
            return self.grid[row][col]
        return None

    def set_piece(self, row: int, col: int, piece) -> None:
        if self.is_inside(row, col):
            self.grid[row][col] = piece

    def setup_board(self) -> None:
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        
        for col in range(BOARD_SIZE):
            piece_class = back_row[col]
            self.grid[0][col] = piece_class(BLACK)
            self.grid[1][col] = Pawn(BLACK)
        
        for col in range(BOARD_SIZE):
            self.grid[6][col] = Pawn(WHITE)
            piece_class = back_row[col]
            self.grid[7][col] = piece_class(WHITE)
            
    def make_move(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
        fr, fc = from_pos
        tr, tc = to_pos

        piece = self.get_piece(fr, fc)
        captured_piece = self.get_piece(tr, tc)

        self.set_piece(fr, fc, None)
        self.set_piece(tr, tc, piece)

        self.history.append({
            "piece": piece,
            "from": from_pos,
            "to": to_pos,
            "captured": captured_piece
        })

        if piece is not None:
            piece.on_move(from_pos, to_pos, self)

    def clone(self) -> "Board":
        new_board = Board(setup=False)

        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece is not None:
                    new_board.grid[r][c] = piece.copy()

        new_board.history = list(self.history)
        return new_board

