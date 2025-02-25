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
    return render_template("get_foods_instructions.html")

@app.route("/health-facts/", strict_slashes = False)
def get_nutrition_instructions():
    return render_template("get_nutrition_instructions.html")

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
    out_str = ""
    if len(items) > 0:
        item_strs = [f"<a href=\"/health-facts/{item}\">{item.title()}</a>" for item in items]
        out_str = f"The types of {category} in this data set are:<br>{'<br>'.join(item_strs)}"
    else:
        out_str = f"The category '{category}' is not in the data set."
        
    return f"""
        <html>
        <head>
        <link rel="stylesheet" href="../static/datastyle.css"/>
        <title>Food search</title>
        </head>
        <body>
        <h3><a href=\"/\">Home</a></h3>
        <p>
        {out_str}
        </p>
        </body>
        </html>"""

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
    out_str = ""
    if len(data) > 0:
        for i in range(len(labels)):
            food_info.append(str(labels[i] + ": " + str(data[i])))
        out_str = f"The nutrients included in '{description.title()}' are:<br>{'<br>'.join(food_info)}" 
    else:
        out_str = f"The food named '{description.title()}' is not in the data set. Would you like to search again?"
    
    return f"""
        <html>
        <head>
        <link rel="stylesheet" href="../static/datastyle.css"/>
        <title>Food nutrition search</title>
        </head>
        <body>
        <h3><a href=\"/\">Home</a></h3>
        <p>
        {out_str}
        </p>
        </body>
        </html>"""

@app.errorhandler(404)
def page_not_found(e):
   return "Page not found. Please paste the homepage URL into your browser for instructions on how to operate this app."

if __name__== "__main__":
   app.run(debug=True)