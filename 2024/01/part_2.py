
#file = "demo.txt"
file = "live.txt"

a, b = map(list, zip(*[list(map(int, line.split())) for line in open(file).read().split("\n") if line]))

a.sort()
b.sort()

c = list(map(lambda x, y: (x * b.count(x)), a, b))
print(sum(c))