lines = open('Day01/input').read().split('\n')

part1 = sum(abs(l - r) for l, r in zip(*map(sorted, zip(*[map(int, line.split()) for line in lines]))))
part2 = sum(int(x) * r.count(x) for l, r in [zip(*map(str.split, lines))] for x in l)

print(part1)
print(part2)