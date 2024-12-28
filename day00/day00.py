import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT = (SCRIPT_DIR / "input.txt").read_text()


def part1(input_str: str) -> int:
    len(input_str)
    return -1


def part2(input_str: str) -> int:
    len(input_str)
    return -1


class Day00Test(unittest.TestCase):

    TEST_INPUT = """
""".strip()

    def test_part1(self) -> None:
        self.assertEqual(part1(self.TEST_INPUT), 0)
        self.assertEqual(part1(INPUT), 0)

    def test_part2(self) -> None:
        self.assertEqual(part2(self.TEST_INPUT), 0)
        self.assertEqual(part2(INPUT), 0)


def main() -> None:
    res = unittest.main(exit=False).result
    if res.wasSuccessful():
        print("part1:", part1(INPUT))
        print("part2:", part2(INPUT))


if __name__ == "__main__":
    main()
