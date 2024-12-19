from functools import cmp_to_key    

with open('Day05/input') as file:
    raw_input = file.read()

# Creating the rules and updates
raw_rules, raw_updates = raw_input.split('\n\n')
rules_list = raw_rules.split('\n')
updates = [[int(num) for num in msg.strip().split(",")] for msg in raw_updates.split('\n')]

cmp = cmp_to_key(lambda a, b: 1-2*(f"{a}|{b}" in rules_list))

# Process the updates and calculate the sum
part1, part2 = 0, 0
for update in updates:
    update_sort = sorted(update, key=cmp)
    if update_sort == update:
        part1 += update[len(update) // 2] 
    else:
        part2 += update_sort[len(update_sort) // 2]  

print(part1, part2)