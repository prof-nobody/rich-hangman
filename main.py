from rich import print
from rich.panel import Panel
from random import randint
from rich import box
from rich.live import Live
from rich.layout import Layout


def get_word_list():
    with open('word_list.txt') as file:
        word_list = file.read()
    word_list = word_list.split()
    word_list = list(set(word_list))
    word_list.sort()
    return word_list


def pick_word(word_list):
    word_picked = word_list[randint(1, len(word_list))]
    return word_picked


def update_board() -> Panel:
    game_panel = Panel(f"{word}\n\n{''.join(answer)}\n\nSTRIKES\n{'#' * strikes}",
                       border_style=bs, title="hangman", height=5, width=50)
    return game_panel


words = get_word_list()
word = pick_word(words)
word = word.lower()
word_len = len(word)
print(word)
answer = "_ " * len(word)
answer = answer.split()
strikes = 0
max_strikes = 6
bs = "green"
layout = Layout()
layout.split_column(
    Layout(update_board(),
           name="upper"
           ),
    Layout(name="lower")
)
layout['upper'].size = 5
layout['lower'].size = 4

with Live(layout, auto_refresh=False) as live:
    while True:
        live.update(layout['upper'])
        letter = input("Letter: ").lower()

        if letter in word:
            location = 0
            while True:
                location = word.find(letter, location)
                if location != -1:
                    answer[location] = letter
                    print(location)
                    location += 1
                elif location == -1:
                    break
            if word == "".join(answer):
                print("VICTORY!")
                break
        else:
            strikes += 1
            if strikes == 3:
                bs = "yellow"
            elif strikes == 5:
                bs = "red"
            elif strikes == 6:
                print("Game Over")
                break

