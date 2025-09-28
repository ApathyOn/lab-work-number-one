def zoos():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

    zoo.insert(1, 'bear')
    print(zoo)

    birds = ['rooster', 'ostrich', 'lark', ]
    zoo.append(birds[0])
    zoo.append(birds[1])
    zoo.append(birds[2])
    print(zoo)

    zoo.remove('elephant')
    return zoo

zoo_result = zoos()
print(zoo_result)


