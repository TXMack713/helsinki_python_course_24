# Write your solution here
def search_by_name(filename: str, word: str):
    recipes = {}
    ingredients = []
    lists_of_recipes = []
    if filename == "":
        filename = "recipes1.txt"
    '''new_file = open(filename, 'r')
    file_contents = []
    recipe_contents = []
    for entry in new_file:
        file_contents.append(entry)
    
    print("file contents", file_contents)
    count = 0
    file_length = len(file_contents)
   
    for item in file_contents:
        if item.startswith("\n"):
            lists_of_recipes.append(recipe_contents)
            print("Recipe content", recipe_contents)
            recipe_contents = []
            continue
        else:
            recipe_contents.append(item.rstrip())
    lists_of_recipes.append(recipe_contents)
    print("Recipe content", recipe_contents)'''

    with open(filename) as file:
        for line in file:
            if line.strip("\n") == "":
                if len(ingredients) != 0:
                    lists_of_recipes.append(ingredients)
                    # print(ingredients)
                ingredients = []
                # continue
            else:
                ingredients.append(line.strip())
        lists_of_recipes.append(ingredients)
    
    # print("List of recipes", lists_of_recipes)
    for recipe in lists_of_recipes:
        single_recipe = {}
        single_recipe["recipe"] = recipe[0]
        # print(recipe[0])
        single_recipe["cook_time"] = recipe[1]
        # print(recipe[1])
        single_recipe["ingredients"] = recipe[2:]
        # print(recipe[2:])
        recipes[recipe[0]] = single_recipe
        # print(single_recipe)
    
    # for key, value in recipes.items():
    #     print(key, value)
    
    found_recipes = []
    for key, value in recipes.items():
        result = key.lower()
        if result.find(word) != -1:
            found_recipes.append(key)
    
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = {}
    ingredients = []
    lists_of_recipes = []
    if filename == "":
        filename = "recipes1.txt"
    '''new_file = open(filename, 'r')
    file_contents = []
    recipe_contents = []
    for entry in new_file:
        file_contents.append(entry)
    
    print("file contents", file_contents)
    count = 0
    file_length = len(file_contents)
   
    for item in file_contents:
        if item.startswith("\n"):
            lists_of_recipes.append(recipe_contents)
            print("Recipe content", recipe_contents)
            recipe_contents = []
            continue
        else:
            recipe_contents.append(item.rstrip())
    lists_of_recipes.append(recipe_contents)
    print("Recipe content", recipe_contents)'''

    with open(filename) as file:
        for line in file:
            if line.strip("\n") == "":
                if len(ingredients) != 0:
                    lists_of_recipes.append(ingredients)
                    # print(ingredients)
                ingredients = []
                # continue
            else:
                ingredients.append(line.strip())
        lists_of_recipes.append(ingredients)
    
    # print("List of recipes", lists_of_recipes)
    for recipe in lists_of_recipes:
        single_recipe = {}
        single_recipe["recipe"] = recipe[0]
        # print(recipe[0])
        single_recipe["cook_time"] = recipe[1]
        # print(recipe[1])
        single_recipe["ingredients"] = recipe[2:]
        # print(recipe[2:])
        recipes[recipe[0]] = single_recipe
        # print(single_recipe)
    
    # for key, value in recipes.items():
    #     print(key, value)
    
    found_recipes = []
    for key, value in recipes.items():
        result = int(value["cook_time"])
        if result <= prep_time:
            # recipe = (key, result)
            recipe = f"{key}, preparation time {value["cook_time"]} min"
            # print(f"{recipe[0]}, preparation time {recipe[1]} min")
            found_recipes.append(recipe)
    
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = {}
    ingredients = []
    lists_of_recipes = []
    if filename == "":
        filename = "recipes1.txt"
    '''new_file = open(filename, 'r')
    file_contents = []
    recipe_contents = []
    for entry in new_file:
        file_contents.append(entry)
    
    print("file contents", file_contents)
    count = 0
    file_length = len(file_contents)
   
    for item in file_contents:
        if item.startswith("\n"):
            lists_of_recipes.append(recipe_contents)
            print("Recipe content", recipe_contents)
            recipe_contents = []
            continue
        else:
            recipe_contents.append(item.rstrip())
    lists_of_recipes.append(recipe_contents)
    print("Recipe content", recipe_contents)'''

    with open(filename) as file:
        for line in file:
            if line.strip("\n") == "":
                if len(ingredients) != 0:
                    lists_of_recipes.append(ingredients)
                    # print(ingredients)
                ingredients = []
                # continue
            else:
                ingredients.append(line.strip())
        lists_of_recipes.append(ingredients)
    
    # print("List of recipes", lists_of_recipes)
    for recipe in lists_of_recipes:
        single_recipe = {}
        single_recipe["recipe"] = recipe[0]
        # print(recipe[0])
        single_recipe["cook_time"] = recipe[1]
        # print(recipe[1])
        single_recipe["ingredients"] = recipe[2:]
        # print(recipe[2:])
        recipes[recipe[0]] = single_recipe
        # print(single_recipe)
    
    # for key, value in recipes.items():
    #     print(key, value)
    
    found_recipes = []
    for key, value in recipes.items():
        result = value["ingredients"]
        print(result)
        if result.count(ingredient) != 0:
            # recipe = (key, int(value["cook_time"]))
            recipe = f"{key}, preparation time {value["cook_time"]} min"
            found_recipes.append(recipe)
        else:
            continue
    
    return found_recipes

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
    
    time_recipes = search_by_time("recipes1.txt", 20)
    for recipe in time_recipes:
        print(f"{recipe[0]}, preparation time {recipe[1]} min")
    
    ingredient_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in ingredient_recipes:
        print(f"{recipe[0]}, preparation time {recipe[1]} min")
