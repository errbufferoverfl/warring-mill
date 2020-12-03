from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def toboggan(to_solve: list, movement: tuple) -> int:
    count = 0
    trees_encountered = 0
    marked = list()

    if movement[1] > 1:
        # remove every nth line
        del to_solve[movement[1]-1::movement[1]]
    # ignore the first line
    to_solve.pop(0)

    for line in to_solve:
        # movement 0: spots right
        # movement 1: spots down
        count += movement[0]
        check_index = count % len(line)
        if line[check_index] == '#':
            line = line[:check_index] + "X" + line[check_index + 1:]
            marked.append(line)
            trees_encountered += 1
        else:
            line = line[:check_index] + "O" + line[check_index + 1:]
            marked.append(line)

    for line in marked:
        print(line)

    print(f"Trees encountered: {trees_encountered}\n")


if __name__ == '__main__':
    move = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for combo in move:
        puzzle = open_puzzle("03-toboggan-trajectory.txt")
        puzzle = [line.strip() for line in puzzle]
        toboggan(puzzle, combo)


