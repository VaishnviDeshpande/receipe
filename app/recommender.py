import difflib

# Sample recipe database (simple)
RECIPE_DB = [
    {
        "name": "Egg Fried Rice",
        "ingredients": ["rice", "eggs", "soy sauce", "onion"],
        "steps": [
            "Cook rice and let it cool.",
            "Scramble eggs in a pan.",
            "Add onions and stir-fry.",
            "Mix in rice and soy sauce. Fry everything together."
        ]
    },
    {
        "name": "Onion Omelette",
        "ingredients": ["eggs", "onion"],
        "steps": [
            "Chop onions and beat eggs.",
            "Mix them together with salt and pepper.",
            "Cook on a non-stick pan until golden."
        ]
    },
    {
        "name": "Soy Sauce Rice",
        "ingredients": ["rice", "soy sauce"],
        "steps": [
            "Cook rice.",
            "Mix with soy sauce and a bit of oil in a hot pan."
        ]
    }
]

def get_recipes(user_input):
    user_ingredients = [i.strip().lower() for i in user_input.split(",")]
    results = []

    for recipe in RECIPE_DB:
        matches = sum(1 for ing in recipe["ingredients"] 
                      if difflib.get_close_matches(ing, user_ingredients, n=1, cutoff=0.6))
        if matches >= len(recipe["ingredients"]) // 2:
            results.append(recipe)
    return results