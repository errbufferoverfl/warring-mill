from pathlib import Path


def open_puzzle(file_name: str):
    input_path = Path("input/")

    if file_name:
        file_to_open = input_path / file_name

        with open(file_to_open) as input_file:
            return input_file.readlines()
    else:
        return None


def parse_rules(rules: list) -> dict:
    rules_dict = dict()
    parent = None

    for rule_collection in rules:
        bag_contents = dict()
        for rule in rule_collection:
            if rule[0].isdigit():
                split_rule = rule.split(',')

                for bags in split_rule:
                    split_bags = bags.split()
                    count = split_bags[0]
                    try:
                        colour = f"{split_bags[1]} {split_bags[2]}"
                    except IndexError:
                        colour = split_bags[1]
                    bag_contents[colour] = count
            elif rule.startswith('no'):
                continue
            else:
                parent = rule

        rules_dict[parent] = bag_contents

    return rules_dict


def process_bags() -> int:
    discovered, processed = ["shiny gold"], set()
    while discovered:
        checked = discovered.pop()
        prnts = {parent for child, parent in ancestors if child == checked}
        discovered.extend(prnts.difference(processed))
        processed.update(prnts)

    return len(processed)


def count_contents() -> int:
    discovered, contents = [("shiny gold", 1)], 0
    while discovered:
        checked = discovered.pop()
        for content in rule_dicts[checked[0]]:
            bag_count = int(rule_dicts[checked[0]][content]) * checked[1]
            discovered.append((content, bag_count))
            contents += bag_count

    return contents


if __name__ == '__main__':
    puzzle = open_puzzle("07-handy-haversacks.txt")

    rule_lists = [line.replace('\n', '').split(" bags contain ") for line in puzzle]
    rule_dicts = parse_rules(rule_lists)
    ancestors = {(subkey, key) for key in rule_dicts.keys() for subkey in rule_dicts[key]}

    print(process_bags())
    print(count_contents())
