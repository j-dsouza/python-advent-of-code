from typing import List

class Boarding:
    def __init__(self, boarding: str):
        self.row = int(boarding[:7].replace("F", "0").replace("B", "1"), 2)
        self.col = int(boarding[7:].replace("L", "0").replace("R", "1"), 2)

    def get_id(self) -> int:
        return self.row * 8 + self.col


def parse(filename: str) -> List[Boarding]:
    with open(filename, "r") as f:
        lines = f.readlines()

    boarding_passes = [Boarding(x) for x in lines]

    return boarding_passes


def pt_1(boarding_passes: List[Boarding]) -> int:
    return max([x.get_id() for x in boarding_passes])


def pt_2(boarding_passes: List[Boarding]) -> int:
    boarding_ids = [x.get_id() for x in boarding_passes]
    boarding_ids.sort()
    missing_next = [i for x, y in zip(boarding_ids, boarding_ids[1:])  
        for i in range(x + 1, y) if y - x > 1]
    return missing_next


def main():
    boarding_passes = parse("/home/jdsouza/github/python-advent-of-code/data/day_5.txt")

    pt1 = pt_1(boarding_passes)
    print(pt1)

    pt2 = pt_2(boarding_passes)
    print(pt2)


if __name__ == "__main__":
    main()