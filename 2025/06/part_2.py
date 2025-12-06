import numpy as np
file = "live.txt"

worksheet_raw =  open(file).read().split("\n")
# get array of chars
worksheet = [list(line) for line in worksheet_raw] 

# transpose rows and columns
worksheet = zip(*worksheet)

#convert tuple in list
worksheet = [list(row) for row in worksheet]

final_worksheet = []
temp_row = {
    "operator": "",
    "numbers": []
}
for row in worksheet:
    str_row = "".join(row)
    if str_row.strip() == "":
        final_worksheet.append(temp_row)
        temp_row = {
            "operator": "",
            "numbers": []
        }
        continue

    operator = row.pop().strip()
    numbers = int("".join(row))
    
    if operator:
        temp_row["operator"] = operator
        
    temp_row["numbers"].append(numbers)

# append last row if not already appended
final_worksheet.append(temp_row)


total = 0
for entry in final_worksheet:
    operator = entry["operator"]
    numbers = entry["numbers"]
    if operator == "+":
        row_total = np.sum(numbers)
    elif operator == "*":
        row_total = np.prod(numbers)
    total += row_total
    
print("Final Total after all operations:", total)