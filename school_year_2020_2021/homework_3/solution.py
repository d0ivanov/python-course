from time import sleep

def simulation(grid):
    # Your implementation goes here
    # Please don't upload the whole content of the file,
    # but only this function (along with any additional
    # code that your implementation requires)
    pass


def print_grid(grid):
    for row in grid:
        for cell in row:
            print('■' if cell else '□', end=' ')
        print('')


def animate(simulation):
    simulacra = next(simulation)
    while True:
        print('')
        print('')
        print_grid(simulacra)
        sleep(1)
        simulacra = next(simulation)


g = [[0 for i in range(15)] for k in range(15)]
g[2][1] = 1
g[2][2] = 1
g[2][3] = 1
g[1][3] = 1
g[0][2] = 1

animate(simulation(g))
