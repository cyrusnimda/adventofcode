#file = "demo.txt"
file = "live.txt"

reports = [list(map(int, line.split())) for line in open(file).read().split("\n") if line]

def is_report_safe(report):
    is_asc = (report[0] < report[1])
    is_safe = True
    #print(report, is_asc)
    for i in range(len(report)-1):
        difference = report[i] - report[i+1]
        #print(difference)
        if(abs(difference) > 3):
            is_safe = False
            return i+1
        if(is_asc and difference >= 0):
            is_safe = False
            return i+1
        if(not is_asc and difference <= 0):
            is_safe = False
            return i+1
    #print(is_safe)
    return is_safe

total_safe_reports = 0
for report in reports:
    #print(report)
    #print(is_report_safe(report))
    response = is_report_safe(report)
    if response == True:
        total_safe_reports += 1
        continue

    del report[response]
    #print("new ", report)
    
    #print(is_report_safe(report))
    if is_report_safe(report)==True:
        total_safe_reports += 1

    
print(total_safe_reports)