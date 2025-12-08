def part1(inp: str) -> int:
    ranges, ids = [x.split() for x in inp.split("\n\n")]
    ranges = [
        range(int(start), int(end) + 1)
        for (start, end) in [x.split("-") for x in ranges]
    ]
    ids = [int(x) for x in ids]

    total = 0
    for id in ids:
        for r in ranges:
            if id in r:
                total += 1
                break

    return total


def part2(inp: str) -> int:
    ranges, _ = [x.split() for x in inp.split("\n\n")]
    ranges = [(int(start), int(end)) for (start, end) in [x.split("-") for x in ranges]]
    ranges = sorted(ranges, key=lambda x: x[0])
    first = ranges[0]
    ranges = ranges[1:]

    number_line = [first]
    did_change = True
    while did_change:
        nl = number_line
        for r in ranges:
            (start, end) = r
            pair = nl[-1]
            (s, e) = pair
            if start <= e and end <= e:
                continue
            elif start <= e and end > e:
                nl[-1] = (s, end)
            elif start == e + 1:
                nl[-1] = (s, end)
            else:
                nl.append((start, end))

        if nl == number_line:
            did_change = False
        number_line = nl

    total = sum([end - start + 1 for (start, end) in number_line])
    return total


def test():
    INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
    """

    EXPECTED = 3
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 14
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
