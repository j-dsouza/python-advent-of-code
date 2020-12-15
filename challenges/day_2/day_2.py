from dataclasses import dataclass
import re
from typing import List

@dataclass
class Policy:
    low: int
    high: int
    letter: str
    password: str


def parse_policies(filename: str) -> List[Policy]:
    fields = [
        "low",
        "high",
        "letter",
        "password"
    ]

    with open(filename, "r") as f:
        lines = f.readlines()

    policies = []

    for line in lines:
        low = int(re.findall(r"\d{1,}", line)[0])
        high = int(re.findall(r"\d{1,}", line)[1])
        letter = re.findall("[a-z]", line)[0]
        password = re.findall("[a-z]{2,}", line)[0]

        policies.append(Policy(low, high, letter, password))

    return policies


def part_1(policy: Policy) -> int:
    return (
        (policy.password.count(policy.letter) >= policy.low) and
        (policy.password.count(policy.letter) <= policy.high)
    )


def part_2(policy: Policy) -> int:
    return (
        (
            (policy.password[policy.low - 1] == policy.letter) and
            (policy.password[policy.high - 1] != policy.letter)
        ) or (
            (policy.password[policy.low - 1] != policy.letter) and
            (policy.password[policy.high - 1] == policy.letter)
        )
    )


def main():
    filename = "/home/jdsouza/github/python-advent-of-code/data/day_2.txt"

    policies = parse_policies(filename)

    pt1 = 0
    pt2 = 0

    for policy in policies:
        pt1 += part_1(policy)
        pt2 += part_2(policy)

    print(pt1)
    print(pt2)




if __name__ == "__main__":
    main()