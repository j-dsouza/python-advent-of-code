from typing import List


def parse(filename: str) -> List[List[str]]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return [list(x) for x in lines]


def pt_1(seating):
    running = True
    while running:
        



def main():
    seating = parse("/home/jdsouza/github/python-advent-of-code/data/day_11_tst.txt")


if __name__ == "__main__":
    main()