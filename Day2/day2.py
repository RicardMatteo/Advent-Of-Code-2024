input = open('Day2/input').read().split('\n')

def is_safe(report):
    diffs = [int(report[i + 1]) - int(report[i]) for i in range(len(report) - 1)]
    return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)

part1 = sum(is_safe(report.split()) for report in input)
part2 = sum(any(is_safe([level for i, level in enumerate(report.split()) if i != j]) for j in range(len(report.split()))) for report in input)

print(part1, part2)