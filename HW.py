with open('Dishes.txt', 'rt', encoding='utf-8') as p:
    cook_book = {}
    for line in p:
        dish = p.readline()
        ingredient_name = p.readline()
        for ing in range(int(ingredient_name)):
            split_lines = p.readline().split(' | ')


    print(p)


