from flask import Flask, render_template, request
from app.recommender import get_recipes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        recipes = get_recipes(ingredients)
    return render_template("index.html", recipes=recipes)