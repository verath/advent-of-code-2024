import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT = (SCRIPT_DIR / "input.txt").read_text().strip()


Coord = tuple[int, int]


def part1(input: str) -> int:
    lookup: dict[Coord, str] = {}
    for y, line in enumerate(input.splitlines()):
        for x, ch in enumerate(line):
            lookup[(x, y)] = ch

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
    for pos in lookup.keys():
        num_found += sum(check_direction(pos, dir) for dir in directions)

    return num_found


def part2(input: str) -> int:
    return -1


class Day03Test(unittest.TestCase):
    TEST_INPUT_PART1 = """
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
        self.assertEqual(part1(self.TEST_INPUT_PART1), 18)
        self.assertEqual(part1(INPUT), 2462)

    # def test_part2(self) -> None:
    #     self.assertEqual(part2(TEST_INPUT_PART2), 48)
    #     self.assertEqual(part2(INPUT), 0)


if __name__ == "__main__":
    unittest.main()
