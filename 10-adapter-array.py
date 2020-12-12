from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def avoid_a_jolt(puzzle: list) -> int:
    # three count starts one higher because your device's built-in adapter is always 3 higher than the highest adapter
    one_count, three_count = 0, 1

    for position_i in range(len(puzzle)+1):
        try:
            if abs(puzzle[position_i] - puzzle[position_i+1]) == 1:
                one_count = one_count + 1
            else:
                three_count = three_count + 1
        except IndexError:
            return one_count * three_count


def adapter_configurations(puzzle: list) -> int:
    size = len(puzzle)

    adapter_configs = [1] * size
    for position_i in range(1, size):
        adapter_configs[position_i] = adapter_configs[position_i - 1]
        if position_i > 1 and abs(puzzle[position_i] - puzzle[position_i - 2]) <= 3:
            adapter_configs[position_i] += adapter_configs[position_i - 2]
        if position_i > 2 and abs(puzzle[position_i] - puzzle[position_i - 3]) <= 3:
            adapter_configs[position_i] += adapter_configs[position_i - 3]

    return adapter_configs[-1]


if __name__ == '__main__':
    puzzle = open_puzzle("10-adapter-array.txt")
    puzzle = [int(line.strip()) for line in puzzle]
    # append a zero to account for the charging outlet that has an effective rating of 0 jolts
    puzzle.append(0)
    puzzle = sorted(puzzle)

    print(avoid_a_jolt(puzzle))
    print(adapter_configurations(puzzle))
