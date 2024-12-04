import itertools


def main():
    d1 = [
        (-1, -1),
        (0, 0),
        (1, 1)
    ]
    d2 = [
        (-1, 1),
        (0, 0),
        (1, -1),
    ]

    word = 'MAS'
    word2 = 'SAM'

    with open('data.txt') as data:
        inputs = data.read().splitlines()
        max = len(inputs)

        def is_hit(xx: int, yy: int):
            w1 = ''
            for d in d1:
                w1 += inputs[yy + d[1]][xx + d[0]]
            if w1 != word and w1 != word2:
                return False

            w2 = ''
            for d in d2:
                w2 += inputs[yy + d[1]][xx + d[0]]
            if w2 != word and w2 != word2:
                return False

            return True

        part_1 = 0
        for x in range(1, max - 1):
            for y in range(1, max - 1):
                if is_hit(x, y):
                    part_1 += 1
        print(part_1)


if __name__ == '__main__':
    main()
