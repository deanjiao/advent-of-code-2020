def find_position(line: str, upper: int, up_char: str, down_char: str) -> int:
    """
    performs binary partitioning
    """
    my_lower = 0
    my_upper = upper
    for char in line:
        if char == up_char:
            my_lower = int((my_lower + my_upper) / 2) + 1
        elif char == down_char:
            my_upper = int((my_lower + my_upper) / 2)
    if line[-1] == up_char:
        return my_upper
    else:
        return my_lower

def part1(file_name: str) -> int:
    """
    finds max seat id
    """
    with open('day5/'+ file_name, 'r') as f:
        in_file = f.read().splitlines()

    max_seat_id = 0
    for line in in_file:
        row = find_position(line[:7], 127, 'B', 'F')
        col = find_position(line[-3:], 7, 'R', 'L')

        seat_id = row * 8 + col
        max_seat_id = max(seat_id, max_seat_id)
    return max_seat_id

print(part1('input.txt'))

def part2(file_name: str) -> int:
    """
    finds your seat id, the one empty seat in the middle
    """
    with open('day5/'+ file_name, 'r') as f:
        in_file = f.read().splitlines()

    seat_ids = []
    for line in in_file:
        row = find_position(line[:7], 127, 'B', 'F')
        col = find_position(line[-3:], 7, 'R', 'L')
        seat_id = row * 8 + col
        seat_ids += [seat_id]
    seat_ids.sort()
    for i in range(len(seat_ids) - 1):
        if seat_ids[i+1] - seat_ids[i] != 1:
            return seat_ids[i] + 1

print(part2('input.txt'))