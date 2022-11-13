from src.pipeline.plan_meals import *

from unittest import TestCase

class TestPipeline(TestCase):

    def test_assign_cost(self):
        pipe = Pipeline()
        pipe.assign_cost()