# a = []
# b = []
# for line in open('demo.txt').read().split("\n"):
#     line_array = list(map(int, line.split()))
#     a.append(line_array[0])
#     b.append(line_array[1])


#file = "demo.txt"
file = "live.txt"

a, b = map(list, zip(*[list(map(int, line.split())) for line in open(file).read().split("\n") if line]))

a.sort()
b.sort()

c = list(map(lambda x, y: abs(x - y), a, b))
print(sum(c))