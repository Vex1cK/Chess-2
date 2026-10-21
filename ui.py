from config import FILES, RANKS


def square_name(pos: tuple[int, int]) -> str:
    row, col = pos
    return FILES[col] + RANKS[row]


def render_board(board) -> None:
    letters = "  " + " ".join(FILES)
    print(letters)

    for row in range(8):
        cells = []
        for col in range(8):
            piece = board.get_piece(row, col)
            if piece is None:
                cells.append("·")
            else:
                cells.append(str(piece))
        print(8 - row, " ".join(cells), 8 - row)

    print(letters)

    history = getattr(board, "history", None)
    if history:
        print("Последний ход:", describe_move(history[-1]))


def describe_move(move: dict) -> str:
    start = move.get("from", move.get("from_pos"))
    end = move.get("to", move.get("to_pos"))
    if start is None or end is None:
        return str(move)

    text = square_name(start) + "-" + square_name(end)
    piece = move.get("piece")
    if piece is not None:
        text = str(piece) + " " + text
    return text


def parse_square(word: str) -> tuple[int, int] | None:
    if len(word) != 2:
        return None

    letter, digit = word[0], word[1]
    if letter not in FILES or digit not in RANKS:
        return None

    row = RANKS.index(digit)
    col = FILES.index(letter)
    return row, col


def parse_move(text: str) -> tuple[tuple[int, int], tuple[int, int]] | None:
    text = text.strip().lower().replace("-", " ")
    words = text.split()

    if len(words) != 2:
        return None

    start = parse_square(words[0])
    end = parse_square(words[1])
    if start is None or end is None:
        return None

    return start, end

