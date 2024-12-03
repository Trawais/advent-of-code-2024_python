import os

def is_report_safe(report):
    # First let's figure out if the line is increasing or decreasing
    list_of_allowed_results = [1, 2, 3] if (report[0] < report[1]) else [-1, -2, -3]
    for i in range(1, len(report)):
        if report[i] - report[i-1] not in list_of_allowed_results:
            return False
    return True

# Task 1
with open(os.environ['INPUT_FILE']) as file:
    result_counter = 0
    for line in file:
        report_items = [int(i) for i in line.strip().split(' ')]
        if is_report_safe(report_items):
            result_counter += 1

print(f"First task result: {result_counter}")

# Task 2
with open(os.environ['INPUT_FILE']) as file:
    result_counter = 0
    for line in file:
        report_items = [int(i) for i in line.strip().split(' ')]

        for i in range(len(report_items)): # Try all possible solution with one bad level
            current_temp_report = [report_items[j] for j in range(len(report_items)) if j != i]
            if is_report_safe(current_temp_report):
                result_counter +=1
                break

print(f"Second task solution: {result_counter}")
