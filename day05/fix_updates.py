def init_rules():
    with open("./page_ordering_rules.txt") as file:
        lines = file.read().splitlines()
        list_of_rules = [tuple(line.split("|")) for line in lines]
        after_rules = dict()
        for rule in list_of_rules:
            if rule[1] not in after_rules:
                after_rules[rule[1]] = []
            after_rules[rule[1]].append(rule[0])
    return after_rules


def init_updates():
    with open("./page_produce_updates.txt") as file:
        lines = file.read().splitlines()
        updates = [line.split(",") for line in lines]
    return updates


def get_middle_page_number(update):
    update_len = len(update)
    return int(update[update_len // 2])


def get_middle_page_number_sum(updates):
    middle_page_number_sum = 0
    for update in updates:
        middle_page_number_sum += get_middle_page_number(update)
    return middle_page_number_sum


def swap(update, idx, error_idx):
    tmp = update[idx]
    update[idx] = update[error_idx]
    update[error_idx] = tmp
    return update


def find_first_error(update, rules):
    for page in update:
        if page in rules:
            return page


def fix_if_bad(update, after_rules, bad_updates):
    idx = 0
    fixed = None
    while idx < len(update):
        page = update[idx]
        if page not in after_rules:
            idx += 1
        else:
            rules = after_rules[page]
            error = find_first_error(update[idx + 1 :], rules)
            if error is not None:
                error_idx = update.index(error)
                update = swap(update, idx, error_idx)
                fixed = update.copy()
                idx = 0
            else:
                idx += 1
    return fixed


def check_updates(updates, after_rules):
    bad_updates = []
    for update in updates:
        fixed = fix_if_bad(update, after_rules, bad_updates)
        if fixed is not None:
            bad_updates.append(fixed)
    return bad_updates


after_rules = init_rules()
updates = init_updates()

bad_updates = check_updates(updates, after_rules)
middle_page_number_sum = get_middle_page_number_sum(bad_updates)
print("Fixed updates middle page number sum is:", middle_page_number_sum)
