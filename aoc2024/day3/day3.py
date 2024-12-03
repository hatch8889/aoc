import re


def main():
    with open('data.txt') as data:
        out = re.findall(r'mul\(\d{1,5}\,\d{1,5}\)|do\(\)|don\'t\(\)', data.read())
        sum_p1 = 0
        sum_p2 = 0
        enabled = True
        for expr in out:
            parts = re.split(r'(\d{1,5})\,(\d{1,5})', expr)
            if parts[0] == 'do()':
                enabled = True
            elif parts[0] == 'don\'t()':
                enabled = False
            elif parts[0].startswith('mul'):
                sum_p1 += int(parts[1]) * int(parts[2])
                if enabled:
                    sum_p2 += int(parts[1]) * int(parts[2])

        print(sum_p1)
        print(sum_p2)


if __name__ == '__main__':
    main()
