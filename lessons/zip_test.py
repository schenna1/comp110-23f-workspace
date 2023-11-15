"""Test my zip function."""
__author__ = "730956810"

from lessons.zip import zip


def test_one_word() -> None:
    """First word returning index 1 in a one item list."""
    words: list[str] = ["apple"]
    integers: list[int] = [1]
    expected_result: dict[str, int] = {"apple": 1}
    assert zip(words, integers) == expected_result


def test_multiple_words() -> None:
    """Returns a dict with words at index in a 3 item list."""
    words: list[str] = ["apple", "banana", "grape"]
    integers: list[int] = [1, 2, 3]
    expected_result: dict[str, int] = {"apple": 1, "banana": 2, "grape": 3}
    assert zip(words, integers) == expected_result


def test_empty_list() -> None:
    """Returns empty dict when lists are empty."""
    words: list[str] = [""]
    integers: list[int] = []
    expected_result: dict = {}
    assert zip(words, integers) == expected_result