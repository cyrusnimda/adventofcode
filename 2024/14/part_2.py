import os

file = "demo.txt"
file = "live.txt"

max_x = 101
max_y = 103
seconds = 10000

# read and transform input
input = open(os.path.join(os.path.dirname(__file__), file), "r").read().split("\n")
robots = []
for robot_line in input:
    posicion, direccion = robot_line.split(" ")
    # remove chars
    posicion = posicion.replace("p=", "")
    direccion = direccion.replace("v=", "")
    #convert in tuple
    posicion = tuple(map(int, posicion.split(",")))
    direccion = tuple(map(int, direccion.split(",")))

    robots.append((posicion, direccion))

#print(robots)
cuadricula = []

# init tiles with inicial position of robots
for x in range(max_x):
    cuadricula.append([])
    for y in range(max_y):
        cuadricula[x].append([])
        cuadricula[x][y] = []
        for posicion_inicial, direccion in robots:
            if (x, y) == posicion_inicial:
                robot_index = robots.index((posicion_inicial, direccion))
                cuadricula[x][y].append(robot_index)


# show current position of tiles
def mostrar_cuadricula(cuadricula):
    print("mostrar cuadricula de ({} , {})".format(max_x, max_y))
    for y in range(max_y):
        for x in range(max_x):
            if len(cuadricula[x][y]) > 0:
                print("#", end="")
            else:
                print(".", end="")
        print("\n")


def move_robot(robot_index: int):
    posicion, direccion = robots[robot_index]
    nueva_x = posicion[0] + direccion[0]
    nueva_y = posicion[1] + direccion[1]

    # check bounds
    if nueva_x > max_x - 1:
        nueva_x -= max_x
    if nueva_x < 0:
        nueva_x += max_x
    if nueva_y > max_y - 1:
        nueva_y -= max_y
    if nueva_y < 0:
        nueva_y += max_y

    nueva_posicion = (nueva_x, nueva_y)

    cuadricula[posicion[0]][posicion[1]].remove(robot_index)
    cuadricula[nueva_posicion[0]][nueva_posicion[1]].append(robot_index)
    # update robots
    robots[robot_index] = (nueva_posicion, direccion)

for second in range(seconds):
    print(f"Segundo numero {second}")
    for robot_index in range(len(robots)):
        move_robot(robot_index)
    mostrar_cuadricula(cuadricula)
    print("\n")
    print("\n")

