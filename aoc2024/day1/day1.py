def main():
    with open('data.txt') as data:
        left = []
        right = []
        inputs = data.read().splitlines()
        for input in inputs:
            dd = input.split('   ')
            left.append(int(dd[0]))
            right.append(int(dd[1]))

    left = sorted(left)
    right = sorted(right)

    sum = 0
    part2 = 0
    for ii in range(len(left)):
        n = left[ii]
        sum += abs(right[ii] - n)
        part2 += n * len(list(filter(lambda x: x == n, right)))

    print(sum)
    print(part2)


if __name__ == '__main__':
    main()
