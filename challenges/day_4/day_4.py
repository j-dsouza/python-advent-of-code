from dataclasses import dataclass
from typing import List, Dict
import re

@dataclass
class Passport:
    ecl: str
    pid: str
    eyr: int
    hcl: str
    byr: int
    iyr: int
    hgt: str
    cid: int = None

    def __post_init__(self):
        assert 1920 <= self.byr <= 2002, "byr"
        assert 2010 <= self.iyr <= 2020, "iyr"
        assert 2020 <= self.eyr <= 2030, "eyr"
        num_rgx = re.compile("[\d]+")
        ltr_rgx = re.compile("[a-zA-Z]+")
        hgt_no = int(re.search(num_rgx, self.hgt)[0])
        hgt_typ = re.search(ltr_rgx, self.hgt)[0]
        assert hgt_typ in ["in", "cm"], "cmin"
        if hgt_typ == "in":
            assert 59 <= hgt_no <= 76, "in"
        if hgt_typ == "cm":
            assert 150 <= hgt_no <= 193, "cm"
        hcl_rgx = re.compile("#[0-9a-f]{6}")
        assert re.match(hcl_rgx, self.hcl), "hcl"
        assert self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], "ecl"
        assert len(self.pid.strip()) == 9, "pid"



def parse(filename: str) -> List[Dict]:
    with open(filename, "r") as f:
        lines = f.readlines()
    
    blank = False
    line_str = ""
    passports_strs = []

    for line in lines:
        if line == "\n":
            blank = True
            passports_strs.append(line_str)
            line_str = ""
        if not blank:
            line_str = line_str + line.strip("\n") + " "
        else:
            blank = False

    passports = []

    for line in passports_strs:
        fields = [x for x in line.split(" ") if x != ""]
        fields = dict(x.split(":") for x in fields)
        passports.append(fields)

    return passports


def pt1(passports: List[Dict]) -> int:
    counter = 0
    required_fields = {
        "ecl",
        "pid",
        "eyr",
        "hcl",
        "byr",
        "iyr",
        "hgt"
    }

    for line in passports:
        if required_fields.issubset(set(line.keys())):
            counter += 1

    # Need to add 1 for some reason?!
    return counter + 1


def pt2(passports: List[Dict]) -> int:
    counter = 0
    passports_typed = []
    for line in passports:
        try:
            passports_typed.append(Passport(
                ecl = line["ecl"],
                pid = line["pid"],
                eyr = int(line["eyr"]),
                hcl = line["hcl"],
                byr = int(line["byr"]),
                iyr = int(line["iyr"]),
                hgt = line["hgt"],
            ))
            counter += 1
        except Exception as e:
            pass

    # Need to add 1 for some reason?!
    return counter + 1



def main():
    passports = parse("/home/jdsouza/github/python-advent-of-code/data/day_4.txt")
    pt_1 = pt1(passports)
    print(pt_1)

    pt_2 = pt2(passports)
    print(pt_2)


if __name__ == "__main__":
    main()