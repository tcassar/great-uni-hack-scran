from src.pipeline.plan_meals import *

from unittest import TestCase

class TestPipeline(TestCase):

    def test_assign_cost(self):
        pipe = Pipeline()
        pipe._assign_cost()

    def test__build_items(self):
        pipe = Pipeline()
        print(pipe._build_items())

    def test__knapsack(self):
        pipe = Pipeline()
        print(pipe._knapsack())

    def test__items_to_recipes(self):
        pipe = Pipeline()
        pipe._items_to_recipes()
        print([r for r in pipe.cb.next_days])

    def test_process(self):
        pipe = Pipeline()
        print(pipe.process())
