def main():
    max_y = 0
    max_x = 0
    bricks = []
    position = None
    direction = 0  # up

    directions = [
        (0, -1),  # up
        (1, 0),  # right
        (0, 1),  # down
        (-1, 0),  #left
    ]

    visited = set()

    with open('data.txt') as data:
        lines = data.read().splitlines()
        max_y = len(lines)
        for y in range(max_y):
            line = lines[y]
            max_x = len(line)
            for x in range(max_x):
                if line[x] == '#':
                    bricks.append((x, y))
                elif line[x] == '^':
                    position = (x, y)

    def out_of_bound(cur):
        if cur[0] < 0 or cur[1] < 0:
            return True
        if cur[0] >= max_x or cur[1] >= max_y:
            return True
        return False

    def move(cur_pos, cur_dir):
        dd = directions[cur_dir]
        return (cur_pos[0] + dd[0]), (cur_pos[1] + dd[1])

    def rotate(cur_dir):
        return (cur_dir + 1) % 4

    def check_wall(cur_pos, cur_dir):
        pos = cur_pos
        loop_visited = set()
        while True:
            visited.add(pos)
            comb = (pos[0], pos[1], cur_dir)
            if comb in loop_visited:
                return False
            loop_visited.add(comb)
            next_position = move(pos, cur_dir)
            if out_of_bound(next_position):
                return True
            if next_position in bricks:
                cur_dir = rotate(cur_dir)
                continue
            pos = next_position
        return False

    check_wall(position, direction)

    print(len(visited))

    part_2 = set()
    for obstacle in list(visited):
        bricks.append(obstacle)
        res = check_wall(position, direction)
        if not res:
            part_2.add(obstacle)

        bricks.remove(obstacle)

    print(len(part_2))

if __name__ == '__main__':
    main()
