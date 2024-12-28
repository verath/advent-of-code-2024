import unittest
import heapq
import collections
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT = (SCRIPT_DIR / "input.txt").read_text()
TEST_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


def part1(input: str) -> int:
    left_list = []
    right_list = []
    for line in input.splitlines():
        left, right = line.split("   ")
        left, right = int(left), int(right)
        heapq.heappush(left_list, left)
        heapq.heappush(right_list, right)

    total_diff = 0
    for _ in range(len(left_list)):
        left = heapq.heappop(left_list)
        right = heapq.heappop(right_list)
        total_diff += abs(left - right)

    return total_diff


def part2(input: str) -> int:
    left_list = []
    right_lookup = collections.Counter()
    for line in input.splitlines():
        left, right = line.split("   ")
        left, right = int(left), int(right)
        right_lookup[right] += 1
        left_list.append(left)

    sim_score = sum(num * right_lookup[num] for num in left_list)
    return sim_score


class Day01Test(unittest.TestCase):

    def test_part1(self) -> None:
        self.assertEqual(part1(TEST_INPUT), 11)
        self.assertEqual(part1(INPUT), 2164381)

    def test_part2(self) -> None:
        self.assertEqual(part2(TEST_INPUT), 31)
        self.assertEqual(part2(INPUT), 20719933)


def main():
    unittest.main(exit=False)
    print("part1:", part1(INPUT))
    print("part2:", part2(INPUT))


if __name__ == "__main__":
    main()
