from src.pipeline.schemas import *
from src.pipeline import plan_meals
from unittest import TestCase


class TestPantry(TestCase):
    def test_update_pantry(self):
        p = Pantry()
        p.build_pantry()
        recipes = plan_meals.Pipeline().process()
        print(recipes)
        p.update_pantry(recipes)



class TestIngredient(TestCase):
    def test__push_to_registry(self):
        i = Ingredient(0, 400, 10, 'mince', 500)
        i._push_to_registry()

    def test_purchase_ingredient(self):
        i = Ingredient(0, 32, 2, 'canned tomato', 20000)
        i.purchase_ingredient()

    def test_push_recipe(self):
        in_names = [("spaghetti", 180),
                    ("parmesan", 20),
                    ("bacon", 100),
                    ("canned tomato", 500)]

        r = Recipe(0, 'amatrician')

        for name, mass in in_names:
            raw_ing = cursor.execute("""SELECT id, calories, protein FROM main.registry
            WHERE name = ?""", [name]).fetchall()[0]
            r.ingredients.append(Ingredient(*raw_ing, name, mass))

        r.push_recipe()
