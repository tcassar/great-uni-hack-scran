from PyQt5 import QtCore, QtGui, QtWidgets
import _sqlite3 as sq
from ui import Ui
import os
from src.pipeline.plan_meals import *


class Ui_MainWindow(Ui):
    def __init__(self):
        self.update_pantry()
        self.update_today_meals()
        self.update_tommorow_meals()

    # SQL querying

    def run_query(self, query):
        db = sq.connect("/home/ioan/PycharmProjects/hackathon/src/pipeline/scran")
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result

    # Pantry Display

    def grab_all_pantry_items(self):
        records = self.run_query("SELECT registry.name FROM registry")
        return [data[0] for data in records if records]

    def update_pantry(self):
        for i, name in enumerate(self.grab_all_pantry_items()):
            self.pantryTable.setRowCount(i + 1)
            item_name = QtWidgets.QTableWidgetItem(name)
            item_name.setText(name)
            self.pantryTable.setItem(i, 0, item_name)

    # Pantry Add Item

    def get_item_from_text(self):
        return self.addItemBox.text()

    def get_gram_from_text(self):
        return self.addGramsBox.text()

    def add_item(self):
        item = self.get_item_from_text()
        gram = self.get_gram_from_text()
        calories = 10
        protein = 100
        if item.isalpha() and gram.isnumeric():
            db = sq.connect("/home/ioan/PycharmProjects/hackathon/src/pipeline/scran")
            c = db.cursor()
            c.execute("INSERT INTO main.registry VALUES (:calories,:protein,:name)",
                      {'calories': calories, 'protein': protein, 'name': item})
            db.close()
        self.update_pantry()

    # Get Todays Recipes
    def get_allrecipes(self):
        recipes = Pipeline

    def update_today_meals(self):
        for i, recipe in enumerate(self.get_all_today_recipes()):
            self.todayTable.setRowCount(i + 1)
            item_name = QtWidgets.QTableWidgetItem(recipe)
            item_name.setText(recipe)
            self.todayTable.setItem(i, 0, item_name)

    # Get Tommorows Recipes

    def get_all_tommorow_recipes(self):
        recipe_records = self.run_query("SELECT recipes.name FROM recipes")
        return recipe_records

    def update_tommorow_meals(self):
        for i, recipe in enumerate(self.get_all_today_recipes()):
            self.tommorowTable.setRowCount(i + 1)
            item_name = QtWidgets.QTableWidgetItem(recipe)
            item_name.setText(recipe)
            self.tommorowTable.setItem(i, 0, item_name)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
