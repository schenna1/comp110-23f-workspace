""""EX01 - Chardle _ A cute step toward Wordle."""
__author__ = "730956810"


character_word_5: str = input("Enter a 5-character word: ")
if len(character_word_5) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")  
    exit()

matchingcharacter: int = 0
print("Searching for " + single_character + " in " +character_word_5)


if single_character == character_word_5[0]:
    print(single_character + " found at index 0")
    matchingcharacter = (matchingcharacter + 1)
if single_character == character_word_5[1]:
    print(single_character + " found at index 1")
    matchingcharacter = matchingcharacter + 1
if single_character == character_word_5[2]:
    print(single_character + " found at index 2")
    matchingcharacter = matchingcharacter +1
if single_character == character_word_5[3]:
    print(single_character + " found at index 3")
    matchingcharacter = matchingcharacter+1
if single_character == character_word_5[4]:
    print(single_character + " found at index 4")
    matchingcharacter=matchingcharacter+1
if matchingcharacter==0:
    print("No instances of " +single_character+ " found in " + character_word_5)
if matchingcharacter != 0:
    print(str(matchingcharacter) + " instance of " + single_character + " found in " + character_word_5 )

     
    
