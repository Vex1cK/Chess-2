from config import WHITE
from pieces.base import Piece
from pieces.queen import Queen


class Pawn(Piece):
    white_symbol = "♙"
    black_symbol = "♟"

    def get_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        moves: list[tuple[int, int]] = []

        if self.color == WHITE:
            direction, start_row = -1, 6
        else:
            direction, start_row = 1, 1

        next_row = row + direction
        if board.is_inside(next_row, col) and board.get_piece(next_row, col) is None:
            moves.append((next_row, col))

            if row == start_row and board.get_piece(row + 2 * direction, col) is None:
                moves.append((row + 2 * direction, col))

        for dc in (-1, 1):
            r, c = row + direction, col + dc
            if board.is_inside(r, c):
                target = board.get_piece(r, c)
                if target is not None and target.color != self.color:
                    moves.append((r, c))

        if board.history:
            last = board.history[-1]
            if (
                isinstance(last["piece"], Pawn)
                and last["piece"].color != self.color
                and abs(last["from"][0] - last["to"][0]) == 2
                and last["to"][0] == row
                and abs(last["to"][1] - col) == 1
            ):
                moves.append((row + direction, last["to"][1]))

        return moves

    def on_move(
        self, from_pos: tuple[int, int], to_pos: tuple[int, int], board
    ) -> None:
        fr, fc = from_pos
        tr, tc = to_pos

        if fc != tc and board.history and board.history[-1]["captured"] is None:
            board.set_piece(fr, tc, None)

        if tr == 0 or tr == 7:
            board.set_piece(tr, tc, Queen(self.color))
