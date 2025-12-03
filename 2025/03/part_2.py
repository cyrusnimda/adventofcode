
file = "live.txt"

batteries_raw =  open(file).read().split("\n")
batteries = [int(line) for line in batteries_raw]
batteries = [list(map(int, str(bank))) for bank in batteries]

def get_max_voltage(bank: list, size_of_voltagek: int, voltage: list = None) -> int:
    if voltage is None:
        voltage = []

    # Base case where we have enough digits
    if len(voltage) == size_of_voltagek:
        return int("".join(map(str, voltage)))
    
    # we can't look in the last x digits, as the voltage won't fit
    left_bank_index = -(size_of_voltagek - len(voltage) - 1)
    right_bank_index = len(bank) - size_of_voltagek + len(voltage) + 1

    # if is the last digit to add, just take the max of the remaining
    left_bank = bank[:left_bank_index] if left_bank_index != 0 else bank
    right_bank = bank[right_bank_index:] if right_bank_index != len(bank) else []

    max_number = max(left_bank)
    voltage.append(max_number)

    #remove everything up to and including max_index
    max_index = left_bank.index(max_number)
    left_bank = left_bank[max_index+1:]

    # Rebuild the bank to loop again
    left_bank.extend(right_bank)
    return get_max_voltage(left_bank, size_of_voltagek, voltage)


voltages = []
for bank in batteries:
    voltages.append(get_max_voltage(bank, 12))

print("Sum of max voltages:", sum(voltages))