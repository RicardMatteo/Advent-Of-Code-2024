with open('Day16/input') as file:
    raw_input = file.read().split('\n')

part1, part2, start, end, grid, visited  = 999999, set(), 0, 0, {}, {}

for y, row in enumerate(raw_input):
    for x, c in enumerate(row):
        grid[(x + y * 1j)] = c
        if c == 'S':
            start = x + y * 1j
        if c == 'E':
            end = x + y * 1j

queue = [(start, 0, 1, [start])]
while queue:
    pos, cost, dir, path = queue.pop(0)
    if (pos,dir) in visited and visited[(pos,dir)] < cost:
        continue
    visited[(pos,dir)] = cost
    if pos == end:
        if cost < part1:
            part1 = cost
            part2 = set(path)
        elif cost == part1:
            part2.update(path)
        continue
    if grid.get(pos+dir, "#") != '#':
        queue.append((pos + dir, cost + 1, dir, path + [pos+ dir]))
    queue.append((pos, cost + 1000, dir * 1j, path))
    queue.append((pos, cost + 1000, dir * - 1j, path))
    
# print the grid
for y in range(len(raw_input)):
    for x in range(len(raw_input[0])):
        print('O' if x + y * 1j in part2 else grid.get(x + y * 1j, '#'), end = '')
    print()

print(part1, len(part2))