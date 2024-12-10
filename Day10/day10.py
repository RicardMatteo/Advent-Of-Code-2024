with open('Day10/input') as file:
    raw_input = file.read().split('\n')

starts, grid, known_p1, known_p2 =[], {}, {}, {}

# Parse input
for y,line in enumerate(raw_input):
    for x, c in enumerate(line):
        grid[x+1j*y] = int(c)
        if c == '0':
            starts.append(x+1j*y)


def find_path(pos, current_value):
    # known paths
    if pos in known_p1:
        return len(known_p1[pos]), known_p2[pos]
   
    # end of path
    if grid.get(pos) == 9:
        known_p1[pos] = {pos}
        known_p2[pos] = 1
        return 1,1
   
    # find in neighbors 
    p1, p2 = set(), 0
    for npos in [pos + 1, pos -1, pos + 1j, pos -1j]:
        if grid.get(npos) == current_value + 1:
            p2 += find_path(npos, current_value + 1)[1]
            p1.update(known_p1.get(npos))
   
    # update known paths
    known_p1[pos] = p1
    known_p2[pos] = p2
   
    return len(p1), p2

part1, part2 = map(sum, zip(*(find_path(start, 0) for start in starts)))
print(part1, part2)