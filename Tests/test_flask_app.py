from flask_app import *
import unittest
from flask import render_template

class Test_Homepage(unittest.TestCase):
    def test_homepage_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        with app.app_context():
            self.assertEqual(render_template("index.html").encode(), response.data)

class Test_Get_Foods(unittest.TestCase):
    def test_get_food_route(self):
        self.app = app.test_client()
        response = self.app.get('/list/cheese', follow_redirects=True)
        self.assertEqual(b'<li><a href="/health-facts/CHEESE,BLUE">CHEESE,BLUE</a></li>', response.data[980:1040])
    def test_get_food_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/list/apple', follow_redirects=True)
        self.assertEqual(b"The Category 'Apple' is Not in the Data Set.", response.data[841:885])
    def test_get_food(self):
        with app.app_context():
            self.assertEqual(get_foods("cheese")[980:1040],'<li><a href="/health-facts/CHEESE,BLUE">CHEESE,BLUE</a></li>')
    def test_get_food_edgecase(self):
        with app.app_context():
            self.assertEqual(get_foods("")[831:870],"The Category '' is Not in the Data Set.")

class Test_Get_Nutrition(unittest.TestCase):
    def test_get_nutrition_route(self):
        self.app = app.test_client()
        response = self.app.get('/health-facts/cheese,blue', follow_redirects=True)
        self.assertEqual(b"<h3>The Nutrients in Cheese,Blue Are:</h3>", response.data[855:897])
    def test_get_nutrition_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/health-facts/cheese', follow_redirects=True)
        self.assertEqual(b"<h3>The food named 'Cheese' is not in the data set.</h3>", response.data[845:901])
    def test_get_nutrition(self):
        with app.app_context():
            self.assertEqual(get_nutrition("cheese,blue")[859:892],"The Nutrients in Cheese,Blue Are:")
    def test_get_nutrition_edgecase(self):
        with app.app_context():
            self.assertEqual(get_nutrition("")[833:883], "<h3>The food named '' is not in the data set.</h3>")
