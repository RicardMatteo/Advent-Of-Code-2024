import re

input = open('Day03/input').read().split('\n')

pattern = r"(don\'t\(\))|(do\(\))|(mul\(\d+,\d+\))"
matches = re.findall(pattern, str(input))

do = True
part1, part2 = 0, 0
for match in matches:
    do = match[1] or (do and not match[0])
    part1 += eval(match[2].replace('mul', '').replace(',', '*')) if match[2] else 0
    part2 += eval(match[2].replace('mul', '').replace(',', '*')) if do and match[2] else 0

print(part1, part2)