def part1(file_name: str) -> int:
    """
    find how many valid passwords there are
    valid example: 1-3 a: abcde
    'a' must occur 1-3 times in the password
    invalid example: 1-3 b: cdefg
    """

    with open('day2/'+ file_name, 'r') as f:
        lines = f.read().splitlines()

    valid_count = 0
    for line in lines:
        tokens = line.split(' ')
        count_range = tokens[0].split('-')
        count_range_lower = int(count_range[0])
        count_range_upper = int(count_range[1])
        test_letter = tokens[1][0]
        password = tokens[2]
        current_count = 0
        for letter in password:
            if letter == test_letter:
                current_count += 1
        if current_count >= count_range_lower and current_count <= count_range_upper:
            valid_count += 1

    return valid_count

print(part1('input.txt'))


def part2(file_name: str) -> int:
    """
    exactly 1 position of the two listed must contain the test letter
    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    """
    # (a and not b) or (not a and b)
    with open('day2/'+ file_name, 'r') as f:
        lines = f.read().splitlines()

    valid_count = 0
    for line in lines:
        tokens = line.split(' ')
        indexes = tokens[0].split('-')
        index_lower = int(indexes[0])
        index_upper = int(indexes[1])
        test_letter = tokens[1][0]
        password = tokens[2]
        if (password[index_lower - 1] == test_letter and not password[index_upper - 1] == test_letter) \
            or (not password[index_lower - 1] == test_letter and password[index_upper - 1] == test_letter):
            valid_count += 1

    return valid_count

print(part2('input.txt'))