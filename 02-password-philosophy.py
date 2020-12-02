from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def normalise(to_convert: list) -> list:
    new_list = list()

    for line in to_convert:
        line = line.replace(': ', ',')
        line = line.replace('-', ',')
        line = line.replace(' ', ',')
        line = line.split(',')
        new_list.append(line)

    return new_list


def validate_passwords() -> int:
    puzzle = open_puzzle("02-password-philosophy.txt")
    puzzle = [line.strip() for line in puzzle]
    normalised_puzzle = normalise(puzzle)
    count = 0

    for line in normalised_puzzle:
        occurrences = line[3].count(line[2])

        if int(line[0]) <= occurrences <= int(line[1]):
            count = count + 1

    return count


def validate_passwords_again() -> int:
    puzzle = open_puzzle("02-password-philosophy.txt")
    puzzle = [line.strip() for line in puzzle]
    normalised_puzzle = normalise(puzzle)
    count = 0

    for line in normalised_puzzle:
        # Add 1 because Toboggan Corporate Policies have no concept of "index zero"!
        occurrences = [pos + 1 for pos, char in enumerate(line[3]) if char == line[2]]
        if int(line[0]) in occurrences and int(line[1]) in occurrences:
            continue
        elif int(line[0]) in occurrences:
            count = count + 1
        elif int(line[1]) in occurrences:
            count = count + 1

    return count


if __name__ == '__main__':
    count = validate_passwords()
    print(count)
    count = validate_passwords_again()
    print(count)

