


mother = 0
father = 1
grandfather = 2

def my_family_height():
    my_family = [mother, father, grandfather]


    
    my_family_height = [
        ['Екатерина', 170],
        ['Эдуард', 185],
        ['Алексей', 168],
    ]
    return my_family_height[1][1]


father_height = my_family_height()
print('Рост отца - ' + str(father_height) + 'см')
print('Общий рост моей семьи - ' + str(170+185+168) + 'см')
