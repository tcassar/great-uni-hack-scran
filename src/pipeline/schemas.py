from dataclasses import dataclass, field

import sqlite3


con = sqlite3.connect("../../tests/test_pipeline/test_scran")
cursor = con.cursor()


@dataclass
class Ingredient:
    id: int
    calories: int
    protein: int
    name: str
    mass: int

    @property
    def price(self) -> int:
        return cursor.execute(
            """SELECT price FROM main.shop
        WHERE  id = ?""",
            [self.id],
        ).fetchone()[0]

    @property
    def packet_size(self) -> int:
        return cursor.execute(
            """SELECT mass FROM main.shop
                WHERE  id = ?""",
            [self.id],
        ).fetchone()[0]

    def __eq__(self, other):
        return True if f"{self.id}{self.name}" == f"{other.id}{other.name}" else False

    def __repr__(self):
        return (
            f"Ingredient(id={self.id}, calories={self.calories}, "
            f" protein={self.protein}, name={self.name}, mass={self.mass})"
        )

    def _push_to_registry(self):

        # check if it exists
        names = [name[0] for name in cursor.execute("""SELECT name FROM registry""").fetchall()]
        if self.name not in names:
            # push new entry to registry
            cursor.execute("""  INSERT INTO registry (calories, protein, name)
                                VALUES (?, ?, ?);""", [self.calories, self.protein, self.name])
            con.commit()

            return cursor.execute("""SELECT id FROM registry WHERE calories=? AND protein=? AND name=? """,
                                  [self.calories, self.protein, self.name])

    def purchase_ingredient(self):
        """ pushes ingredient to pantry;
            if it doesn't exist in registry, """

        self._push_to_registry()  # make new entry to registry if doesn't exist

        # if we exist in the pantry update mass else create entry in pantry
        pid = cursor.execute("""SELECT r.id FROM pantry 
        JOIN registry r on pantry.id = r.id
        WHERE r.name = ?""", [self.name]).fetchone()

        if pid:
            cursor.execute("""UPDATE pantry SET mass = ? WHERE id = ?""", [self.mass, pid])
        else:
            # can always guarantee we will be in registry
            cursor.execute("""INSERT INTO pantry (mass, id) VALUES (?, 
            (SELECT id from registry WHERE name=?))""", [self.mass, self.name])

        con.commit()

@dataclass
class Recipe:
    id: int
    name: str
    ingredients: tuple[Ingredient] = field(default_factory=lambda: [])
    cost: int = -1

    @property
    def value(self):
        """Value is protein / calories ratio (*100, so we can round and use integer weights in graph"""
        return (
            sum([round(i.protein / i.calories * 100) for i in self.ingredients])
            if self.ingredients
            else -1
        )


@dataclass
class CookBook:
    recipes: list[Recipe] = field(default_factory=lambda: [])
    next_days: list[Recipe] = field(default_factory=lambda: [])

    def pull_recipes(self):

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
        return " ".join([ing.name for ing in self.ingredients])

    def build_pantry(self):

        query = """
SELECT r.id, calories, protein, name, mass FROM pantry
JOIN registry r on r.id = pantry.id"""

        ing_data = cursor.execute(query).fetchall()

        for ing in ing_data:
            self.ingredients.append(Ingredient(*ing))

    def update_pantry(self, recipes: list[Recipe]):

        """Will update values for recipes which are passed in"""

        sql_exists = """UPDATE pantry 
        SET mass = ? 
        WHERE id = ?"""

        sql_nexiste_pas = """INSERT INTO pantry (id, mass) VALUES (?, ?)"""

        pantry_ids = cursor.execute("SELECT id FROM main.pantry").fetchall()
        pantry_ids = [pid[0] for pid in pantry_ids]

        for recipe in recipes:
            for ingredient in recipe.ingredients:
                if ingredient.id in pantry_ids:
                    # update table where entry already exists
                    cursor.execute(sql_exists, [ingredient.mass, ingredient.id])
                else:
                    # add row to pantry linked to id
                    cursor.execute(sql_nexiste_pas, [ingredient.id, ingredient.mass])

        con.commit()
