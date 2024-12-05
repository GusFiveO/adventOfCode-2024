def init_rules():
    with open("./page_ordering_rules.txt") as file:
        lines = file.read().splitlines()
        list_of_rules = [tuple(line.split("|")) for line in lines]
        before_rules = dict()
        after_rules = dict()
        for rule in list_of_rules:
            if rule[0] not in before_rules:
                before_rules[rule[0]] = []
            before_rules[rule[0]].append(rule[1])
            if rule[1] not in after_rules:
                after_rules[rule[1]] = []
            after_rules[rule[1]].append(rule[0])
    return before_rules, after_rules


def init_updates():
    with open("./page_produce_updates.txt") as file:
        lines = file.read().splitlines()
        updates = [line.split(",") for line in lines]
    return updates


def check_forward(update, idx, after_rules):
    if update[idx] not in after_rules:
        return True
    rules = after_rules[update[idx]]
    for page in update[idx + 1 :]:
        if page in rules:
            print(f"{update[idx]} should be after {page}")
            return False
    return True


def check_backward(update, idx, before_rules):
    if update[idx] not in before_rules:
        return True
    rules = before_rules[update[idx]]
    for page in update[:idx]:
        if page in rules:
            print(f"{update[idx]} should be before {page}")
            return False
    return True


def get_middle_page_number(update):
    update_len = len(update)
    return int(update[update_len // 2])


def check_updates(updates, before_rules, after_rules):
    count = 0
    for update in updates:
        error = False
        for idx, page in enumerate(update):
            if not check_forward(update, idx, after_rules) or not check_backward(
                update, idx, before_rules
            ):
                error = True
                break
        if not error:
            count += get_middle_page_number(update)
    return count


before_rules, after_rules = init_rules()
updates = init_updates()

middle_page_number_sum = check_updates(updates, before_rules, after_rules)
print("Valid updates middle page number sum is:", middle_page_number_sum)
