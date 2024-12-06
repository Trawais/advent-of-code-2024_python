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
print(f"original content length: {len(content)}")
