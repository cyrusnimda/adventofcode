import re

file = "live.txt"
#file = "live.txt"

total_tokens = 0
claw_configs =  open(file).read().split("\n\n")
for claw_config in claw_configs:
    claw_config = re.findall(r"(\d+)", claw_config)
    button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = map(int, claw_config)
    prize_x += 10000000000000
    prize_y += 10000000000000

    numero_de_pulsaciones_button_a = (prize_x * button_b_y - prize_y * button_b_x) / (button_a_x * button_b_y - button_a_y * button_b_x)
    numero_de_pulsaciones_button_b = (prize_x - button_a_x * numero_de_pulsaciones_button_a) / button_b_x

    # check if both are integers
    if (numero_de_pulsaciones_button_a % 1 == 0) and (numero_de_pulsaciones_button_b % 1 == 0):
        tokens = int(numero_de_pulsaciones_button_a) * 3 + int(numero_de_pulsaciones_button_b) * 1
        total_tokens += tokens
        print(f"Possible win with A: {numero_de_pulsaciones_button_a}, B: {numero_de_pulsaciones_button_b} paying {tokens} tokens")

print("")
print(f"Total tokens spent: {total_tokens}")
