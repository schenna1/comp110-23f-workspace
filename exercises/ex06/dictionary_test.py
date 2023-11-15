"""Making unit tests for various functions."""
__author__ = "730596810"

# functions:


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts strings in a dictionary."""
    new_dict: dict[str, str] = {}

    for new_value in x:
        new_key: str = x[new_value]
        new_dict[new_key] = str(new_value)

    if len(x) != len(new_dict):
        raise KeyError("Uh Oh!")
    return (new_dict)


def favorite_color(x: dict[str, str]) -> str:
    """Returns the favorite (most frequent) color."""
    count_dict: dict[str, int] = {}
    fav_color: str = ""
    max_count: int = 0

    for name in x:
        color = x[name]
        if color in count_dict:
            count_dict[color] += 1
        else:
            count_dict[color] = 1

        if count_dict[color] > max_count:
            fav_color = color
            max_count = count_dict[color]

    return fav_color


def count(x: list[str]) -> dict[str, int]:
    """Produces a dictionary counting the frequency of integars in the provided list."""
    new_dict: dict[str, int] = {}
    for item in x:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return (new_dict)


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Organizes words based on the first letter, ignoring case."""
    new_dict: dict[str, list[str]] = {}

    for word in x:
        first_letter: str = word[0].lower()

        if first_letter not in new_dict:
            word_list: list[str] = []
            word_list.append(word)
            new_dict[first_letter] = word_list
        else:
            new_dict[first_letter].append(word)

    return new_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance log when provided name and day of attendance."""
    if day in attendance_log:
        if student not in attendance_log[day]: 
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return attendance_log


# Unit tests for invert


def test_two_pairs() -> None:
    """Dictionary returning 2 and 3 as keys for 1 and 2 values respectively."""
    inp_dict: dict[str, str] = {"1": "2", "2": "3"}
    expected_result: dict[str, str] = {"2": "1", "3": "2"}
    assert invert(inp_dict) == expected_result


def test_when_key_value_same() -> None:
    """Dictionary returning 1 2 and 3 for keys and 2 3 and 3 for values respectively."""
    inp_dict: dict[str, str] = {"1": "2", "2": "3", "4": "4"}
    expected_result: dict[str, str] = {"2": "1", "3": "2", "4": "4"}
    assert invert(inp_dict) == expected_result


def test_empty_dict() -> None:
    """Returns empty dict."""
    inp_dict: dict[str, str] = {}
    expected_result: dict[str, str] = {}
    assert invert(inp_dict) == expected_result


# Unit tests for favorite_color


def test_fav_color_blue() -> None:
    """Returns favorite color blue."""
    inp_dict: dict[str, str] = {"Joe": "blue", "Mary": "red", "Barry": "blue"}
    expected_result: str = "blue"
    assert favorite_color(inp_dict) == expected_result


def test_one_color() -> None:
    """Returns favorite, and only, color blue."""
    inp_dict: dict[str, str] = {"Joe": "blue", "Mary": "blue", "Barry": "blue"}
    expected_result: str = "blue"
    assert favorite_color(inp_dict) == expected_result


def test_fav_empty() -> None:
    """Returns empty string from empty dict."""
    inp_dict: dict[str, str] = {}
    expected_result: str = ""
    assert favorite_color(inp_dict) == expected_result

# Unit tests for count


def test_3_item_list() -> None:
    """Returns hello value 2 and bye value 1."""
    new_list: list[str] = ["hello", "bye", "hello"]
    expected_result: dict[str, int] = {"hello": 2, "bye": 1}
    assert count(new_list) == expected_result


def test_same_count() -> None:
    """Returns hello value 2 and bye value 2."""
    new_list: list[str] = ["hello", "bye", "bye", "hello"]
    expected_result: dict[str, int] = {"hello": 2, "bye": 2}
    assert count(new_list) == expected_result


def test_empty_list() -> None:
    """Returns empty dict from empty list."""
    new_list: list[str] = []
    expected_result: dict[str, int] = {}
    assert count(new_list) == expected_result

# Unit tests for alphabetizer


def test_3_items() -> None:
    """Returns 'apple' and 'and' under 'a' and 'blue' under 'b'."""
    inp_list: list[str] = ["Apple", "and", "blue"]
    expected_result: dict[str, list[str]] = {"a": ["Apple", "and"], "b": ["blue"]}
    assert alphabetizer(inp_list) == expected_result


def test_same_key() -> None:
    """Returns 'apple', 'and', and 'agree' under 'a'."""
    inp_list: list[str] = ["apple", "and", "agree"]
    expected_result: dict[str, list[str]] = {"a": ["apple", "and", "agree"]}
    assert alphabetizer(inp_list) == expected_result


def test_empty() -> None:
    """Returns empty dict'."""
    inp_list: list[str] = []
    expected_result: dict[str, list[str]] = {}
    assert alphabetizer(inp_list) == expected_result

# Unit tests for update_attendance


def test_add_student() -> None:
    """Add 'becca' to 'tues'. Returns 'james, 'ellie' and 'becca' present on 'mon' and 'tues'."""
    inp_log: dict[str, list[str]] = {"mon": ["james", "ellie", "becca"], "tues": ["james", "ellie"]}
    inp_day: str = "tues"
    inp_student: str = "becca"
    expected_result: dict[str, list[str]] = {"mon": ["james", "ellie", "becca"], "tues": ["james", "ellie", "becca"]}
    assert update_attendance(inp_log, inp_day, inp_student) == expected_result


def test_no_repeat() -> None:
    """Add 'tues' and 'james' present to log."""
    inp_log: dict[str, list[str]] = {"mon": ["james", "ellie", "becca"]}
    inp_day: str = "tues"
    inp_student: str = "james"
    expected_result: dict[str, list[str]] = {"mon": ["james", "ellie", "becca"], "tues": ["james"]}
    assert update_attendance(inp_log, inp_day, inp_student) == expected_result


def test_no_change() -> None:
    """Returns same dictionary as dictionary in argument."""
    inp_log: dict[str, list[str]] = {"mon": ["james", "ellie", "becca"], "tues": ["james", "ellie", "becca"]}
    inp_day: str = ""
    inp_student: str = ""
    expected_result: dict[str, list[str]] = {"mon": ["james", "ellie", "becca"], "tues": ["james", "ellie", "becca"]}
    assert update_attendance(inp_log, inp_day, inp_student) == expected_result