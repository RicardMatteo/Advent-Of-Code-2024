from functools import lru_cache

with open('Day19/input') as file:
    raw_input = file.read().split('\n')

def count(towels, pattern):
    @lru_cache
    def rec(pattern):
        if pattern == '':
            return 1  # Une possibilité trouvée
        tot = 0
        for towel in towels:
            if pattern.startswith(towel):
                tot += rec(pattern[len(towel):])
        return tot
    return rec(pattern)

towels,patterns = tuple(raw_input[0].split(', ')), raw_input[2:]
solution = [count(towels, p) for p in patterns]
print(sum(c > 0 for c in solution), sum(solution), sep='\n')
