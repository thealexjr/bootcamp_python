cookbook = {
  "sandwich": {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
  },
  "cake": {
    "ingredients": ["flour", "sugar", "sugar"],
    "meal": "dessert",
    "prep_time": 60
  },
  "salad": {
    "ingredients": ["avocado", "avocado", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
  }
}

"""#printing only the keys:
for i in cookbook.keys():
        print(i)

#printing only the values
for i in cookbook.values():
        print(i)"""

def recipe_info(cookbook, name):
        print("Recipe for", name)
        print("Ingredients: ", end='')
        for ingredient in cookbook[name]['ingredients']:
                print(ingredient, end='')
                if ingredient != cookbook[name]["ingredients"][-1]:
                        print(", ", end='')
                else:
                        print()
        print("To be eaten for", cookbook[name]['meal'])
        print("Takes", cookbook[name]['prep_time'], "minutes of cooking.\n")

def delete_recipe(recipe):
    for cle in cookbook.items:
            if cle == recipe:
                    cookbook.pop('cle', None)


def add_recipe(cookbook):
        print("Please enter the recipe's name")
        name = input()
        print("Please enter type of recipe")
        meal = input()
        print("Please enter ingredients separated by commas")
        ingredients = input().split(',')
        for each in ingredients:
                each = each.strip()
        print("Please enter preparation time in minutes")
        prep = input()

        cookbook[name] = {
                "ingredients": ingredients,
                "meal": meal,
                "prep_time" : prep
                }
        print("Recipe", name, "added.\n")
        return cookbook

def print_cookbook(cookbook):
        for each in cookbook:
                recipe_info(cookbook, each)


while (1):
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        x = input()
        if x == "1":
                cookbook = add_recipe(cookbook)
        if x == "2":
                delete_recipe(cookbook)
        if x == "3":
                recipe_name = input("recipe: ")
                if recipe_name in cookbook:
                        print_recipe(recipe_name)
                print(recipe_name, " doesn't exist in the cookbook")
        if x == "4":
                print_cookbook(cookbook)
        if x == "5":
                exit()
        else:
                print("\nThis option doesn't exist, please type the corresponding number.To exit enter 5\n")
  
 

