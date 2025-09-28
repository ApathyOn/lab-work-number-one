radius = 42


def area():
    area = round(3.1415926*(radius**2), 4)
    return area


point_1 = (23, 34)

def distance_1():

    return bool(((23**2 + 34**2)**0.5) < 42)


point_2 = (30, 30)

def distance_2():
    return  bool(((30**2 + 30**2)**0.5) < 42)
    

areaa = area()
result_distance_1 = distance_1()
result_distance_2 = distance_2()


print(areaa)
print(result_distance_1)
print(result_distance_2)


