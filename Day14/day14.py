from collections import defaultdict
import re

with open('Day14/input') as file:
    raw_input = file.read().split('\n')

wide, height, sec = 101, 103, 100
quad1, quad2, quad3, quad4 = 0, 0, 0, 0
robots = []

for line in raw_input:
    x,y,dx,dy = map(int, re.findall(r'-?\d+', line))
    robots.append((x,y,dx,dy))
    # part 1
    x = (x + sec * dx) % wide
    y = (y + sec * dy) % height

    if   x < wide//2 and y < height//2: quad1 += 1
    elif x > wide//2 and y < height//2: quad2 += 1
    elif x < wide//2 and y > height//2: quad3 += 1
    elif x > wide//2 and y > height//2: quad4 += 1

sec = 0
while True: # part 2
    positions = defaultdict(int)
    collision_found = False

    for x, y, dx, dy in robots:
        x_current = (x + dx * sec) % wide
        y_current = (y + dy * sec) % height
        positions[(x_current, y_current)] += 1

        if positions[(x_current, y_current)] > 1:
            collision_found = True
            break
        
    if not collision_found: 
        grid = [['#' if positions[i,j] == 1 else "." for i in range(wide)] for j in range(height)]
        for row in grid: print(''.join(row))
        break

    sec += 1

print(quad1 * quad2 * quad3 * quad4, sec)