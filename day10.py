from functools import reduce
from itertools import combinations_with_replacement


def part1(inp: str) -> int:
    inputs = [x for x in inp.strip().splitlines()]
    total = 0
    for line in inputs:
        input = line.split()
        lights = [0 if x == "." else 1 for x in input[0][1:-1]]
        buttons = [list(map(int, x[1:-1].split(","))) for x in input[1:-1]]
        joltage = eval(input[-1])

        memos = {}
        for button in buttons:
            light = [0] * len(lights)
            for b in button:
                light[b] = 1
            memos[str(button)] = light

        if lights in memos.values():
            total += 1
            continue

        x = 1
        found = False
        while not found:
            for comb in combinations_with_replacement(buttons, x):
                for button in buttons:
                    key = list(comb) + [button]
                    ls = [memos[str(b)] for b in key]
                    btn = str(key)
                    light = reduce(
                        lambda a, b: list(x ^ y for x, y in zip(a, b)),
                        ls,
                        [0] * len(lights),
                    )
                    memos[btn] = light
                    if light == lights:
                        found = True
                        total += len(key)
                        break
                if found:
                    break
            x += 1

    return total


def part2(inp: str) -> int:
    inputs = [x for x in inp.strip().splitlines()]
    total = 0
    for line in inputs:
        input = line.split()
        lights = [0 if x == "." else 1 for x in input[0][1:-1]]
        buttons = [list(map(int, x[1:-1].split(","))) for x in input[1:-1]]
        joltage = [int(x) for x in input[-1][1:-1].split(",")]

        memos = {}
        for button in buttons:
            j = [0] * len(joltage)
            for b in button:
                j[b] = 1
            memos[str(button)] = j

        if joltage in memos.values():
            total += 1
            continue

        x = 1
        found = False
        while not found:
            for comb in combinations_with_replacement(buttons, x):
                for button in buttons:
                    key = list(comb) + [button]
                    ls = [memos[str(b)] for b in key]
                    btn = str(key)
                    j = reduce(
                        lambda a, b: list(x + y for x, y in zip(a, b)),
                        ls,
                        [0] * len(joltage),
                    )
                    memos[btn] = j
                    if j == joltage:
                        found = True
                        total += len(key)
                        break
                if found:
                    break
            x += 1
            if x > 100:
                break

    return total


def test():
    INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    """

    EXPECTED = 7
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 33
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
