import re

def part1(file_name: str) -> int:
    """
    detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

    Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. 
    Passports are separated by blank lines.
    """
    with open('day4/'+ file_name, 'r') as f:
        in_file = f.read()
    
    passports = in_file.split('\n\n')  # Passports are separated by blank lines.
    valid_count = 0
    for passport in passports:
        keys_and_values = passport.replace('\n', ' ').split(' ')
        contains_cid = False
        key_count = 0

        if len(keys_and_values) < 7:
            continue

        for item in keys_and_values:
            key = item.split(':')[0]
            if key == 'cid':
                contains_cid = True
            key_count += 1
        if (key_count == 7 and not contains_cid) or key_count == 8:
            valid_count += 1
    return valid_count

# print(part1('input.txt'))

def test(keys_and_values: str):
    contains_cid = False
    key_count = 0
    for item in keys_and_values:
        key_value_pair = item.split(':')
        if len(key_value_pair) != 2:
            continue
        # print(key_value_pair)
        key = key_value_pair[0]
        value = key_value_pair[1]

        if key == 'byr' and (int(value) < 1920 or int(value) > 2002):
            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            continue
        elif key == 'iyr' and (int(value) < 2010 or int(value) > 2020):
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            continue
        elif key == 'eyr' and (int(value) < 2020 or int(value) > 2030):
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            continue
        elif key == 'hgt':
            # hgt (Height) - a number followed by either cm or in:
            #     If cm, the number must be at least 150 and at most 193.
            #     If in, the number must be at least 59 and at most 76.
            measurement = value[-2:]
            height = value[:-2]
            if (measurement == 'cm' and (int(height) < 150 or int(height) > 193)) or \
                (measurement == 'in' and (int(height) < 59 or int(height) > 76)):
                continue
        elif key == 'hcl':
            # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
            if value[0] != '#' or len(value) != 7:
                continue
            try:
                hex(int(value[-6:], 16))
            except ValueError:
                continue
        elif key == 'ecl' and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
            continue
        elif key == 'pid':
            # pid (Passport ID) - a nine-digit number, including leading zeroes.
            if len(value) != 9:
                continue
            try:
                int(value)
            except ValueError:
                continue
        elif key == 'cid':  # cid (Country ID) - ignored, missing or not.
            contains_cid = True
        key_count += 1
    return key_count

print(test(['cid:003456789']))
print(test(['hgt:150cm']))
print(test(['hgt:194cm']))
print(test(['hgt:58in']))
print(test(['hgt:76in']))
print(test(['hgt:77in']))

# yknow i should have used re here
def part2(file_name: str) -> int:
    """
    more restrictions on the value of each field
    
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    """
    with open('day4/'+ file_name, 'r') as f:
        in_file = f.read()
    
    passports = in_file.split('\n\n')  # Passports are separated by blank lines.
    valid_count = 0
    for passport in passports:
        keys_and_values = re.split("\n| ", passport)
        contains_cid = False
        key_count = 0
        # print(keys_and_values)
        if len(keys_and_values) < 7:
            continue

        for item in keys_and_values:
            key_value_pair = item.split(':')
            if len(key_value_pair) != 2:
                continue
            # print(key_value_pair)
            key = key_value_pair[0]
            value = key_value_pair[1]

            if key == 'byr' and (int(value) < 1920 or int(value) > 2002):
                # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                continue
            elif key == 'iyr' and (int(value) < 2010 or int(value) > 2020):
                # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                continue
            elif key == 'eyr' and (int(value) < 2020 or int(value) > 2030):
                # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                continue
            elif key == 'hgt':
                # hgt (Height) - a number followed by either cm or in:
                #     If cm, the number must be at least 150 and at most 193.
                #     If in, the number must be at least 59 and at most 76.
                measurement = value[-2:]
                height = value[:-2]
                if (measurement == 'cm' and (int(height) < 150 or int(height) > 193)) or \
                    (measurement == 'in' and (int(height) < 59 or int(height) > 76)) or \
                    (measurement not in ['cm', 'in']):
                    continue
            elif key == 'hcl':
                # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                if value[0] != '#' or len(value) != 7:
                    continue
                try:
                    hex(int(value[-6:], 16))
                except ValueError:
                    continue
            elif key == 'ecl' and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                continue
            elif key == 'pid':
                # pid (Passport ID) - a nine-digit number, including leading zeroes.
                if len(value) != 9:
                    continue
                try:
                    int(value)
                except ValueError:
                    continue
            elif key == 'cid':  # cid (Country ID) - ignored, missing or not.
                contains_cid = True
            key_count += 1
        if (key_count == 7 and not contains_cid) or key_count == 8:
            valid_count += 1
    return valid_count

print(part2('input.txt'))