import re
from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def standardised(lines: list) -> list[list[str]]:
    standardised_puzzle = list()
    batch = list()

    for line in lines:
        if line != '':
            batch.append(line)
        else:
            standardised_batch = ' '.join(batch).split(' ')
            standardised_puzzle.append(standardised_batch)
            batch = list()

    return standardised_puzzle


def dictionaryify(standardised_input: list[list[str]]) -> list[dict]:
    actual_puzzle = list()
    for row in standardised_input:
        dictonaried_input = dict()
        for value in row:
            key, pair = value.split(':')
            dictonaried_input[key] = pair
        actual_puzzle.append(dictonaried_input)
    return actual_puzzle


def validate_height(height: str):
    if height.endswith("cm"):
        if 150 <= int(height.replace("cm", "")) <= 193:
            return True
        else:
            return False
    elif height.endswith("in"):
        if 59 < int(height.replace("in", "")) < 76:
            return True
        else:
            return False


def validate_year(year: int, min: int, max: int):
    length = len(year) == 4
    between = min <= int(year) <= max

    if length and between:
        return True
    else:
        return False


def validate_hair_colour(colour: str):
    hex_re = r"#[0-9a-fA-F]+"

    if re.match(hex_re, colour):
        return True
    else:
        return False


def validate_eye_colour(colour: str):
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if colour in valid_colours:
        return True
    else:
        return False


def validate_passport_id(passport_id: str):
    if len(passport_id) == 9:

        return True
    else:
        return False


def validate_all_the_things(passport: dict):
    if validate_passport_id(passport["pid"]) \
            and validate_height(passport["hgt"]) \
            and validate_year(passport["byr"], 1920, 2002) \
            and validate_year(passport["iyr"], 2010, 2020) \
            and validate_year(passport["eyr"], 2020, 2030) \
            and validate_hair_colour(passport["hcl"]) \
            and validate_eye_colour(passport["ecl"]):
        return True
    else:
        return False


def papers_please(passport_dicts: list):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_keys = ['cid']
    valid_passports = 1

    for passport in passport_dicts:
        if len(passport) == 8:
            if validate_all_the_things(passport):
                valid_passports = valid_passports + 1
        elif len(passport) == 7 and passport.get('cid', None) is None:
            if validate_all_the_things(passport):
                valid_passports = valid_passports + 1

    print(valid_passports)


if __name__ == '__main__':
    puzzle = open_puzzle("04-passport-processing.txt")
    puzzle = [line.strip() for line in puzzle]
    puzzle = standardised(puzzle)
    puzzle = dictionaryify(puzzle)
    papers_please(puzzle)
