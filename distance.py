def distance():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    moscow_london = ((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5
    moscow_paris = ((550 - 480) ** 2 + (370 - 480) ** 2) ** 0.5
    london_paris = ((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5

    distances = {
        'moscow': {
            'London': moscow_london,
            'Paris': moscow_paris
        },

        'london': {
            'Moscow': moscow_london,
            'Paris': london_paris
        },

        'paris': {
            'London': london_paris,
            'Moscow': moscow_paris
        }
    }
    return distances


distances = distance()
print(distances)