from dataclasses import dataclass, field

import sqlite3


@dataclass
class Ingredient:
    id: int
    calories: int
    protein: int
    name: str

    def __str__(self):
        return self.name


@dataclass
class Recipe:
    id: int
    mass: int
    name: str
    ingredients: list[Ingredient] = field(default_factory=lambda: [])


@dataclass
class Pantry:
    ingredients: list[Ingredient] = field(default_factory=lambda: [])

    def __str__(self):
        return ' '.join([ing.name for ing in self.ingredients])

    def build_pantry(self):
        ing_data = sqlite3.connect('./scran').cursor().execute('SELECT * FROM registry').fetchall()

        for ing in ing_data:
            self.ingredients.append(Ingredient(*ing))

