def how_many_cakes_can_be_baked(how_recipe, how_available):
    counter = 0
    while can_bake(how_recipe, how_available):
        counter += 1
        for item in how_recipe.keys():
            how_available[item] -= how_recipe[item]

    return counter


def can_bake(can_recipe, can_available):
    return_value = False
    for k, v in can_recipe.items():
        if k in can_available.keys() and can_recipe[k] <= can_available[k]:
            return_value = True
        else:
            return False

    return return_value


def cakes(cakes_recipe, cakes_available):
    return how_many_cakes_can_be_baked(cakes_recipe, cakes_available)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))  # 2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))  # 0
