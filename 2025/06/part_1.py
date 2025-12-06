import numpy as np

file = "live.txt"

worksheet_raw =  open(file).read().split("\n")
worksheet = []
for row in worksheet_raw:
    # slipt numbers separated by one or more spaces
    row = row.split()
    # convert to integers if possible
    row = [int(x) if x.isdigit() else x for x in row]
    worksheet.append(row)

# get last alement of worksheet and remove it from worksheet
operations = worksheet.pop()

# transpose worksheet to work with columns easily
worksheet = np.array(worksheet).T.tolist()

worksheet_rows = len(worksheet)
worksheet_cols = len(worksheet[0])

total = 0
for index in range(worksheet_rows):
    operator = operations[index]

    array_to_operate = worksheet[index]
    if operator == "+":
        row_total = np.sum(array_to_operate)
    elif operator == "*":
        row_total = np.prod(array_to_operate)
    total += row_total

print("Final Total after all operations:", total)