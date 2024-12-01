
#file = "demo.txt"
file = "live.txt"

a, b = zip(*[list(map(int, line.split())) for line in open(file).read().split("\n") if line])
a = list(a)
b = list(b)

a.sort()
b.sort()

print(a)
print(b)

c = list(map(lambda x, y: (x * b.count(x)), a, b))
print(sum(c))