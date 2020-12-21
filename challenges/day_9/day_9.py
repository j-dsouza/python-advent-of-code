from typing import List
from itertools import combinations, permutations


def parse(filename: str) -> List[int]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return [int(x) for x in lines]


def pt_1(nums: List[int], gap: int) -> int:
    for i in range(len(nums) - gap):
        lst = nums[i:i+gap]
        target = nums[i+gap]
        sums = combinations(lst, 2)
        sums = [sum(x) for x in sums]
        if target not in sums:
            return target


def pt_2(nums: List[int], target: int) -> int:
    max_pos = [i for i, x in enumerate(nums) if x == target][0]
    short_nums = nums[:max_pos]
    for i in range(max_pos):
        r = range(len(short_nums) - i)
        combinations = [short_nums[x:x+i] for x in r]
        for ls in combinations:
            tot = sum(ls)
            if tot == target:
                return (max(ls) + min(ls))


def main():
    nums = parse("/home/jdsouza/github/python-advent-of-code/data/day_9.txt")
    
    pt1 = pt_1(nums, 25)
    print(pt1)

    pt2 = pt_2(nums, pt1)
    print(pt2)


if __name__ == "__main__":
    main()