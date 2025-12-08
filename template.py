def part1(inp: str) -> int: ...


def part2(inp: str) -> int: ...


def test():
    INPUT = """
    """

    EXPECTED = ...
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = ...
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
