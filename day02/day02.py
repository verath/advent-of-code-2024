from typing import Generator
import unittest
from pathlib import Path

TEST_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()

SCRIPT_DIR = Path(__file__).parent
INPUT = (SCRIPT_DIR / "input.txt").read_text().strip()


def check_safe(levels: list[int]) -> bool:
    expect_increasing = levels[1] > levels[0]
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        abs_diff = abs(diff)
        is_increasing = diff > 0
        if abs_diff < 1 or abs_diff > 3:
            return False
        if (expect_increasing and not is_increasing) or (
            not expect_increasing and is_increasing
        ):
            return False
    return True


def read_levels(input_str: str) -> Generator[list[int], None, None]:
    for line in input_str.splitlines():
        yield [int(c) for c in line.split(" ")]


def part1(input_str: str) -> int:
    num_safe = 0
    for levels in read_levels(input_str):
        num_safe += 1 if check_safe(levels) else 0
    return num_safe


def part2(input_str: str) -> int:
    num_safe = 0
    for levels in read_levels(input_str):
        is_safe = check_safe(levels)
        if not is_safe:
            for i in range(len(levels)):
                levels_copy = levels.copy()
                levels_copy.pop(i)
                is_safe = check_safe(levels_copy)
                if is_safe:
                    break
        num_safe += 1 if is_safe else 0
    return num_safe


class Day02Test(unittest.TestCase):

    def test_is_safe(self) -> None:
        self.assertTrue(check_safe([7, 6, 4, 2, 1]))
        self.assertFalse(check_safe([1, 2, 7, 8, 9]))
        self.assertFalse(check_safe([9, 7, 6, 2, 1]))
        self.assertFalse(check_safe([1, 3, 2, 4, 5]))
        self.assertFalse(check_safe([8, 6, 4, 4, 1]))
        self.assertTrue(check_safe([1, 3, 6, 7, 9]))

    def test_part1(self) -> None:
        self.assertEqual(part1(TEST_INPUT), 2)
        self.assertEqual(part1(INPUT), 660)

    def test_part2(self) -> None:
        self.assertEqual(part2(TEST_INPUT), 4)
        self.assertEqual(part2(INPUT), 689)


if __name__ == "__main__":
    unittest.main()
