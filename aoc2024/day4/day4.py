import itertools

def main():
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    word = 'XMAS'

    with open('data.txt') as data:
        inputs = data.read().splitlines()
        max = len(inputs)

        def check_bounds(xx, yy):
            if xx < 0 or xx >= max:
                return False
            if yy < 0 or yy >= max:
                return False
            return True

        def find_word(xx: int, yy: int, direction: tuple[int, int]):
            for ii in range(len(word)):
                xn = xx + (ii * direction[0])
                yn = yy + (ii * direction[1])
                if not check_bounds(xn, yn):
                    return False
                letter = inputs[yn][xn]
                if letter != word[ii]:
                    return False
            return True

        part_1 = 0
        for x in range(max):
            for y in range(max):
                for d in directions:
                    if find_word(x, y, d):
                        part_1 += 1

        print(part_1)




if __name__ == '__main__':
    main()
