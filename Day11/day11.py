import functools
from math import log10


with open('Day11/input') as file:
    stones = file.read().split()

@functools.cache
def cacl_stone(stone, n):
    
    if n == 0: return 1
    
    if stone == 0: return cacl_stone(1, n - 1)
    
    d = int(log10(stone))+1
    if d % 2 == 0:
        pow10 = 10 ** (d // 2)
        return cacl_stone(stone // pow10, n - 1) + cacl_stone(stone % pow10, n - 1)
        
    return cacl_stone(stone * 2024, n - 1)
    
print(sum(cacl_stone(int(stone), 25) for stone in stones), \
    sum(cacl_stone(int(stone), 75) for stone in stones))
