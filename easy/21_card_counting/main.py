# https://www.codingame.com/ide/puzzle/card-counting-when-easily-distracted

# K Q J T all have a value of 10
# calculate the percentageChance (rounded to the nearest whole number) that the value of the next card will be less than the bustThreshold.


# Travailler avec des valeur Hexa pour les cartes ?

# verifier si chaque element de Serie ne comporte que des cartes
# Si c'est pas le cas supprimer l'élément en question
# On a alors que des cartes dans des series
# Compter les cartes dont la valeur est < à treshold
# En déduire le nombre de ces cartes dans le tas restant
# Diviser ce nombre par le nombre total de cartes restantes
# Arrondir et afficher x%


# -----------------------------------------------------------------------------
RedirectIOtoFile = True
if RedirectIOtoFile:
    import sys
    import os
    from pathlib import Path

    k_input = "input.txt"
    os.chdir(Path(__file__).parent)
    sys.stdin = open(k_input, "r")

# # -----------------------------------------------------------------------------
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import time
# start_time = time.perf_counter()
# end_time = time.perf_counter()
# print(f"Execution time: {(end_time - start_time) * 1_000_000 :.2f} µs")


# -----------------------------------------------------------------------------
from collections import Counter

k_CardPerValue = 4
k_DeckSize = 52
set_cards = set("23456789TJQKA")


def count_remaining_below(list, val_max):
    letter_count = Counter(list)
    n = 0  # Count cards value from 1 to val_max
    [n := n + k_CardPerValue - letter_count.get(str(key), 0) for key in range(1, val_max)]
    return n


str_in = input()
threshold = int(input())  # 2<=threshold<=10
batches = str_in.split(".")

for batch in batches[:]:  # work on a copy of the list
    batch_as_set = set(batch)
    if not batch_as_set.issubset(set_cards):
        batches.remove(batch)

observed_cards = "".join(s for s in batches)
nb_remaining_cards = k_DeckSize - len(observed_cards)
observed_cards = (  # we will count value<10 we can remove them to speed up count_below()
    observed_cards.replace("A", "1").replace("T", "").replace("J", "").replace("Q", "").replace("K", "")
)

n = count_remaining_below(observed_cards, threshold)  # compter les cartes restantes dont la valeur est < threshold
print(f"{round(100*n/nb_remaining_cards)}%")


# # -----------------------------------------------------------------------------
# k_CardPerValue = 4
# k_DeckSize = 52


# def count_remaining_below(list, val_max):
#     """Count the number of cards whose value is below val_max in (Deck - list) set of cards"""
#     letter_count = {}

#     for char in list:
#         if char in letter_count:
#             letter_count[char] += 1
#         else:
#             letter_count[char] = 1
#     n = 0
#     for key, value in letter_count.items():
#         # key = "10" if key == "A" else key
#         if int(key) < val_max:
#             n += k_CardPerValue - value  # if we observed 3 times the card, we have 1 left
#         # else:
#         #     break
#     return n


# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
# set_cards = set(cards)
# str_in = input()
# threshold = int(input())  # 2<=threshold<=10
# series = str_in.split(".")

# for serie in series[:]:  # work on a copy of the list
#     set_serie = set(serie)
#     if not set_serie.issubset(set_cards):
#         series.remove(serie)

# observed_cards = "".join(s for s in series)
# nb_observed_cards = len(observed_cards)
# nb_remaining_cards = 52 - len(observed_cards)
# observed_cards = (
#     # remove the cards we will not count
#     # even if threshold=10, we will count card<10 we can remove them to speed up count_below()
#     observed_cards.replace("A", "1")
#     .replace("T", "")
#     .replace("J", "")
#     .replace("Q", "")
#     .replace("K", "")
# )
# # observed_cards = list(observed_cards)
# # observed_cards.sort()

# # compter les cartes restantes dont la valeur est < threshold
# n = count_remaining_below(observed_cards, threshold)
# # countif(set_serie, threshold)
# print(f"{round(100*n/nb_remaining_cards)}%")


# # -----------------------------------------------------------------------------
# k_CardPerValue = 4
# k_DeckSize = 52


# def count_below(list, val_max):
#     letter_count = {}

#     for char in list:
#         if char in letter_count:
#             letter_count[char] += 1
#         else:
#             letter_count[char] = 1
#     n = 0
#     for key, value in letter_count.items():
#         key = "10" if key == "A" else key
#         if int(key) < val_max:
#             n += k_CardPerValue - value  # if we observed 3 times the card, we have 1 left
#         # else:
#         #     break
#     return n


# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
# set_cards = set(cards)
# str_in = input()
# threshold = int(input())  # 2<=threshold<=10
# series = str_in.split(".")

# for serie in series[:]:  # work on a copy of the list
#     set_serie = set(serie)
#     if not set_serie.issubset(set_cards):
#         series.remove(serie)

# observed_cards = "".join(s for s in series)
# nb_remaining_cards = 52 - len(observed_cards)
# observed_cards = (
#     # remove the cards we will not count
#     observed_cards.replace("A", "1")
#     .replace("T", "")
#     .replace("J", "")
#     .replace("Q", "")
#     .replace("K", "")
# )
# # observed_cards = list(observed_cards)
# # observed_cards.sort()

# # compter les cartes dont la valeur est < threshold
# n = count_below(observed_cards, threshold)
# # countif(set_serie, threshold)
# print(f"{round(100*n/nb_remaining_cards)}%")


# -----------------------------------------------------------------------------
if RedirectIOtoFile:
    sys.stdin.close()


"""
"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"

9J4T7A55Q.Something just touched my leg!.9T75.RainMan.Cute dealer.Is that Penn or Teller?.TATA.A.I'm so smart.366K9.362436
9J4T7A55Q.Something just touched my leg!.9T75.RainMan.Cute dealer.Is that Penn or Teller?.TATA.A.I'm so smart.366K9.362436

9J4T7A55Q.
Something just touched my leg!.
9T75.
RainMan.
Cute dealer.
Is that Penn or Teller?.
TATA.
A.
I'm so smart.
366K9.
362436


9J4T7A55Q
9T75
TATA
A
366K9
362436


9J4T7A55Q9T75TATAA366K9362436

9471559751113669362436


1   4
2   1
3   3
4   2
5   3
6   4
7   2
8   0
9   3



"""
