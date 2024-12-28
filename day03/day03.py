from dataclasses import dataclass
from typing import Generator, TypeAlias
import unittest
from pathlib import Path
import re

TEST_INPUT_PART1 = (
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)
TEST_INPUT_PART2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)

SCRIPT_DIR = Path(__file__).parent
INPUT = (SCRIPT_DIR / "input.txt").read_text().strip()


@dataclass
class Mul:
    lhs: int
    rhs: int


@dataclass
class Do:
    pass


@dataclass
class Dont:
    pass


Instruction: TypeAlias = Mul | Do | Dont

MUL_PATTERN = re.compile(r"mul\((?P<lhs>\d{1,3}),(?P<rhs>\d{1,3})\)")
DO_PATTERN = re.compile(r"do\(\)")
DONT_PATTERN = re.compile(r"don't\(\)")


def parse_instructions(s: str) -> Generator[Instruction, None, None]:
    while s:
        if m := MUL_PATTERN.match(s):
            s = s[m.end() :]
            lhs = int(m.group("lhs"))
            rhs = int(m.group("rhs"))
            yield Mul(lhs, rhs)
        elif m := DO_PATTERN.match(s):
            s = s[m.end() :]
            yield Do()
        elif m := DONT_PATTERN.match(s):
            s = s[m.end() :]
            yield Dont()
        else:
            s = s[1:]


def part1(input_str: str) -> int:
    return sum(
        inst.lhs * inst.rhs
        for inst in parse_instructions(input_str)
        if isinstance(inst, Mul)
    )


def part2(input_str: str) -> int:
    total = 0
    enabled = True
    for instruction in parse_instructions(input_str):
        match instruction:
            case Do():
                enabled = True
            case Dont():
                enabled = False
            case Mul(lhs, rhs) if enabled:
                total += lhs * rhs

    return total


class Day03Test(unittest.TestCase):
    def test_part1(self) -> None:
        self.assertEqual(part1(TEST_INPUT_PART1), 161)
        self.assertEqual(part1(INPUT), 174960292)

    def test_part2(self) -> None:
        self.assertEqual(part2(TEST_INPUT_PART2), 48)
        self.assertEqual(part2(INPUT), 56275602)


if __name__ == "__main__":
    unittest.main()
