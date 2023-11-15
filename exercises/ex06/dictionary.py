"""EX06 - Practicing functions with Dictionary."""
__author__ = "730956810"


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
    """Organizes words based on first letter."""
    new_dict: dict[str, list[str]] = {}
    for words in x:
        letter: str = words[0]
        if letter not in new_dict:
            word_list: list[str] = []
            word_list.append(words)
            new_dict[letter.lower()] = word_list
        else:
            new_dict[letter.lower()].append(words)
    return (new_dict)


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance log when provided name and day of attendance."""
    if day in attendance_log:
        attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]  
    return attendance_log