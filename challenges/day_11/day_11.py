from typing import List
import copy
from itertools import chain, repeat
from collections import Counter


def parse(filename: str) -> List[List[str]]:
    with open(filename, "r") as f:
        lines = f.readlines()

    seating = [list(x.replace("\n", "")) for x in lines]
    pad_token = "."
    
    seating_padded = [pad(x, pad_token) for x in seating]
    seating_padded = pad(seating_padded, [pad_token] * len(seating_padded[0]))

    return seating_padded


def pad(iterable, pad_token):
    return list(chain(repeat(pad_token, 1), iterable, repeat(pad_token, 1)))


def pt_1(seating):
    running = True
    
    x_range = [-1, 0, 1]
    y_range = [-1, 0, 1]

    while running:
        seating_copy = copy.deepcopy(seating)

        for y, row in enumerate(seating_copy[1: -1]):
            y += 1
            for x, seat in enumerate(row[1: -1]):
                count_occupied = 0
                x += 1
                for yr in y_range:
                    for xr in x_range:
                        if yr != 0 or xr != 0:
                            seat_look = seating_copy[y + yr][x + xr]
                            if seat_look == "#":
                                count_occupied += 1
                
                if seat == ".":
                    seating[y][x] = "."
                elif seat == "L" and count_occupied == 0:
                    seating[y][x] = "#"
                elif seat == "#" and count_occupied >= 4:
                    seating[y][x] = "L"

        if seating == seating_copy:
            running = False

    return Counter([y for x in seating for y in x])


def main():
    seating = parse("/home/jdsouza/github/python-advent-of-code/data/day_11.txt")
    pt1 = pt_1(seating)
    print(pt1["#"])


if __name__ == "__main__":
    main()