import re
from pathlib import Path
from typing import Optional


def open_puzzle(file_name: str) -> Optional[list[str]]:
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def standardise_puzzle(lines: list) -> list[list[str]]:
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


def convert_to_dictionary(standardised_input: list[list[str]]) -> list[dict]:
    actual_puzzle = list()

    for row in standardised_input:
        dictonaryed_input = dict()
        for value in row:
            key, pair = value.split(':')
            dictonaryed_input[key] = pair
        actual_puzzle.append(dictonaryed_input)
    return actual_puzzle


def validate_height(height: str) -> bool:
    if height.endswith("cm"):
        if 150 <= int(height.replace("cm", "")) <= 193:
            return True
    elif height.endswith("in"):
        if 59 <= int(height.replace("in", "")) <= 76:
            return True
    else:
        return False


def validate_year(year: int, min_year: int, max_year: int) -> bool:
    length = len(year) == 4
    between = min_year <= int(year) <= max_year

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


def validate_eye_colour(colour: str) -> bool:
    if colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    else:
        return False


def validate_passport_id(passport_id: str) -> bool:
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
    valid_passports = 0

    for passport in passport_dicts:
        if len(passport) == 8 and validate_all_the_things(passport):
            valid_passports = valid_passports + 1
        elif len(passport) == 7 and passport.get('cid', None) is None and validate_all_the_things(passport):
            valid_passports = valid_passports + 1

    print(valid_passports)


if __name__ == '__main__':
    puzzle = open_puzzle("04-passport-processing.txt")
    puzzle = [line.strip() for line in puzzle]
    puzzle = standardise_puzzle(puzzle)
    puzzle = convert_to_dictionary(puzzle)
    papers_please(puzzle)
