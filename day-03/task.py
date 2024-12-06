import os
import re

with open(os.environ['INPUT_FILE']) as file:
    content = file.read()

# First task
def sum_all_mul_actions(content):
    sum = 0
    for x in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', content):
        sum += int(x.group(1)) * int(x.group(2))
    return sum

sum = sum_all_mul_actions(content)

print(f"First task solution: {sum}")

# Second task
# First we need to trim the end of the file where there is "don't()" but there is no more "do()" function to enable the calculation again

splitted_by_dont = content.split("don't()")
sum_2 = sum_all_mul_actions(splitted_by_dont[0])
for i in range(1, len(splitted_by_dont)):
    if 'do()' in splitted_by_dont[i]:
        temp = splitted_by_dont[i].split('do()', 1)[1]
        sum_2 += sum_all_mul_actions(temp)

print(f"Second task: {sum_2}")
