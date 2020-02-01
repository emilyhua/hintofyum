import spoonacular as sp
api = sp.API("19fb5e376e2647d78ec112501cb0c3f2")

def get_ingredients(list, serving_num, nutrition_included = False):
    response = api.parse_ingredients(list, servings=serving_num, includeNutrition = nutrition_included)
    return response

def display_recipe_names(query):
    recipe_list = api.autocomplete_recipe_search(query, 10)
    return recipe_list

def find_from_ingredients(ingredient_list):
    #ranking = 2 means minimizing missing ingredients
    recipe_list = api.search_recipes_by_ingredients(ingredients=ingredient_list, number=10, ranking=2)
    return recipe_list

def get_recipe(id):
    recipe_info = api.get_recipe_information(id)
    return recipe_info

# info = get_recipe(1136928)
# for thing in info:
#     print(thing)
#
# ingredients = input("Enter ingredients you would like to cook with: ")
# recipes = find_from_ingredients(ingredients)
# max_recipes = 10
# curr_recipes = 0
# recipe_id = -1
# for recipe in recipes:
#     # if curr_recipes < 10:
#     #     recipe_id = parse_recipe(recipe)
#     #     curr_recipes++
#     print(recipe)
#     print("\n")
