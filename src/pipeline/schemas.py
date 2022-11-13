from dataclasses import dataclass, field

import sqlite3

cursor = sqlite3.connect('../../tests/test_pipeline/test_scran').cursor()

@dataclass
class Ingredient:
    id: int
    calories: int
    protein: int
    name: str
    mass: int

    def __str__(self):
        return self.name


@dataclass
class Recipe:
    id: int
    name: str
    ingredients: tuple[Ingredient] = field(default_factory=lambda: [])
    cost: int = -1


@dataclass
class CookBook:
    recipes: list[tuple[Recipe, int]] = field(default_factory=lambda: [])

    def pull_recipies(self):

        ingredients_query = """SELECT irl.ingredient_id, r.calories, r.protein, r.name, irl.mass FROM recipes
                                JOIN ingredient_recipie_link irl on recipes.id = irl.recipe_id
                                JOIN registry r on irl.ingredient_id = r.id
                                WHERE irl.recipe_id = ?;"""

        recipes_query = """SELECT id, name FROM main.recipes"""

        for recipe in cursor.execute(recipes_query).fetchall():
            r = Recipe(*recipe)
            ingredients = cursor.execute(ingredients_query, [recipe[0]]).fetchall()
            for ingredient in ingredients:
                # noinspection PyTypeChecker
                r.ingredients.append(Ingredient(*ingredient))

            self.recipes.append(r)

@dataclass
class Pantry:
    ingredients: list[Ingredient] = field(default_factory=lambda: [])

    def __str__(self):
        return ' '.join([ing.name for ing in self.ingredients])

    def build_pantry(self):
        ing_data = cursor.execute('SELECT * FROM registry').fetchall()

        for ing in ing_data:
            self.ingredients.append(Ingredient(*ing))

