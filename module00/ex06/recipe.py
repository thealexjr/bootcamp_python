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
    for cle in cookbook:
            if cle == recipe:
                    print(cookbook["cle"])
    print("That recipe doesn't exist in this cookbook.")
    
  
def delete_recipe(recipe):
    for cle in cookbook:
            if cle == recipe:
                    cookbook.pop('cle', None)

