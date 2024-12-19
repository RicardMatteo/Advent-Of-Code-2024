with open('Day06/input') as file:
    raw_input = file.read().split('\n')

part1, part2, start, dir, grid = 0, 0, (0,0), 0, {}

for y,line in enumerate(raw_input):
    for x, c in enumerate(line):
        grid[x+1j*y] = c
        if c == '^':
            start = x+1j*y
            dir = -1j

def check_for_loop(pos, dir, hits, added_wall=None):
    while pos in grid:
        if (pos+dir,dir) in hits:
            return True
        
        while grid.get(pos + dir) == '#' or (pos + dir) == added_wall:
            hits.add((pos+dir, dir))        
            dir = dir*1j
    
        pos += dir
    return False

hits = set()
added = []
pos = start
while pos in grid:    
    part1 += (1 if grid.get(pos) != 'X' else 0)
    grid[pos] = 'X'
    npos = pos + dir
    
    while grid.get(npos) == '#':
        # Turn
        hits.add((npos,dir))
        dir = dir*1j
        npos = pos + dir

    if (grid.get(npos) != 'X') and npos not in added:
        hits_bis = hits.copy()
        loop = check_for_loop(pos, dir, hits_bis, npos)
        if loop:
            added.append(npos)
            part2 += 1

    pos = npos

print(part1, part2)