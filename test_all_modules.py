# test_all_modules.py

import distance
import circle
import operations
import my_family
import favorite_movies
import garden
import secret
import shopping
import songs_list
import store
import zoo


def test_distance():
    result = distance.distance()
    assert result is not None 


def test_circle_area():
    result = circle.area()
    assert isinstance(result, (int, float))
    assert result > 0 


def test_circle_distance_1():
    result = circle.distance_1()
    assert isinstance(result, (int, float))


def test_circle_distance_2():
    result = circle.distance_2()
    assert isinstance(result, (int, float))


def test_operations_result():
    result = operations.result()
    assert isinstance(result, (int, float))
    


def test_my_family_height():
    result = my_family.my_family_height()
    assert isinstance(result, (int, float))
    assert result > 0


def test_favorite_movies():
    result = favorite_movies.first()
    assert result is not None  


def test_garden():
    result = garden.general()
    assert result is not None  


def test_secret():
    result = secret.secret_message()
    assert result is not None 


def test_shopping():
    result = shopping.sweets()
    assert result is not None  


def test_songs_list():
    result = songs_list.violator_songs_dict()
    assert result is not None


def test_store():
    result = store.store()
    assert result is not None  


def test_zoo():
    result = zoo.zoos()
    assert result is not None 