from dataclasses import dataclass
from functools import reduce
from operator import mul


@dataclass
class Junction:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash(f"{self.x},{self.y},{self.z}")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


@dataclass
class Edge:
    j1: Junction
    j2: Junction

    @property
    def distance(self) -> int:
        return (
            (self.j1.x - self.j2.x) ** 2
            + (self.j1.y - self.j2.y) ** 2
            + (self.j1.z - self.j2.z) ** 2
        )

    def __str__(self):
        return f"{self.j1} -- {self.distance} -- {self.j2}"


def part1(inp: str, iterations=1000) -> int:
    junctions = [
        Junction(int(x), int(y), int(z))
        for (x, y, z) in [line.split(",") for line in inp.strip().split("\n")]
    ]
    edges: list[Edge] = []
    while len(junctions) > 0:
        junction = junctions.pop()
        for j in junctions:
            edges.append(Edge(junction, j))

    edges.sort(key=lambda edge: edge.distance)
    circuits: list[set[Junction]] = []
    for edge in edges[:iterations]:
        to_merge: list[set[Junction]] = []
        for idx, circuit in enumerate(circuits):
            if edge.j1 in circuit or edge.j2 in circuit:
                to_merge.append(idx)
        circuit = reduce(
            lambda a, b: a.union(b),
            [circuit for (idx, circuit) in enumerate(circuits) if idx in to_merge],
            {edge.j1, edge.j2},
        )
        for idx in reversed(to_merge):
            del circuits[idx]
        circuits.append(circuit)

    lengths = [len(circuit) for circuit in circuits]
    lengths.sort(reverse=True)
    return reduce(mul, lengths[:3])


def part2(inp: str) -> int:
    junctions = [
        Junction(int(x), int(y), int(z))
        for (x, y, z) in [line.split(",") for line in inp.strip().split("\n")]
    ]
    edges: list[Edge] = []
    for idx, junction in enumerate(junctions):
        for j in junctions[idx + 1 :]:
            edges.append(Edge(junction, j))

    edges.sort(key=lambda edge: edge.distance)

    circuits: list[set[Junction]] = [{j} for j in junctions]
    for edge in edges:
        to_merge: list[set[Junction]] = []
        for idx, circuit in enumerate(circuits):
            if edge.j1 in circuit or edge.j2 in circuit:
                to_merge.append(idx)
        circuit = reduce(
            lambda a, b: a.union(b),
            [circuit for (idx, circuit) in enumerate(circuits) if idx in to_merge],
            {edge.j1, edge.j2},
        )
        for idx in reversed(to_merge):
            del circuits[idx]
        circuits.append(circuit)
        if len(circuits) == 1:
            return edge.j1.x * edge.j2.x

    raise ValueError("Something has gone terribly wrong")


def test():
    INPUT = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
    """

    EXPECTED = 40
    output = part1(INPUT, 10)
    assert output == EXPECTED

    EXPECTED = 25272
    output = part2(INPUT)
    assert output == EXPECTED


if __name__ == "__main__":
    test()

    INPUT = __file__.split(".")[0] + ".txt"
    with open(INPUT, "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
