
file = "live.txt"

batteries =  open(file).read().split("\n")

"""
    Get the maximum voltage from each battery bank,
    where each bank is represented as a string of digits.

    The last digit in the bank is not considered for voltage calculation.
    as it can't be the first digit of the voltage pair.

    We look for the maximum digit in the bank (excluding the last digit),
    then find the maximum digit to the right of that digit to form the voltage pair.
"""
def get_max_voltage(bank: str) -> int:
    sub_bank = bank[:-1]
    sub_bank_digits = [int(d) for d in sub_bank]
    sub_max_digit = max(sub_bank_digits)
    sub_max_index = sub_bank_digits.index(sub_max_digit)

    # we can only look to the right side of the max digit position
    sub_bank_right = bank[sub_max_index + 1:]
    sub_bank_right_digits = [int(d) for d in sub_bank_right]
    sub_max_right_digit = max(sub_bank_right_digits)
    
    max_voltage = int(f"{sub_max_digit}{sub_max_right_digit}")
    return max_voltage


voltages = []
for bank in batteries:
    voltages.append(get_max_voltage(bank))

print("Sum of max voltages:", sum(voltages))
