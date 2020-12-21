from typing import List, Tuple

class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.one_over = len(self.instructions) + 1
        self.acc = 0
        self.used = []
        self.cur = 0
        self.running = True

    def run_pt1(self):
        while self.running:
            if self.cur in self.used:
                self.running = False

            elif self.instructions[self.cur][0] == "nop":
                self.used.append(self.cur)
                self.cur += 1

            elif self.instructions[self.cur][0] == "acc":
                self.used.append(self.cur)
                self.acc += self.instructions[self.cur][1]
                self.cur += 1

            elif self.instructions[self.cur][0] == "jmp":
                self.used.append(self.cur)
                self.cur += self.instructions[self.cur][1]

        return self.acc

    def run_pt2(self):
        self.one_over = len(self.instructions)
        for i in range(len(self.instructions)):
            self.acc = 0
            self.used = []
            self.cur = 0
            self.running = True
            jmp = False
            nop = False
            if self.instructions[i][0] == "nop":
                self.instructions[i][0] = "jmp"
                nop = True
            elif self.instructions[i][0] == "jmp":
                self.instructions[i][0] = "nop"
                jmp = True
            # import pdb; pdb.set_trace()

            while self.cur < self.one_over and self.running:
                if self.cur in self.used:
                    self.running = False

                elif self.instructions[self.cur][0] == "nop":
                    self.used.append(self.cur)
                    self.cur += 1

                elif self.instructions[self.cur][0] == "acc":
                    self.used.append(self.cur)
                    self.acc += self.instructions[self.cur][1]
                    self.cur += 1

                elif self.instructions[self.cur][0] == "jmp":
                    self.used.append(self.cur)
                    self.cur += self.instructions[self.cur][1]
                
                if self.cur == self.one_over:
                    return self.acc

            if nop:
                self.instructions[i][0] = "nop"
            elif jmp:
                self.instructions[i][0] = "jmp"


def parse(filename: str) -> List[List]:
    with open(filename) as f:
        lines = f.readlines()
    
    return [[x.split(" ")[0], int(x.split(" ")[1])] for x in lines]


def main():
    instructions = parse("/home/jdsouza/github/python-advent-of-code/data/day_8.txt")
    computer = Computer(instructions)
    
    print(computer.run_pt1())

    print(computer.run_pt2())


if __name__ == "__main__":
    main()