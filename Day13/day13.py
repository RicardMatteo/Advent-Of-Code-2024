with open('Day13/input') as file:
    raw_input = file.read().split('\n\n')

part1, part2 = 0, 0
parse = lambda comb: map(int, [c[2:] for c in comb.split(': ')[1].split(', ')])

def find_minimum(X1, Y1, X2, Y2, X3, Y3):
    det = X1 * Y2 - Y1 * X2
  
    if det == 0: return None  # No solution
    
    a = (X3 * Y2 - Y3 * X2) / det
    b = (X1 * Y3 - Y1 * X3) / det

    if a.is_integer() and b.is_integer(): 
        return abs(int(a)), abs(int(b))

for block in raw_input:
    (X1, Y1), (X2, Y2), (X3, Y3) = [parse(comb) for comb in block.split('\n')]

    res = find_minimum(X1, Y1, X2, Y2, X3, Y3)
    res2 = find_minimum(Y1, X1, Y2, X2, Y3 + 10**13, X3 + 10**13)
    
    part1 += res[0]*3 + res[1] if res and all([x <= 100 for x in res]) else 0
    part2 += res2[0]*3 + res2[1] if res2 else 0

print(part1, part2)