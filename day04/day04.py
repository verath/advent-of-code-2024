import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT = (SCRIPT_DIR / "input.txt").read_text().strip()


Coord = tuple[int, int]
Lookup = dict[Coord, str]


def parse(input_str: str) -> Lookup:
    lookup = {}
    for y, line in enumerate(input_str.splitlines()):
        for x, ch in enumerate(line):
            lookup[(x, y)] = ch
    return lookup


def part1(input_str: str) -> int:
    lookup = parse(input_str)
    directions = [
        (1, 0),  # horizontal forward
        (-1, 0),  # horizontal backward
        (0, 1),  # vertical forward
        (0, -1),  # vertical backward
        (1, 1),  # diagonal down right
        (-1, 1),  # diagonal down left
        (-1, -1),  # diagonal up left
        (1, -1),  # diagonal up right
    ]

    def check_direction(start_pos: Coord, direction: tuple[int, int]) -> bool:
        for i, expected_char in enumerate("XMAS"):
            x = start_pos[0] + direction[0] * i
            y = start_pos[1] + direction[1] * i
            if lookup.get((x, y)) != expected_char:
                return False
        return True

    num_found = 0
    for pos in lookup:
        num_found += sum(check_direction(pos, dir) for dir in directions)

    return num_found


def part2(input_str: str) -> int:
    lookup = parse(input_str)

    def is_x_mas(start_pos: Coord) -> bool:
        if lookup[start_pos] != "A":
            return False
        x, y = start_pos
        ul = lookup.get((x - 1, y - 1), "")
        ur = lookup.get((x + 1, y - 1), "")
        dr = lookup.get((x + 1, y + 1), "")
        dl = lookup.get((x - 1, y + 1), "")
        diag_a = ul + dr
        diag_b = ur + dl
        return diag_a in {"MS", "SM"} and diag_b in {"MS", "SM"}

    return sum(is_x_mas(pos) for pos in lookup)


class Day04Test(unittest.TestCase):
    TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()

    def test_part1(self) -> None:
        self.assertEqual(part1(self.TEST_INPUT), 18)
        self.assertEqual(part1(INPUT), 2462)

    def test_part2(self) -> None:
        self.assertEqual(part2(self.TEST_INPUT), 9)
        self.assertEqual(part2(INPUT), 1877)


if __name__ == "__main__":
    unittest.main()
