from typing import TypedDict
def get_num_words(text):
    words = text.split()
    count = len(words)
    return count
def each_character(text):
    each_chara: dict[str, int] = {}
    for i in text:
        i = i.lower()
        if i not in each_chara:
            each_chara[i] = 1
        else:
            each_chara[i] += 1
    return each_chara
class CharacterCount(TypedDict):
    char: str
    num: int
def sort_on(char_count: CharacterCount) -> int:
    return char_count["num"]
def sorted_char(each_character: dict[str, int]) -> list[CharacterCount]:
    sorted_list =[]
    for key, value in each_character.items():
        sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list