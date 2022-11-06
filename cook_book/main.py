with open('recipes.txt', 'rt', encoding = 'utf-8') as file:
    cook_book = {}
    ingredients_ditail = {}
    for line in file:

        dish = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            ing = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ing
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity, 'measure': measure
                                })
            cook_book[dish] = ingredients
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    prod_dict = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] in prod_dict.keys():
                prod_dict[ingredients['ingredient_name']]['quantity'] +=  person_count * int(ingredients['quantity'])
            else:
                prod_dict[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': int(ingredients['quantity']) * person_count}
    return prod_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# print(prod_dict)
# print(cook_book)