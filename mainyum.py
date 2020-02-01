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
    recipe_list = api.search_recipes_by_ingredients(ingredients=ingredient_list, number = 10, ranking=2)
    return recipe_list

def parse_recipe(recipe_list):


ingredients = input("Enter ingredients you would like to cook with: ")
recipes = find_from_ingredients(ingredients)
for recipe in recipes:
    print(recipe)
    print("\n")
