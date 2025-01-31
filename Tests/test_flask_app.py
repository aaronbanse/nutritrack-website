from ind_flask_app import *
import unittest

class Test_homepage(unittest.TestCase):
    def test_homepage_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b"""
    <h1>Welcome to The Homepage!</h1>
    <h3>Use this app to find useful information about foods, nutrition, and more!</h3>
    <p>
    <h2>App Features:</h2>
    <p>
    <h3>1. Access information of a specific cell by appending the row and column of the cell you seek at the end of the browser URL above.</h3>
    <h4>  ex. http://127.0.0.1:5000/0/0 finds row 0 and column 0.</h4>
    <p>
    <h3>2. Access a list of the related food types in the data set by typing /list/keyword at the end of the browser URL above.</h3>
    <h4>  ex. http://127.0.0.1:5000/list/cheese to find the types of cheese in the data set.</h4>
    <h4>  note: if the webpage returns blank, the food is not included in the data set.</h4>
    <p>
    <h3>3. Access a list of the nutritional information associated with a specific food by entering /health-facts/the specific food at the end of the browser URL above.</h3>
    <h4>  ex. http://127.0.0.1:5000/health-facts/cheese,blue to find the nutritional data for blue cheese in the data set.</h4>
    <h4>  note: if the webpage returns blank, the type of food is not included in the data set.</h4>
    <br>
    <h3>If you need to return to the homepage, enter http://127.0.0.1:5000 into your browser, though URLs may differ from machine to machine.</h3>
    <h3>Take a look at (and maybe copy) your URL now so that you can come back to the homepage if you need to!</h3>
    """, response.data)

class Test_get_food(unittest.TestCase):
    def test_get_food_route(self):
        self.app = app.test_client()
        response = self.app.get('/list/cheese', follow_redirects=True)
        self.assertEqual(b"The types of cheese in this data set are: Cheese,Blue; Cheese,Brick; Cheese,Brie", response.data)
    def test_get_food_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/list/apple', follow_redirects=True)
        self.assertEqual(b"The category of 'apple' is not in the data set. Would you like to search again?", response.data)
    def test_get_food(self):
        self.assertEqual(get_food("cheese"),"The types of cheese in this data set are: Cheese,Blue; Cheese,Brick; Cheese,Brie")
    def test_get_food_edgecase(self):
        with self.assertRaises(TypeError):
            get_food()

class Test_get_nutrition(unittest.TestCase):
    def test_get_nutrition(self):
        self.app = app.test_client()
        response = self.app.get('/health-facts/cheese,blue', follow_redirects=True)
        self.assertEqual(b"The nutrients included in 'Cheese,Blue' are: Alpha Carotene: 0.0; Ash: 5.11; Beta Carotene: 74.0; Beta Cryptoxanthin: 0.0; Carbohydrate: 2.34", response.data)
    def test_get_nutrition_route_edgecase(self):
        self.app = app.test_client()
        response = self.app.get('/health-facts/cheese', follow_redirects=True)
        self.assertEqual(b"The food named 'Cheese' is not in the data set. Would you like to search again?", response.data)
    def test_get_nutrition(self):
        self.assertEqual(get_nutrition("cheese,blue"),"The nutrients included in 'Cheese,Blue' are: Alpha Carotene: 0.0; Ash: 5.11; Beta Carotene: 74.0; Beta Cryptoxanthin: 0.0; Carbohydrate: 2.34")
    def test_get_nutrition_edgecase(self):
        with self.assertRaises(TypeError):
            get_nutrition()