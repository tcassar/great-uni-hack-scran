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
        i = Ingredient(0, 400, 10, 'mince', 500)
        i.purchase_ingredient()