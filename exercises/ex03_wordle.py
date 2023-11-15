"""EX03 - Structured Wordle!"""
__author__ = "730596810"


def contains_char(searched_string: str, character: str) -> bool:
    """Test if character is found in word."""
    assert len(character) == 1
    index: int = 0
    while index < len(searched_string):
        if character == searched_string[index]:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Codify string with emojis."""
    assert len(guess) == len(secret)
    index: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    while index < len(secret):
        if contains_char(secret, guess[index]) is False:
            emoji += WHITE_BOX
        else:
            if secret[index] == guess[index]:
                emoji += GREEN_BOX
            else:
                emoji += YELLOW_BOX
        index += 1
    return emoji


def input_guess(expected_value: int) -> str:
    """Input for user to guess word."""
    guess: str = input(f"Enter a {expected_value} character word: ")
    while expected_value != len(guess):
        guess = input(f"That wasn't {expected_value} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 1
    secret_word: str = "codes"
    guess: str = input_guess(len(secret_word))

    while turn_count <= 6: 
        print(f"=== Turn {turn_count}/6 ===")
        print(emojified(guess, secret_word))
        
        if guess == secret_word:
            print(f"You won in {turn_count}/6 turns!")
        else:
            turn_count += 1

    if turn_count > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
