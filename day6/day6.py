def part1(file_name: str) -> int:
    """
    return sum of counts for groups
    groups are separated by blank lines
    """
    with open('day6/'+ file_name, 'r') as f:
        in_file = f.read()

    groups = in_file.split('\n\n')
    count_sum = 0
    for group in groups:
        people = group.split('\n')
        count = 0
        questions = {}
        for person in people:
            for question in person:
                questions[question] = True
        count = len(questions)
        count_sum += count
    return count_sum

print(part1('input.txt'))

def part2(file_name: str) -> int:
    """
    return sum of counts for groups where everyone said yes
    """
    with open('day6/'+ file_name, 'r') as f:
        in_file = f.read()

    groups = in_file.rstrip().split('\n\n')
    count_sum = 0
    for group in groups:
        people = group.split('\n')
        questions = {}
        for person in people:
            for question in person:
                if question in questions.keys():
                    questions[question] += 1
                else:
                    questions[question] = 1
        
        count = 0
        for yes_count in questions.values():
            if yes_count == len(people):  # everyone answered yes for that question
                count += 1
        count_sum += count
    return count_sum

print(part2('input.txt'))