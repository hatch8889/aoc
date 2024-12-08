import collections
import itertools


def main():
    max_y = 0
    max_x = 0

    antenae = collections.defaultdict(list)

    with open('data.txt') as data:
        lines = data.read().splitlines()
        max_y = len(lines)
        for y in range(max_y):
            line = lines[y]
            max_x = len(line)
            for x in range(max_x):
                c = line[x]
                if c != '.':
                    antenae[c].append(complex(x, y))

    part_1 = set()
    part_2 = set()

    def in_grid(pos: complex):
        if pos.real < 0 or pos.imag < 0:
            return False
        if pos.real >= max_x or pos.imag >= max_y:
            return False
        return True

    for ant in antenae:
        for a1, a2 in itertools.combinations(antenae[ant], 2):
            d = a2 - a1

            new_pos = a2 + d
            if in_grid(new_pos):
                part_1.add(new_pos)

            new_pos = a1 - d
            if in_grid(new_pos):
                part_1.add(new_pos)

            for n in range(0, 50):
                new_pos = a2 + d * n
                if in_grid(new_pos):
                    part_2.add(new_pos)
                else:
                    break

            for n in range(0, 50):
                new_pos = a1 - d * n
                if in_grid(new_pos):
                    part_2.add(new_pos)
                else:
                    break

    print(len(part_1))
    print(len(part_2))


if __name__ == '__main__':
    main()

