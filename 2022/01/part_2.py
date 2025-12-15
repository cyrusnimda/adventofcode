
file = "live.txt"

foods =  open(file).read().split("\n\n")

calories = []
for i, food in enumerate(foods):
    items = food.splitlines()
    total = sum(int(item) for item in items)
    calories.append(total)

sorted_calories = sorted(calories, reverse=True)

print("top 3 calories:", sum(sorted_calories[:3]))
