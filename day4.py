from typing import Sequence

def is_valid_point(matrix: Sequence[Sequence[str]], point: tuple[int, int]) -> bool:
    (i, j) = point
    adjs_i = [0]
    adjs_j = [0]
    if i != 0:
        adjs_i.append(-1)
    if i != len(matrix)-1:
        adjs_i.append(1)
    if j != 0:
        adjs_j.append(-1)
    if j != len(matrix[i])-1:
        adjs_j.append(1)
    options = ((x, y) for x in adjs_i for y in adjs_j)
    num_adj = 0
    for (x, y) in options:
        if (x, y) == (0, 0):
            continue
        if matrix[i+x][j+y] == '@':
            num_adj += 1
    if num_adj < 4:
        return True
    return False

def part1(inp: str) -> int:
    total = 0

    mat = inp.split()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            cell = mat[i][j]
            if cell == '.':
                continue
            if is_valid_point(mat, (i, j)):
                total += 1
    
    return total


def part2(inp: str, prev = 0) -> int:
    for x in inp.split():
        print(x)
    print('prev:', prev)

    to_remove = []

    mat = list(map(lambda x: list(x), inp.split()))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            cell = mat[i][j]
            if cell == '.':
                continue
            if is_valid_point(mat, (i, j)):
                to_remove.append((i, j))
            
    if len(to_remove) == 0:
        return prev

    for (i, j) in to_remove:
        mat[i][j] = '.'
    return prev + part2('\n'.join([''.join(x) for x in mat]), len(to_remove))
    

def test():
    INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
    """

    EXPECTED = 13
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 43
    output = part2(INPUT)
    assert output == EXPECTED

if __name__ == '__main__':
    test()

    INPUT = __file__.split('.')[0] + '.txt'
    with open(INPUT, 'r') as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
