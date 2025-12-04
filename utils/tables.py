from typing import TypeVar

T = TypeVar("T")


def pad(matrix: list[list[T]], pad_amount: int, pad_char: str):
    """Pad around matrix with pad_amount of pad_char."""
    rows = [pad_char for _ in range(len(matrix[0]) + 2 * pad_amount)]
    cols = [pad_char for _ in range(pad_amount)]
    return (
        [rows[:] for _ in range(pad_amount)]
        + [cols[:] + matrix_row + cols[:] for matrix_row in matrix]
        + [rows[:] for _ in range(pad_amount)]
    )
