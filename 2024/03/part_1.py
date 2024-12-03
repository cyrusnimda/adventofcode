import re 

#file = "demo.txt"
file = "live.txt"

memory =  open(file).read()
#print(memory)

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
#print(matches)

total = 0
for multiply in matches:
    #print(multiply)
    numbers = list(map(int, re.findall(r"\d{1,3}", multiply)))
    result = numbers[0] * numbers[1]
    total += result

print("total=",total)
   