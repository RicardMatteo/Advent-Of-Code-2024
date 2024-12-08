with open('Day6/input') as file:
    raw_input = file.read().split('\n')

    
part1, part2 = 0, 0
start = (0,0)
dir = 0
map = {}
for y,line in enumerate(raw_input):
    for x, c in enumerate(line):
        map[x+1j*y] = c
        if c == '^':
            start = x+1j*y
            dir = -1j
        


def check_for_loop(pos, dir, hits, added_wall=None):
    while pos in map:
        if (pos+dir,dir) in hits:
            return True
        
        while map.get(pos + dir) == '#' or (pos + dir) == added_wall:
            hits.add((pos+dir, dir))        
            dir = dir*1j
    
        pos += dir
    return False
        
hits = set()
added = []
pos = start
while pos in map:
    
    part1 += (1 if map.get(pos) != 'X' else 0)
    map[pos] = 'X'
    npos = pos + dir
    
    while map.get(npos) == '#':
        # Turn
        hits.add((npos,dir))
        dir = dir*1j
        npos = pos + dir

    if (map.get(npos) != 'X') and npos not in added:
        hits_bis = hits.copy()
        loop = check_for_loop(pos, dir, hits_bis, npos)
        if loop:
            added.append(npos)
            part2 += 1
            
    pos = npos


print(part1, part2)