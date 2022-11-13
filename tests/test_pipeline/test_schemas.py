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
