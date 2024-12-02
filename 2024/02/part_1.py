#file = "demo.txt"
file = "live.txt"

reports = [list(map(int, line.split())) for line in open(file).read().split("\n") if line]

def is_report_safe(report):
    is_asc = (report[0] < report[1])
    is_safe = True
    print(report, is_asc)
    for i in range(len(report)-1):
        difference = report[i] - report[i+1]
        #print(difference)
        if(abs(difference) > 3):
            is_safe = False
            break
        if(is_asc and difference >= 0):
            is_safe = False
            break
        if(not is_asc and difference <= 0):
            is_safe = False
            break
    #print(is_safe)
    return is_safe

total_safe_reports = 0
for report in reports:
    if is_report_safe(report):
        total_safe_reports += 1

    
print(total_safe_reports)