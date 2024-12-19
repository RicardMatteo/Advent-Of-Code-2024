import re
with open('Day07/input') as file:
    raw_input = file.read().split('\n')

part1, part2 = 0, 0

remove_suffix = lambda a,b: int(str(a)[:-len(str(b))] if a!=b else 0)

def solve(res, numbers, part2=False):
    *numbers, tail = numbers
    
    if not numbers:
        return tail == res
    
    if res-tail >= 0 and solve(res-tail, numbers, part2):
        return True
    
    q,r = divmod(res, tail)
    if r == 0 and solve(q, numbers, part2) and (res !=0 or tail ==1):
        return True
    
    if part2 and str(res).endswith(str(tail)) and solve(remove_suffix(res,tail), numbers, part2):
        return True
    
    return False

for line in raw_input:
    res, *numbers = map(int, re.split(': | ', line))
    
    part1 += res if solve(res, numbers) else 0
    part2 += res if solve(res, numbers, True) else 0

print(part1, part2)