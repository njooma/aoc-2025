from dataclasses import dataclass
from typing import Optional


def part1(inp: str) -> int:
    splitters = []
    for line in inp.split("\n"):
        s = [i for i, val in enumerate(line) if val == "^"]
        if s:
            splitters.append(s)

    total = 1
    while len(splitters) > 0:
        line = splitters.pop()
        for splitter in line:
            for s in reversed(splitters):
                if splitter in s:
                    break
                if (splitter + 1) in s or (splitter - 1) in s:
                    total += 1
                    break

    return total


def part2(inp: str) -> int:
    @dataclass
    class Node:
        id: tuple[int, int]
        left: Optional["Node"] = None
        right: Optional["Node"] = None
        num_paths: Optional[int] = None
        visted: bool = False

    splitters = []
    for line in inp.split("\n"):
        s = [i for i, val in enumerate(line) if val == "^"]
        if s:
            splitters.append(s)

    nodes: dict[tuple[int, int], Node] = {}
    while len(splitters) > 0:
        line = splitters.pop()
        for splitter in line:
            for i, s in enumerate(reversed(splitters)):
                if splitter in s:
                    break
                if splitter + 1 in s:
                    curr = nodes.get(
                        (len(splitters), splitter), Node((len(splitters), splitter))
                    )
                    parent = nodes.get(
                        (len(splitters) - i - 1, splitter + 1),
                        Node((len(splitters) - i - 1, splitter + 1)),
                    )
                    parent.left = curr
                    nodes[curr.id] = curr
                    nodes[parent.id] = parent
                if splitter - 1 in s:
                    curr = nodes.get(
                        (len(splitters), splitter), Node((len(splitters), splitter))
                    )
                    parent = nodes.get(
                        (len(splitters) - i - 1, splitter - 1),
                        Node((len(splitters) - i - 1, splitter - 1)),
                    )
                    parent.right = curr
                    nodes[curr.id] = curr
                    nodes[parent.id] = parent

    start: Node
    for id, node in nodes.items():
        if id[0] == 0:
            start = node
    assert start is not None

    def dfs(node: Node) -> int:
        if node is None:
            return 1

        if node.num_paths is not None:
            return node.num_paths

        if node.left is None and node.right is None:
            node.num_paths = 2
            return 2

        total = 0
        total += dfs(node.left)
        total += dfs(node.right)
        node.num_paths = total
        return node.num_paths

    dfs(start)
    return start.num_paths


def test():
    INPUT = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
    """

    EXPECTED = 21
    output = part1(INPUT)
    assert output == EXPECTED

    EXPECTED = 40
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
