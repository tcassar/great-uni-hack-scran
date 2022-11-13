"""plans scran"""
from src.pipeline import schemas


class Pipeline:

    def __init__(self):

        # build pantry, get recipes
        self.pantry = schemas.Pantry()
        self.cb = schemas.CookBook()

        self.pantry.build_pantry()
        self.cb.pull_recipies()

    def assign_cost(self):
        """Assigns cost to recipes depending on what is currently
        in the pantry"""

        print(self.pantry.ingredients, end='\n\n')

        for recipe in self.cb.recipes:
            cost = 0
            for ingredient in recipe.ingredients:
                if pantry_ingredient := [i for i in self.pantry.ingredients if i == ingredient]:
                    if pantry_ingredient[0].mass >= ingredient.mass:
                        # cost of ingredient is 0 as we have enough in pantry
                        continue
                    else:
                        # otherwise we need to buy stuff
                        cost += ingredient.price
                        pantry_ingredient[0].mass += ingredient.packet_size
                else:
                    new = ingredient
                    new.mass = new.packet_size
                    cost += new.price
                    self.pantry.ingredients.append(new)

            print(f"{recipe.name} will cost {cost} and have a value of {recipe.value}")
