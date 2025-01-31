from flask import Flask
import csv
import pandas
from ProductionCode.get_food_data import fetch_category
from ProductionCode.get_food_data import health_facts

dummy_data = []


def load_data():
   """Loads data from the csv in the Data folder"""
   with open('Data/food_dummy_data.csv', newline='') as f:
       reader = csv.reader(f)
       for row in reader:
           dummy_data.append(row)

app = Flask(__name__)

# I am not familiar with HTML, so this is based on a few minutes of internet surfing... I assume we learn a bit more later in the course :)
@app.route("/")
def homepage():
    return """
    <h1>Welcome to The Homepage</h1>
    <h3>Use this app to find useful information about foods, nutrition, and more</h3>
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
    """

@app.route("/<row>/<column>", strict_slashes = False)
def get_cell(row, column):
    """
    Accesses the information of a specific cell from an input row and column.
    
    Arguments:
    row : input from route
    column : input from route
    """
    row, column = int(row), int(column)
    load_data()
    try:
        return ("This cell contains " + dummy_data[row][column] + " from the column labeled: '" + dummy_data[0][column] + "' and from the row labeled '" + dummy_data[row][0] + "'.")
    except IndexError:
        return ("This cell is out of bounds. Please try again by inputting a valid row and column into the URL above.")

@app.route("/list/<category>", strict_slashes = False)
def get_food(category):
    """
    Using the helper functions, accesses the data set to print the related food types of a specific category of food.
    
    Arguments:
    category : input from route, food category
    """
    category = category.upper()
    items = list(fetch_category(category))
    category = category.lower()
    if len(items) == 0:
        return ("The category of '" + category + "' is not in the data set. Would you like to search again?")
    else:
        return ("The types of " + category + " in this data set are: " + "; ".join(items).title())

@app.route("/health-facts/<description>", strict_slashes = False)
def get_nutrition(description):
    """
    Using the helper functions, accesses the data set to print the related nutritional information for a specific food type.
    
    Arguments:
    description : input from route, specific food type
    """
    description = description.upper()
    facts = health_facts(description)
    labels = list(facts.columns)
    values = list(facts.values.squeeze())
    food_info = []
    if len(values) == len(labels):
        for i in range(len(labels)):
            food_info.append(str(labels[i][5:] + ": " + str(values[i]))) #formatting retrieved from command_line.py
        return ("The nutrients included in '" + description.title() + "' are: " + "; ".join(food_info))
    else:
        return ("The food named '" + description.title() + "' is not in the data set. Would you like to search again?")

@app.errorhandler(404)
def page_not_found(e):
   return "Page not found. Please paste the homepage URL into your browser for instructions on how to operate this app."

if __name__== "__main__":
   app.run(debug=True)