from functools import cmp_to_key

def is_in_correct_order(rules, numbers):
    for rule in rules:
        if numbers.count(rule[0]) > 0 and numbers.count(rule[1]):
            if numbers.index(rule[0]) > numbers.index(rule[1]):
                return False

    return True


def sort(rules, numbers: [int]):
    def compare(item1, item2):
        for rule in rules:
            if rule.count(item1) <= 0 or rule.count(item2) <= 0:
                continue
            return rule.index(item1) - rule.index(item2)

        return 0

    return list(sorted(numbers, key=cmp_to_key(compare)))


def main():

    rules = []
    numbers_list = []

    with open('data.txt') as data:
        for line in data.read().splitlines():
            if line.count('|') > 0:
                dd = line.split('|')
                rules.append([int(dd[0]), int(dd[1])])
            if line.count(',') > 0:
                numbers_list.append([(int(n)) for n in line.split(',')])


    p1_sum = 0
    p2_sum = 0
    for numbers in numbers_list:
        if is_in_correct_order(rules, numbers):
            p1_sum += numbers[len(numbers)//2]
        else:
            ordered_numbers = sort(rules, numbers)
            p2_sum += ordered_numbers[len(ordered_numbers)//2]

    print(p1_sum)
    print(p2_sum)


if __name__ == '__main__':
    main()
