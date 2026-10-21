from pieces.base import Piece


class Knight(Piece):

    white_symbol = "♘"
    black_symbol = "♞"
    
    DELTAS = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
    ]

    def __init__(self, color):
        super().__init__(color)
    
    def on_move(
            self, from_pos: tuple[int, int], to_pos: tuple[int, int], board
        ) -> None:
        pass

    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        moves = []

        for dr, dc in self.DELTAS:
            r = row + dr
            c = col + dc

            if board.is_inside(r, c):     
                target = board.get_piece(r, c)
                
                if target == None or target.color != self.color:
                    moves.append((r, c))

        return moves