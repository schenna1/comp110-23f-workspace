def short_words(x: list[str]) -> list[str]:
    i: int = 0
    list: list[str] = [""]
    while i < len(list):
        if len(list[i]) < 5:
            list.append(list[i])
            i += 1
        else:
            print(f"{list[i]} is too long!")
    print(list)

short_words(["sun", "cloud", "sky"])