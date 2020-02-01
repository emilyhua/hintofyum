from flask import Flask, request, render_template
import simplejson as json
import requests
from mainyum import find_from_ingredients, display_recipe_names, get_recipe
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_recipes():
    if request.method == 'POST':
        content = find_from_ingredients(request.form["restaurant_name"])
        json_response = json.loads(content.text)
        print(json_response)
        return render_template("home.html", response=json_response) if json_response != [] else render_template(
            "home.html", response="")
    else:
        return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# @app.route('/recipe{id}', methods['GET', 'POST'])
# def display_recipe(id):
#     if request.method == 'POST':
#             content = get_recipe(id)
#             json_response = json.loads(content.text)
#             print(json_response)
#             return render_template("test.html", response=json_response) if json_response != [] else render_template(
#                 "restaurant_list.html", response="")
#         else:
#             return render_template("test.html")
