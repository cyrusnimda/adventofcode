import re

file = "live.txt"
#file = "live.txt"

total_tokens = 0
claw_configs =  open(file).read().split("\n\n")
for claw_config in claw_configs:
    claw_config = re.findall(r"(\d+)", claw_config)
    button_a_x, button_a_y, button_b_x, button_b_y, price_x, prize_y = map(int, claw_config)

    for numero_de_pulsaciones_button_a in range(101):
        for numero_de_pulsaciones_button_b in range(101):
            posible_premio = (numero_de_pulsaciones_button_a * button_a_x + numero_de_pulsaciones_button_b * button_b_x,
                              numero_de_pulsaciones_button_a * button_a_y + numero_de_pulsaciones_button_b * button_b_y)
            if posible_premio == (price_x, prize_y):
                tokens = numero_de_pulsaciones_button_a * 3 + numero_de_pulsaciones_button_b * 1
                total_tokens += tokens
                print(f"Possible win with A: {numero_de_pulsaciones_button_a}, B: {numero_de_pulsaciones_button_b} paying {tokens} tokens")

print("")
print(f"Total tokens spent: {total_tokens}")
