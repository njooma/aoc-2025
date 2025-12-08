import re
from typing import Iterable
from functools import reduce
from operator import add, mul


def calculate(operands: Iterable[int], operator: str):
    if operator == "+":
        return sum(operands)
    elif operator == "*":
        return reduce(mul, operands)


def part1(inp: str) -> int:
    lines = [x.strip() for x in inp.strip().split("\n")]
    operators = [x.strip() for x in lines[-1].split()]
    lines = lines[:-1]
    lines = [[int(n) for n in re.findall(r"(\d+)\s*", x)] for x in lines]

    total = 0
    for idx in range(len(operators)):
        total += calculate([x[idx] for x in lines], operators[idx])

    return total


def part2(inp: str) -> int:
    lines = [x for x in inp.strip().split("\n")]
    operators = [x.strip() for x in lines[-1].split()]
    lines = lines[:-1]

    total = 0
    i = 0
    operands = []
    for idx in range(len(lines[0])):
        numbers = [x[idx].strip() for x in lines]
        if any(numbers):
            operand = reduce(add, numbers).strip()
            operands.append(int(operand))
        else:
            total += calculate(operands, operators[i])
            operands = []
            i += 1

    total += calculate(operands, operators[i])
    return total


def test():
    INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
    """

    EXPECTED = 4277556
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 3263827
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
