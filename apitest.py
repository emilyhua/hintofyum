import spoonacular as sp
api = sp.API("19fb5e376e2647d78ec112501cb0c3f2")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
data = response.json()
print(data[0]['name'])
#>>>"flour"

# Detect text for mentions of food
response = api.detect_food_in_text("I really want a cheeseburger.")
data = response.json()
print(data['annotations'][0])
#>>>{"annotation": "cheeseburger", "tag":"dish"}

# Get a random food joke
response = api.get_a_random_food_joke()
data = response.json()
print(data['text'])
#>>>"People are a lot less judgy when you say you ate an 'avocado salad' instead of a bowl of guacamole."
