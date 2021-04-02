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

"""printing only the keys:
for i in cookbook.keys():
        print(i)

printing only the values
for i in cookbook.values():
        print(i)

printing the items
for i in cookbook.items():
        print(i)"""

def print_recipe(recipe):
    for cle in cookbook.items:
            if cle == recipe:
                    print(cookbook["cle"])
    print("That recipe doesn't exist in this cookbook.")
    
  
def delete_recipe(recipe):
    for cle in cookbook.items:
            if cle == recipe:
                    cookbook.pop('cle', None)
            
            
def add_recipe(recipe,ingredients,meal,prep_time):
    new_recipe = {
      recipe: {
      "ingredients": ingredients.split(","),
      "meal": meal_type,
      "prep_time": prep_time
    }
  }
  cookbook.update(new_recipe)
  
def print_all_recipe():
    for cle in cookbook.items:
        print(cle)
        
print("Please select an option by typing the corresponding number:")
                print("1: Add a recipe")
                print("2: Delete a recipe")
                print("3: Print a recipe")
                print("4: Print the cookbook")
                print("5: Quit")
                x = input()
                if x == "1":
                     a = input("Please enter the recipe's name to add: ")
                     b = input("Please enter the recipe's ingredients: ")
                     c = input("Please enter the recipe's type of meal: ")
                     d = input("Please enter the recipe's prep time: ")
                    cookbook = add_recipe(a,b,c,d)
                elif x == "2":
                     name = input("Please enter the recipe's name to delete: ")
                    delete_recipe(name)
                elif x == "3":
                    name = input("Please enter the recipe's name to get its details: ")
                    print_recipe(name)
                elif x == "4":
                    print(cookbook)
                elif x == "5":
                    exit()
                else:
                    print("\nThis option doesn't exist, please type the corresponding number.\n")
  
 

