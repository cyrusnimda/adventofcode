#file = "demo.txt"
file = "live.txt"

reports = [list(map(int, line.split())) for line in open(file).read().split("\n") if line]

def is_report_safe(report):
    is_asc = (report[0] < report[1])
    is_safe = True
    for i in range(len(report)-1):
        difference = report[i] - report[i+1]
        if(abs(difference) > 3):
            is_safe = False
            return i+1
        if(is_asc and difference >= 0):
            is_safe = False
            return i+1
        if(not is_asc and difference <= 0):
            is_safe = False
            return i+1
    return is_safe

total_safe_reports = 0
for report in reports:
    response = is_report_safe(report)
    if type(response) == type(True):
        total_safe_reports += 1
        continue

    reportCopy1 = report.copy()
    reportCopy2 = report.copy()
    reportCopy3 = report.copy()

    # delete element in position response
    del reportCopy1[response]
    del reportCopy2[0]
    del reportCopy3[response-1]

    if type(is_report_safe(reportCopy1)) == type(True) or type(is_report_safe(reportCopy2)) == type(True) or type(is_report_safe(reportCopy3)) == type(True):
        total_safe_reports += 1
    else:
        print(report)

    
print(total_safe_reports)