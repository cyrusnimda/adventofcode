
#a = [list(map(int, line.split())) for line in open('demo.txt').read().split("\n")]

# a = []
# b = []
# for line in open('demo.txt').read().split("\n"):

#     line_array = list(map(int, line.split()))
#     a.append(line_array[0])
#     b.append(line_array[1])

# print(a)
# print(b)

#file = "demo.txt"
file = "live.txt"

a, b = zip(*[list(map(int, line.split())) for line in open(file).read().split("\n") if line])
a = list(a)
b = list(b)

a.sort()
b.sort()

print(a)
print(b)

c = list(map(lambda x, y: abs(x - y), a, b))
print(sum(c))