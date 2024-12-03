import re

input = open('Day3/input').read().split('\n')

part1 = sum([eval(match[2].replace('mul', '').replace(',', '*')) for match in re.findall(r"(don\'t\(\))|(do\(\))|(mul\(\d+,\d+\))", str(input)) if match[2]])

part2 = sum(eval(match[2].replace('mul', '').replace(',', '*')) for match in re.findall(r"(don\'t\(\))|(do\(\))|(mul\(\d+,\d+\))", "do()"+ str(input)) if (do := (match[1] or (do and not match[0]))) and match[2])

print(part1, part2)