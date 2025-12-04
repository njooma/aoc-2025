def part1(inp: str) -> int:
    banks = inp.split()
    total = 0

    for bank in banks:
        bint = list(map(lambda x: int(x), bank))
        start = max(bint[:len(bint) - 1])
        start_index = bint.index(start)
        end = max(bint[start_index + 1:])
        total += int(str(start) + str(end))

    return total

def part2(inp: str) -> int:
    NUM_BATS = 12
    
    banks = inp.split()
    total = 0

    for bank in banks:
        to_add = []

        bint = list(map(lambda x: int(x), bank))
        while len(to_add) < NUM_BATS:
            start = max(bint[:len(bint) - (NUM_BATS - len(to_add) - 1)])
            to_add.append(start)
            bint = bint[bint.index(start) + 1:]

        total += int(''.join(map(lambda x: str(x), to_add)))

    return total


def test():
    INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
    """

    EXPECTED = 357
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 3121910778619
    output = part2(INPUT)
    assert output == EXPECTED

if __name__ == '__main__':
    test()

    INPUT = __file__.split('.')[0] + '.txt'
    with open(INPUT, 'r') as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
