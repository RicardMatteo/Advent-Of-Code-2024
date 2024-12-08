lines = open('Day4/input').read().split('\n')

directions = [1, 1j, -1, -1j, 1 + 1j, -1 - 1j, 1 - 1j, -1 + 1j]

coords = {x + y * 1j: val for y, line in enumerate(lines) for x, val in enumerate(line)}

g = lambda pos, d, k : coords.get((pos + k * d), ".")

p1, p2 = 0, 0

for pos in coords:

    p1 += sum(all(g(pos,d,k)== "XMAS"[k] for k in range(4)) for d in directions)

    p2 += g(pos,0,0) == 'A' and all(sum(map(ord,[g(pos,d,1), g(pos,d,-1)])) == ord('M') + ord('S') for d in [1+1j,1-1j])

print(p1, p2)
