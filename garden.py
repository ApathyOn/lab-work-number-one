


garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )


meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )


garden_set = set(garden)
meadow_set = set(meadow)

def exclusive():

    exclusive = garden_set | meadow_set
    return exclusive

def general():

    general = garden_set & meadow_set
    return general

def garden_flowers():
    garden_flowers = garden_set.difference(meadow_set)
    return garden_flowers


def meadow_flowers():
    meadow_flowers = meadow_set.difference(garden_set)
    return meadow_flowers


exclusive_result = exclusive()
general_result = general()
garden_flowers_result = garden_flowers()
meadow_flowers_result = meadow_flowers()

print(exclusive_result)
print(general_result)
print(garden_flowers_result)
print(meadow_flowers_result)
