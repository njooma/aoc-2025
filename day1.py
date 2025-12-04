def parse_input(inp: str) -> int:
    ticks = int(inp[1:])
    if inp[0] == 'L':
        return ticks*-1
    return ticks

def part1(inp: str) -> int:
    inp = inp.split()
    pos = 50
    count = 0
    for i in inp:
        pos += parse_input(i)
        pos %= 100
        if pos == 0:
            count += 1

    return count

def part2(inp: str) -> int:
    inp = inp.split()
    pos = 50
    count = 0

    was_prev_zero = False
    for i in inp:
        num_ticks = parse_input(i)

        num_rotations = abs(num_ticks) // 100
        count += num_rotations

        additional_ticks = num_ticks - (num_rotations * 100 * (-1 if num_ticks < 0 else 1))
        pos += additional_ticks
        if not was_prev_zero and (pos <= 0 or pos > 99):
            count += 1
        pos %= 100
        was_prev_zero = pos == 0

    return count


def test():
    INPUT = """
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
    """

    EXPECTED = 3
    count = part1(INPUT)
    assert count == EXPECTED

    EXPECTED = 6
    count = part2(INPUT)
    assert count == EXPECTED

if __name__ == '__main__':
    test()
    
    INPUT = __file__.split('.')[0] + '.txt'
    with open(INPUT, 'r') as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
