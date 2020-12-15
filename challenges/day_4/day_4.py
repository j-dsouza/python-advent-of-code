from typing import List, Dict

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

    return counter



def main():
    passports = parse("/home/jdsouza/github/python-advent-of-code/data/day_4.txt")
    pt_1 = pt1(passports)
    print(pt_1)


if __name__ == "__main__":
    main()