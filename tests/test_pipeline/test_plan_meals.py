from src.pipeline.plan_meals import *

from unittest import TestCase

class TestPipeline(TestCase):

    def test_assign_cost(self):
        pipe = Pipeline()
        pipe._assign_cost()

    def test__build_items(self):
        pipe = Pipeline()
        print(pipe._build_items())