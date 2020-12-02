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