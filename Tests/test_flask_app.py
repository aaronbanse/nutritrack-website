from flask_app import *
import unittest
from flask import render_template

class Test_Homepage(unittest.TestCase):
    def test_homepage_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(f'{render_template("index.html")}', response.data)

class Test_Get_Foods(unittest.TestCase):
    def test_get_food_route(self):
        self.app = app.test_client()
        response = self.app.get('/list/cheese', follow_redirects=True)
        self.assertEqual(f"{render_template('get_foods_output.html',items=items,category=category, succeeded=True)}", response.data)
    def test_get_food_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/list/apple', follow_redirects=True)
        self.assertEqual(f"{render_template('get_foods_output.html',items=items,category=category, succeeded=False)}", response.data)
    def test_get_food(self):
        self.assertEqual(get_foods("cheese"),"The types of cheese in this data set are:<br>Cheese,Blue<br>Cheese,Brick<br>Cheese,Brie")
    def test_get_food_edgecase(self):
        with self.assertRaises(TypeError):
            get_foods()

class Test_Get_Nutrition(unittest.TestCase):
    def test_get_nutrition_route(self):
        self.app = app.test_client()
        response = self.app.get('/health-facts/cheese,blue', follow_redirects=True)
        self.assertEqual(f"{render_template('get_nutrition_output.html', description=description.title(), items=[], succeeded=True)}", response.data)
    def test_get_nutrition_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/health-facts/cheese', follow_redirects=True)
        self.assertEqual(f"{render_template('get_nutrition_output.html', description=description.title(), items=[], succeeded=False)}", response.data)
    def test_get_nutrition(self):
        self.assertEqual(get_nutrition("cheese,blue"),"The nutrients included in 'Cheese,Blue' are:<br>Alpha Carotene: 0.0<br>Ash: 5.11<br>Beta Carotene: 74.0<br>Beta Cryptoxanthin: 0.0<br>Carbohydrate: 2.34")
    def test_get_nutrition_edgecase(self):
        with self.assertRaises(TypeError):
            get_nutrition()

'''      
class Test_get_cell(unittest.TestCase):
    def test_get_cell_route(self):
        self.app = app.test_client()
        response = self.app.get('/Ash/2', follow_redirects=True)
        self.assertEqual(b"0.0", response.data)
    def test_get_cell_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/Ash/-1', follow_redirects=True)
        self.assertEqual(b"Error: row must be an integer.", response.data)
        self.app = app.test_client()
        response = self.app.get('/Ashl/5', follow_redirects=True)
        self.assertEqual(b"Error: column name \"Ashl\" not found", response.data)
    def test_get_cell(self):
        self.assertEqual(get_cell('Ash', "1"), "2.11")
    def test_get_cell_edgecase(self):
        self.assertEqual(get_cell('Description','30'), 'Error: row index out of bounds. Only use indices from 0 to 20.')
'''