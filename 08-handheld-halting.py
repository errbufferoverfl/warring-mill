import sys
from pathlib import Path

global accumulator
accumulator = 0


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def acc(amount: str, pos: int) -> int:
    """
    acc increases or decreases a single global value called the accumulator by the value given in the argument.
    For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction,
    the instruction immediately below it is executed next.

    Args:
        pos:
        amount:

    Returns:

    """
    global accumulator
    accumulator = accumulator + int(amount.strip('+'))
    return pos + 1


def jmp(amount: str, pos: int) -> int:
    """
    jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as
    an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to
    the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.

    Args:
        pos:
        amount:

    Returns:
    """
    return pos + int(amount.strip('+'))


def nop(pos: int) -> int:
    """
    nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

    Returns:
    """
    return pos + 1


def run(current_puzzle: list, part = 'one'):
    memory = list()
    pos = 0

    while True:
        if part == 'one':
            if pos in memory:
                print(accumulator)
                return
        else:
            if pos == len(current_puzzle):
                print(accumulator)
                return
            elif len(memory) >= len(current_puzzle):
                return
            elif pos in memory:
                return

        instruction = current_puzzle[pos].split()[0]
        amount = current_puzzle[pos].split()[1]

        memory.append(pos)

        if instruction == 'acc':
            pos = acc(amount, pos)
        elif instruction == 'jmp':
            pos = jmp(amount, pos)
        else:
            pos = nop(pos)


if __name__ == '__main__':
    puzzle = open_puzzle("08-handheld-halting.txt")
    puzzle = [line.strip() for line in puzzle]

    # part 1
    run(puzzle)

    for position in range(len(puzzle)):
        accumulator = 0
        new_puzzle = [p[:] for p in puzzle]

        if new_puzzle[position].startswith("nop"):
            new_puzzle[position] = new_puzzle[position].replace("nop", "jmp")
            run(new_puzzle, 'two')
        elif new_puzzle[position].startswith("jmp"):
            new_puzzle[position] = new_puzzle[position].replace("jmp", "nop")
            run(new_puzzle, 'two')
