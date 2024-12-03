import re 

#file = "demo2.txt"
file = "live.txt"

memory =  open(file).read()
#print(memory)

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)", memory)
#print(matches)

total = 0
do = True
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    else:
        if do:
            numbers = list(map(int, re.findall(r"\d{1,3}", match)))
            result = numbers[0] * numbers[1]
            total += result

print("total=",total)
   