import os

with open(os.environ['INPUT_FILE']) as file:
    first = []
    second = []
    for line in file:
        item_1, item_2 = line.strip().split("   ")
        first.append(int(item_1))
        second.append(int(item_2))

first.sort()
second.sort()

sum = 0
for i in range(len(first)):
    sum += abs(first[i] - second[i])
print(f"First task result: {sum}")

# Task 2
sum_2 = 0
counter_second = {i:second.count(i) for i in second}
for item in first:
    sum_2 += ( item * counter_second.get(item, 0) )

print(f"Second task result: {sum_2}")
