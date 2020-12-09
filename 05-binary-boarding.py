from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def process_boarding_pass(boarding_pass: str, translation_table: dict) -> int:
    return int(boarding_pass.translate(translation_table), 2)


if __name__ == '__main__':
    puzzle = open_puzzle("05-binary-boarding.txt")
    puzzle = [line.strip() for line in puzzle]

    translation_table = ''.maketrans("FBLR", "0101")

    boarding_passes = list()

    for puzzle_line in puzzle:
        boarding_passes.append(process_boarding_pass(puzzle_line, translation_table))

    print(max(boarding_passes))
    print(sum(range(min(boarding_passes), max(boarding_passes) + 1)) - sum(boarding_passes))
