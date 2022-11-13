"""plans scran"""
from src.pipeline import schemas
from src.engine import graph, knapsack


class Pipeline:
    """To get list of recipes:
    `recipes = Pipeline().process()`
    """

    def __init__(self, budget=20000):

        self.budget = budget

        # build pantry, get recipes
        self.pantry = schemas.Pantry()
        self.cb = schemas.CookBook()

        self.pantry.build_pantry()
        self.cb.pull_recipes()

    def _assign_cost(self):
        """Assigns cost and value to recipes depending on what is currently
        in the pantry"""

        for recipe in self.cb.recipes:
            cost = 0
            for ingredient in recipe.ingredients:
                if pantry_ingredient := [
                    i for i in self.pantry.ingredients if i == ingredient
                ]:
                    if pantry_ingredient[0].mass >= ingredient.mass:
                        # cost of ingredient is 0 as we have enough in pantry
                        pantry_ingredient[0].mass -= ingredient.mass
                        continue
                    elif pantry_ingredient[0].mass < 0:
                        pantry_ingredient[
                            0
                        ].mass = 0  # reset to none so we don't end up with an imaginary food debt
                    else:
                        # otherwise we need to buy stuff
                        cost += ingredient.price
                        pantry_ingredient[0].mass += (
                            ingredient.packet_size - ingredient.mass
                        )
                else:
                    new = ingredient
                    new.mass = new.packet_size - ingredient.mass
                    cost += new.price
                    self.pantry.ingredients.append(new)

            recipe.cost = cost
            print(f"{recipe.name} will cost {cost} and have a value of {recipe.value}")

    def _build_items(self) -> list[graph.Item]:
        """builds list of Items ready to be put into knapsace"""

        self._assign_cost()

        items = []
        for recipe in self.cb.recipes:
            items.append(graph.Item(recipe.name, recipe.cost, recipe.value))

        return items

    def _knapsack(self) -> list[graph.Item]:
        """Runs the knapsack problem on list[items] and returns list[Items]"""
        kp = knapsack.Knapsack(self._build_items(), self.budget)
        return kp.solve_kp()

    def _items_to_recipes(self):
        items = self._knapsack()

        self.cb.next_days.append(
            *[
                [recipe for recipe in self.cb.recipes if recipe.name == item.label]
                for item in items
            ][0]
        )

    def process(self) -> list[schemas.Recipe]:
        """Returns next few days worth of recipes"""
        self._items_to_recipes()
        print(self.cb.next_days, "process")
        return self.cb.next_days
