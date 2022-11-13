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

