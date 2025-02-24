from flask import Flask, render_template
from ProductionCode.datasource import DataSource

# dataset accessor
ds = DataSource()

app = Flask(__name__)

# I am not familiar with HTML, so this is based on a few minutes of internet surfing... I assume we learn a bit more later in the course :)
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/list/", strict_slashes = False)
def get_foods_instructions():
    return """
            <html>
            <h3><a href="/">Home</a></h3>
            <body>
            <h2>Find specific foods in the database</h2>
            <p>Enter the food you would like to search up after "/list/".
            <br>
            You can click on each food item to see their nutrition facts.<p>
            </body>
            </html>
            """

@app.route("/health-facts/", strict_slashes = False)
def get_nutrition_instructions():
    return """
            <html>
            <h3><a href="/">Home</a></h3>
            <body>
            <h2>Find nutrition facts for specific foods</h2>
            <p>
            Enter the specific food item you would like to search up after "/healh-facts/". 
            <br>
            If the item was not found, make sure it exists using the "/list/" command.
            <p>
            </body>
            </html>
            """

@app.route("/list/<category>", strict_slashes = False)
def get_foods(category):
    """
    Using the helper functions, accesses the data set to print the related food types of a specific category of food.
    
    Arguments:
    category : input from route, food category
    """
    
    category = category.upper() # format for search
    items = ds.fromCategoryGetTypes(category=category)
    
    category = category.lower() # format for printing
    if len(items) > 0:
        item_strs = [f"<a href=\"/health-facts/{item}\">{item.title()}</a>" for item in items]
        return ("<h3><a href=\"/\">Home</a></h3><p>The types of " + category + " in this data set are:<br>" + "<br>".join(item_strs) + "</p>")
    else:
        return ("<h3><a href=\"/\">Home</a></h3><p>The category '" + category + "' is not in the data set.</p>")

@app.route("/health-facts/<description>", strict_slashes = False)
def get_nutrition(description):
    """
    Using the helper functions, accesses the data set to print the related nutritional information for a specific food type.
    
    Arguments:
    description : input from route, specific food type
    """
    description = description.upper()
    labels, data = ds.fromDescriptionGetNutrition(description=description)
    
    food_info = []
    if len(data) > 0:
        for i in range(len(labels)):
            food_info.append(str(labels[i] + ": " + str(data[i])))
        return ("<h3><a href=\"/\">Home</a></h3><p>The nutrients included in '" + description.title() + "' are:<br>" + "<br>".join(food_info) + "</p>")
    else:
        return ("<h3><a href=\"/\">Home</a></h3> <p>The food named '" + description.title() + "' is not in the data set. Would you like to search again?</p>")

@app.errorhandler(404)
def page_not_found(e):
   return "Page not found. Please paste the homepage URL into your browser for instructions on how to operate this app."

if __name__== "__main__":
   app.run(debug=True)