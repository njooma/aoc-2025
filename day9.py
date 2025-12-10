from typing import TypeVar

def area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


T = TypeVar('T')
def rindex(lst: list[T], val: T) -> int:
    return len(lst) - lst[::-1].index(val) - 1

def part1(inp: str) -> int:
    points = [
        (int(x), int(y))
        for (x, y) in [line.split(",") for line in inp.strip().split("\n")]
    ]
    max_area = 0
    for idx, point in enumerate(points):
        for p in points[idx + 1 :]:
            a = area(point, p)
            if a > max_area:
                max_area = a
    return max_area


def part2(inp: str) -> int:
    points = [
        (int(x), int(y))
        for (x, y) in [line.split(",") for line in inp.strip().split("\n")]
    ]

    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    grid: list[list[str]] = [['.' for x in range(max_x+2)] for y in range(max_y+2)]
    for row in grid:
        print(row)

    for idx, point in enumerate(points):
        grid[point[1]][point[0]] = '#'
        np = points[idx+1-len(points)]
        for x in range(abs(point[0] - np[0])):
            grid[point[1]][x + min(point[0], np[0])] = 'X'
        for y in range(abs(point[1] - np[1])):
            grid[y + min(point[1], np[1])][point[0]] = 'X'

    for row in grid:
        print(row)
        first, last = None, None
        for idx, elm in enumerate(row):
            if not elm == '.':
                first = idx
                break
        for idx, elm in enumerate(reversed(row)):
            if not elm == '.':
                last = len(row) - idx - 1
                break
        if first is None or last is None:
            continue
        
        for idx, elm in enumerate(row):
            if idx in range(first, last):
                row[idx] = 'X'

    for row in grid:
        print(row)


    max_area = 0
    for idx, point in enumerate(points):
        for p in points[idx + 1 :]:
            a = area(point, p)
            if a > max_area:

                start_x = point[0]
                end_x = p[0]
                if p[0] < point[0]:
                    start_x = p[0]
                    end_x = point[0]

                start_y = point[1]
                end_y = p[1]
                if p[1] < point[1]:
                    start_y = p[1]
                    end_y = point[1]
                
                is_valid = True
                for rdx in range(start_y, end_y):
                    row = grid[rdx]
                    if '.' in row[start_x:end_x]:
                        is_valid = False
                        break

                if is_valid:
                    max_area = a
    return max_area


def test():
    INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
    """

    EXPECTED = 50
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 24
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
