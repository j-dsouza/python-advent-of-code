from typing import List
from collections import defaultdict


def parse(filename: str) -> List[int]:
    with open(filename, "r") as f:
        lines = [int(x) for x in f.readlines()]
        
    lines.sort()

    return lines


def pt_1(adaptors: List[int]) -> int:
    gap_1 = 0
    gap_3 = 0

    if adaptors[0] == 1:
        gap_1 += 1
    elif adaptors[0] == 3:
        gap_3 += 1

    for prev, curr in zip(adaptors, adaptors[1:]):
        if curr - prev == 1:
            gap_1 += 1
        elif curr - prev == 3:
            gap_3 += 1

    gap_3 += 1

    return gap_1 * gap_3


def pt_2(adaptors: List[int]) -> int:
    counts = defaultdict(int, {0: 1})

    for x in adaptors:
        counts[x] = counts[x - 3] + counts[x - 2] + counts[x - 1]

    return counts[adaptors[-1]]


def main():
    adaptors = parse("/home/jdsouza/github/python-advent-of-code/data/day_10.txt")
    
    pt1 = pt_1(adaptors)
    print(pt1)
    
    pt2 = pt_2(adaptors)
    print(pt2)


if __name__ == "__main__":
    main()