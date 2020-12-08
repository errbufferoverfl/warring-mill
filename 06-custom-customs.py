from collections import Counter
from pathlib import Path
from typing import Optional, Union


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def aggregate_dict_counts(original_dict: dict, dict_to_append:dict) -> dict:
    ephemeral_dict = {**original_dict, **dict_to_append}

    for key, value in ephemeral_dict.items():
        if key in original_dict and key in dict_to_append:
            ephemeral_dict[key] = value + original_dict[key]

    return ephemeral_dict


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


def count_yes_answers(customs_form: str) -> int:
    return len(set(customs_form))


def count_common_questions(customs_form: list[str]) -> Union[dict, dict]:
    frequency_analysis = dict()

    for person in customs_form:
        q_frequency = Counter(person)
        frequency_analysis = aggregate_dict_counts(frequency_analysis, q_frequency)

    return frequency_analysis


def identify_common_answers(number_of_people: int, frequency_analysis: dict):
    count = 0

    for key, value in frequency_analysis.items():
        if frequency_analysis[key] == number_of_people:
            count = count + 1

    return count


if __name__ == '__main__':
    puzzle = open_puzzle("06-custom-customs.txt")
    puzzle = [line.strip() for line in puzzle]
    puzzle.append('')
    puzzle = standardise_puzzle(puzzle)
    yes_count = list()
    same_answer = list()

    for puzzle_list in puzzle:
        yes_count.append(count_yes_answers(''.join(puzzle_list)))
        answer_frequency = count_common_questions(puzzle_list)
        same_answer.append(identify_common_answers(len(puzzle_list), answer_frequency))

    print(sum(yes_count))
    print(sum(same_answer))



