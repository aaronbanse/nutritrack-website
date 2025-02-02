from flask import Flask, render_template
import pandas
from ProductionCode.get_food_data import fetch_category, health_facts, get_data, error

# get dummy data as a pandas dataframe
dummy_data = get_data(dummy=True)

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

@app.route("/<column_name>/<row>", strict_slashes = False)
def get_cell(column_name: str, row: str):
    """
    Accesses the information of a specific cell from an input column name and row.
    
    Arguments:
    column_name : input from route
    row : input from route
    """
    
    # error checks
    if not row.isdigit():
        return error("row must be an integer.")
    if column_name not in dummy_data.columns:
        return error(f"column name \"{column_name}\" not found")
    if int(row) < 0 or int(row) >= len(dummy_data[column_name]) - 1:
        return error(f"row index out of bounds. Only use indices from 0 to {len(dummy_data[column_name])-1}.")
    
    return dummy_data[column_name][int(row)]

@app.route("/list/<category>", strict_slashes = False)
def get_foods(category):
    """
    Using the helper functions, accesses the data set to print the related food types of a specific category of food.
    
    Arguments:
    category : input from route, food category
    """
    
    category = category.upper() # format for search
    items = list(fetch_category(category))
    
    category = category.lower() # format for printing
    if len(items) == 0:
        return ("The category '" + category + "' is not in the data set.")
    else:
        return ("The types of " + category + " in this data set are:<br>" + "<br>".join([item.title() for item in items]))

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
        return ("The nutrients included in '" + description.title() + "' are:<br>" + "<br>".join(food_info))
    else:
        return ("The food named '" + description.title() + "' is not in the data set. Would you like to search again?")

@app.errorhandler(404)
def page_not_found(e):
   return "Page not found. Please paste the homepage URL into your browser for instructions on how to operate this app."

if __name__== "__main__":
   app.run(debug=True)