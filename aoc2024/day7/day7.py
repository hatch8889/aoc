def is_true(finish: int, s: int, elements: list[int]):
    if len(elements) == 0:
        return s == finish

    r = is_true(finish, s + elements[0], elements[1:])
    if r:
        return True

    return is_true(finish, s * elements[0], elements[1:])


def is_true_p2(finish: int, s: int, elements: list[int]):
    if len(elements) == 0:
        return s == finish

    r = is_true_p2(finish, s + elements[0], elements[1:])
    if r:
        return True

    r = is_true_p2(finish, s * elements[0], elements[1:])
    if r:
        return True

    return is_true_p2(finish, int(str(s) + str(elements[0])), elements[1:])


def main():
    guides = []

    with open('data.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            parts1 = line.split(': ')
            parts2 = parts1[1].split(' ')
            g = list(map(int, parts2))
            guides.append((int(parts1[0]), g))

    part_1 = 0
    part_2 = 0
    for g in guides:
        if is_true(g[0], 0, g[1]):
            part_1 += g[0]
        if is_true_p2(g[0], 0, g[1]):
            part_2 += g[0]

    print(part_1)
    print(part_2)


if __name__ == '__main__':
    main()
