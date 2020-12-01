import math
from pathlib import Path
import itertools


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def repair_report() -> int:
    puzzle = open_puzzle("01-report-repair.txt")
    puzzle = [int(line.strip()) for line in puzzle]

    for i in range(0, len(puzzle)):
        for combination in itertools.combinations(puzzle, i):
            if sum(combination) == 2020:
                yield combination


if __name__ == '__main__':
    combination = repair_report()

    for combo in combination:
        print(math.prod(combo))
