
#file = "demo.txt"
file = "live.txt"

ecuations = open(file).read().split("\n")

def can_be_obteined(result, numbers):
    first_number = numbers[0]
    last_number = numbers[-1]
    # base case
    if len(numbers) == 1:
        return first_number == result
    
    # recursive case
    # multiple case
    if result % last_number == 0 and can_be_obteined(result // last_number, numbers[:-1]): return True

    # add case
    if result > last_number and can_be_obteined(result - last_number, numbers[:-1]): return True

    # concat case
    numbers_to_remove = -len(str(last_number))
    str_result = str(result)
    str_last_number = str(last_number)
    if len(str_result) > len(str_last_number) and str_result.endswith(str_last_number) and can_be_obteined(int(str_result[:numbers_to_remove]), numbers[:-1]): return True
    
    return False

numbers_that_match = []
for ecuation in ecuations:
    result = int(ecuation.split(": ")[0])
    numbers = list(map(int, ecuation.split(": ")[1].split()))
    #print(result, numbers)
    if can_be_obteined(result, numbers):
        numbers_that_match.append(result)

print()
print("numbers_that_match", sum(numbers_that_match))

