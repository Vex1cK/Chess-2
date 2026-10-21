from pieces.piece import Piece

class Kangaroo(Piece):
    DIRECTIONS = [
        (-1,-1), (-1, 0), (-1,1),
        (0, -1),        (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]
    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        moves = []
        for dr, dc in self.DIRECTIONS:
            r1,c1 = row + dr, col + dc
            if self._can_land(board, r1, c1):
                moves.append((r1, c1))
                r2,c2 = row + 2 * dr, col + 2 * dc
                if self._can_land(board, r2, c2):
                    moves.append((r2, c2))
        return moves
    def on_move(self,from_pos: tuple[int, int], to_pos: tuple[int, int]):
       return None
    def _can_land(self, board, r1, c1):
        if not board.is_inside(r1, c1):
            return False
        target = board.get_piece(r1, c1)
        if target is None:
            return False
