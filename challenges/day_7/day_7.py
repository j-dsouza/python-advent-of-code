from typing import List


def parse(filename: str) -> dict:
    with open(filename, "r") as f:
        lines = f.readlines()

    bags = {}
    for bag in lines:
        outer = " ".join(bag.split(" ")[:2])
        inside = bag.split("contain ")[1]
        inside_list = inside.split(", ")
        inner = {}
        for bag in inside_list:
            if "no other bags" not in bag:
                colour = " ".join(bag.split(" ")[1:3])
                number = int(bag.split(" ")[0])
                inner[colour] = number
        bags[outer] = inner

    return bags


def pt_1(bags, colour, top_colours):
    for key, contents in bags.items():
        if colour in contents.keys():
            top_colours.add(key)
            pt_1(bags, key, top_colours)

    return top_colours


def pt_2(bags, colour, no):
    total = 0
    contents = bags[colour]
    total += no
    for new_col in contents.keys():
        if bags[new_col]:
            total += no * pt_2(bags, new_col, contents[new_col])
        else:
            total += no * contents[new_col]

    return total
    

def main():
    bags = parse("/home/jdsouza/github/python-advent-of-code/data/day_7.txt")
    # print(bags)

    pt1 = pt_1(bags, "shiny gold", set())
    print(len(pt1))

    pt2 = pt_2(bags, "shiny gold", 1)
    pt2 -= 1            # Remove the additional 1 that gets added at start
    print(pt2)


if __name__ == "__main__":
    main()