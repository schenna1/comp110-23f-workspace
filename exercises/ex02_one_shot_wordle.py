"""EX02 - One Shot Wordle."""
__author__ = "730956810"

secret: str = "python"
count: int = len(secret)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# asks user for input
question: str = input(f"What is your {count}-letter guess? ")
while len(question) != count:
    question = input(f"That was not {count} letters! Try again: ")

index: int = 0
emoji: str = ""

# checking indexes
while index < len(secret):
    if secret[index] == question[index]:
        emoji = emoji + GREEN_BOX    
    else:
        exists: bool = False
        exists_index: int = 0

        while exists is False and exists_index < len(secret):
            if question[index] == secret[exists_index]:
                exists = True
            else:
                exists_index += 1
        if exists is not False:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index += 1
print(emoji)

# providing user feedback
if len(question) == count and question == secret:
    print("Woo! You got it!")
elif len(question) == count and question != secret:
    print("Not quite. Play again soon!")
