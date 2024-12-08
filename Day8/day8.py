import itertools

with open('Day8/input') as file:
    raw_input = file.read().split('\n')

map = {x + y * 1j: val for y, line in enumerate(raw_input) for x, val in enumerate(line)}

antinodes_part1, antinodes_part2 = set(), set()
antennas = {}

for pos, val in map.items():
    if val != '.':
        antennas.setdefault(val, []).append(pos)


def check_antinodes(loc1, loc2, antinodes, part1=False):
    diff = loc2 - loc1
    
    while loc1-diff in map:
        antinodes.add((loc1-diff))
        if part1:
            break
        loc1 -= diff

    while loc2+diff in map:
        antinodes.add((loc2+diff))
        if part1:
            break
        loc2 += diff
    
    if not part1:
        antinodes.add(loc1)
        antinodes.add(loc2)

for antenna in antennas:
    for loc, loc2 in itertools.combinations(antennas[antenna], 2):
        check_antinodes(loc, loc2, antinodes_part1, True)
        check_antinodes(loc, loc2, antinodes_part2, False)

print(len(antinodes_part1), len(antinodes_part2))