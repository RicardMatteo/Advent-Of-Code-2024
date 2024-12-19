from functools import lru_cache

with open('Day19/input') as file:
    raw_input = file.read().split('\n')

@lru_cache
def count(pattern):
    if pattern == '': return 1
    return sum(count(pattern[len(towel):]) for towel in towels if pattern.startswith(towel))

towels,patterns = raw_input[0].split(', '), raw_input[2:]
solution = [count(p) for p in patterns]
print(sum(c > 0 for c in solution), sum(solution), sep='\n')