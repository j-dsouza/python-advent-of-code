from typing import List
import string

def parse(filename) -> List[str]:
    with open(filename, "r") as f:
        lines = f.read().split("\n\n")
    
    groups = [x.replace("\n", "") for x in lines]
    return groups


def parse_2(filename) -> List[str]:
    with open(filename, "r") as f:
        lines = f.read().split("\n\n")
    
    people = [x.split("\n") for x in lines]
    return people


def pt_1(groups: List[List[str]]) -> int:
    group_sets = [set(x) for x in groups]
    return sum(len(x) for x in group_sets)


def pt_2(people: List[List[str]]) -> int:
    # import pdb; pdb.set_trace()
    sums = 0
    for person in people:
        corr = set(person[0])
        for x in person[1:]:
            corr &= set(x)
        sums += len(corr)

    return sums


def main():
    groups = parse("/home/jdsouza/github/python-advent-of-code/data/day_6.txt")

    pt1 = pt_1(groups)
    print(pt1)

    people = parse_2("/home/jdsouza/github/python-advent-of-code/data/day_6.txt")
    pt2 = pt_2(people)
    print(pt2)


if __name__ == "__main__":
    main()