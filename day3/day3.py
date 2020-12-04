def part1(file_name: str, right: int, down: int) -> int:
    """
    return the number of trees (#) along the slope:
    right 3, down 1
    """

    with open('day3/'+ file_name, 'r') as f:
        lines = f.read().splitlines()

    count = 0
    x = 0
    y = 0
    size_x = len(lines[0])
    size_y = len(lines)
    while True:
        if y >= size_y - 1:
            break

        x = (x + right) % size_x
        y += down
        # print(x, y, lines[y][x])
        if lines[y][x] == '#':
            count += 1
    return count

print(part1('input.txt', 3, 1))

def part2(file_name: str) -> int:
    """
    Multiply the tree counts for the following slopes:
    Right 1, down 1.
    Right 3, down 1.
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    x1 = part1(file_name, 1, 1)
    x2 = part1(file_name, 3, 1)
    x3 = part1(file_name, 5, 1)
    x4 = part1(file_name, 7, 1)
    x5 = part1(file_name, 1, 2)
    return x1 * x2 * x3 * x4 * x5

print(part2('input.txt'))
