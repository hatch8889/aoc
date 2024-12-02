def is_safe(line):
    decreasing: bool | None = None
    for n in range(1, len(line)):
        a = line[n - 1]
        b = line[n]
        if a == b:
            return False

        if decreasing is None:
            decreasing = a > b

        if decreasing:
            diff = a - b
        else:
            diff = b - a

        if diff > 3:
            return False
        if diff <= 0:
            return False
    return True


def is_safe_p2(line):
    for n in range(len(line)):
        if is_safe(line[:n] + line[n+1:]):
            return True

    return False


def main():
    lines = []

    with open('data.txt') as data:
        inputs = data.read().splitlines()
        for input in inputs:
            dd = input.split(' ')
            line = []
            for n in dd:
                line.append(int(n))
            lines.append(line)

    part1 = 0
    part2 = 0
    for line in lines:
        if is_safe(line):
            part1 += 1
            part2 += 1
        elif is_safe_p2(line):
            part2 += 1

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
