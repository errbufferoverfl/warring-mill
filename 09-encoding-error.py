import itertools
from _bisect import bisect_left, insort_left
from collections import deque
from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def window(seq, n=26):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win


def calc_sum(keys: list) -> set:
    summations = set()
    for i, x in enumerate(keys):
        for j in keys:
            summations.add(x + j)

    return summations


def find_contiguous_set(keys: list, our_sum: int) -> int:
    for number in itertools.count(2):
        for count in range(len(keys) - 1):
            group = keys[count: count + number]

            if sum(group) == our_sum:
                return min(group) + max(group)


if __name__ == '__main__':
    puzzle = open_puzzle("09-encoding-error.txt")
    puzzle = [int(line.strip()) for line in puzzle]

    window = 25
    current_decryption_window = sorted(puzzle[:window])
    part_one_answer = 0

    for count in range(window, len(puzzle)):
        current_summation = calc_sum(current_decryption_window)
        del current_decryption_window[bisect_left(current_decryption_window, puzzle[count - window])]
        if puzzle[count] not in current_summation: part_one_answer = puzzle[count]
        insort_left(current_decryption_window, puzzle[count])

    print(part_one_answer)
    print(find_contiguous_set(puzzle, part_one_answer))
