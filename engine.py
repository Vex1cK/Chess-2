from config import WHITE, BLACK, BOARD_SIZE

class Engine:

    # Ищет короля цвета color и возвращает его координаты, иначе вернет -1 -1
    def find_king(self, board, color: str) -> tuple[int, int] | None:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                piece = board.get_piece(i, j)
                if piece.color == color and piece.is_king == True:
                    return tuple(i, j)
        return tuple(-1, -1)

    # проверяет король под шахом или нет
    def is_in_check(self, board, color: str) -> bool:
        i_king, j_king = self.find_king(board, color)
        if i_king == -1:
            return False
        
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                piece = board.get_piece(i, j)
                if piece.color != color and tuple(i_king, j_king) in piece.get_moves(i, j, board):
                    return True
        return False

    # возвращает легальные ходы фигуры, которые не ставят короля под шах
    def get_legal_moves(self, board, row: int, col: int) -> list[tuple[int, int]]:
        piece = board.get_piece(row, col)
        if piece == None:
            return []
        raw_moves = piece.get_moves(row, col, board)
        legal_moves = []
        for i, j in raw_moves:
            sim_board = board.clone()
            sim_board.make_move((row, col), (i, j))
            if not self.is_in_check(sim_board, piece.color):
                legal_moves.append(tuple(i, j))
        return legal_moves

    # проверяет есть ли хотя бы один легальный код
    def has_any_legal_moves(self, board, color: str) -> bool:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                piece = board.get_piece(i, j)
                if piece == None or piece.color != color:
                    continue
                if self.get_legal_moves(board, i, j) == []:
                    continue
                return True
        return False

    # возвращает статус игры
    def get_game_status(self, board, current_color: str) -> str:
        has_moves = self.has_any_legal_moves(board, current_color)
        in_check = self.is_in_check(board, current_color)

        if not has_moves and in_check:
            return "checkmate"

        if not has_moves and not in_check:
            return "stalemate"

        if in_check:
            return "check"

        return "ongoing"