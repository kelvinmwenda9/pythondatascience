for x in range(1, 10, 1):
    print('Outer loop') # parent

    for i in range(1, 10, 1):
        print('Inner loop', end='') # child

