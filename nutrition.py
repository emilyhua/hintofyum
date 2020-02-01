import spoonacular as sp
api = sp.API("eaf1205e8c26404a8cda30c46c86f1cd")

def find_from_ingredients(ingredient_list):
#ranking = 2 means minimizing missing ingredients
 recipe_list = api.search_recipes_by_ingredients(ingredients=ingredient_list, number=1, ranking=2)
 return recipe_list

def get_recipe_nutrition(ingredient_list, serving_num):
	recipe_list = api.visualize_recipe_nutrition(ingredientList=ingredient_list, servings=serving_num)
	return recipe_list

ingredients = input("Enter ingredients you would like to cook with: ")
nutrition = get_recipe_nutrition(ingredients, 1)
for recipe in nutrition:
 print(recipe)
