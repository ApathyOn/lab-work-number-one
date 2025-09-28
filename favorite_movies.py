my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

def first():
    first = (my_favorite_movies[:10])
    return first

def last():
    last = my_favorite_movies[42:]
    return last

def second():
    second = my_favorite_movies[12:25]
    return second

def second_last():
    second_last = my_favorite_movies[35:40]
    return second_last

first_result = first()
last_result = last()
second_result = second()
second_last_result = second_last()

print(first_result)
print(last_result)
print(second_result)
print(second_last_result)


