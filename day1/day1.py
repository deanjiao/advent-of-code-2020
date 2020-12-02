def part1() -> int:
    """
    find the two entries that sum to 2020, then multiply them together
    """

    with open('day1/input.txt', 'r') as f:
        lines = f.read().splitlines()

    for x in lines:
        for y in lines:
            if int(x) + int(y) == 2020:
                print(x, y)
                mult = int(x) * int(y)
                return mult
print(part1())

def part2() -> int:
    """
    Find 3 numbers that sum to 2020
    """

    with open('day1/input.txt', 'r') as f:
        lines = f.read().splitlines()

    for x in lines:
        for y in lines:
            for z in lines:
                if int(x) + int(y) + int(z) == 2020:
                    print(x, y, z)
                    mult = int(x) * int(y) * int(z)
                    return mult
print(part2())