from dataclasses import dataclass
import numpy as np


# @dataclass
# class Map:

def parse_map(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    map_tmp = []

    for line in lines:
        map_tmp.append(list(line.rstrip()))

    map = []

    for line in map_tmp:
        map.append([0 if x == '.' else 1 for x in line])

    return map


def pt_1(map: list, right: int) -> int:
    trees = 0
    width = len(map[0])
    x = 0

    for row in map:
        if row[x] == 1:
            trees += 1
        x = (x + right) % width
    
    return trees


def pt_2(map: list, down: int, right: int) -> int:
    trees = 0
    width = len(map[0])
    x = 0
    y = 0

    for row in map:
        if row[x] == 1 and y % down != 1:
            trees += 1
            print(y, x)
        if y % down != 1:
            x = (x + right) % width
        y += 1
    print('end')

    return trees
    

def main():
    filename = "/home/jdsouza/github/python-advent-of-code/data/day_3.txt"

    map = parse_map(filename)

    pt1 = pt_1(map, 3)
    print(pt1)

    pt2_tests = (
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    )

    pt2_tests_answers = []
    
    for test in pt2_tests:
        pt2_tests_answers.append(pt_2(map, test[0], test[1]))
    
    print(pt2_tests_answers)
    pt2 = np.prod(pt2_tests_answers)
    print(pt2)



if __name__ == "__main__":
    main()