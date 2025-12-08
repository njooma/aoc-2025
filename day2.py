def part1(inp: str) -> int:
    inp = inp.split(",")
    total = 0
    for i in inp:
        if not i.strip():
            continue
        x = map(lambda x: x.strip(), i.split("-"))
        start, end = x
        s_even = len(start) % 2 == 0
        e_even = len(end) % 2 == 0
        s_int, e_int = int(start), int(end)
        print(start, end, end="\n\t")

        if not s_even and not e_even and len(start) == len(end):
            print()
            continue

        if not s_even:
            start = "1" + "0" * len(start)
            s_int = int(start)

        if s_int > e_int:
            print()
            continue

        first_half = start[: (len(start) // 2)]
        while (
            int(first_half + first_half) >= s_int
            and int(first_half + first_half) <= e_int
        ):
            print(first_half + first_half, end="\n\t")
            total += int(first_half + first_half)
            first_half = str(int(first_half) + 1)
        print()

    print(total)
    return total


def part1_bf(inp: str) -> int:
    inp = inp.split(",")
    total = 0
    for i in inp:
        if not i.strip():
            continue
        x = map(lambda x: x.strip(), i.split("-"))
        start, end = x
        s_int, e_int = int(start), int(end)

        for i in range(s_int, e_int + 1):
            if i < 11:
                continue
            first_half = str(i)[: len(str(i)) // 2]
            if i == int(first_half + first_half):
                total += i

    return total


def part2(inp: str) -> int:
    inp = inp.split(",")
    total = 0
    for i in inp:
        if not i.strip():
            continue
        x = map(lambda x: x.strip(), i.split("-"))
        start, end = x

        for i in range(int(start), int(end) + 1):
            if i < 11:
                continue

            stri = str(i)

            sqrt = int(len(stri) ** 0.5)
            factors = [1]
            for j in range(2, sqrt + 1):
                if len(stri) % j == 0:
                    factors.append(j)
                    factors.append(len(stri) // j)
            factors = list(set(factors))

            for factor in factors:
                ll = len(stri) // factor
                if i == int(stri[:factor] * ll):
                    total += i
                    break

    return total


def test():
    INPUT = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
    """

    EXPECTED = 1227775554
    output = part1_bf(INPUT)
    assert output == EXPECTED

    EXPECTED = 4174379265
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1_bf(inp))
        print(part2(inp))
