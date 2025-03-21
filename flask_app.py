from flask import Flask, render_template, request
from ProductionCode.datasource import DataSource

ds = DataSource()
app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def homepage():
    return render_template("index.html")

@app.route("/nutrients/", strict_slashes = False)
def get_nutrient_facts():
    return render_template("nutrient_facts.html")

@app.route("/recommendations/", methods=['GET', 'POST'], strict_slashes = False)
def get_recommendations():
    age = None
    sex = None
    if request.method == 'POST':
        age = request.form.get('age')
        sex = request.form.get('sex')
    return render_template("recommendations.html", age=age, sex=sex)

@app.route("/food-search/", strict_slashes = False)
def get_food_search():
    """
    Food search homepage, displays search bar.
    """
    return render_template("food_search.html")

@app.route("/list/<category>", strict_slashes = False)
def get_foods(category):
    """
    Accesses the data set to print the related food types of a specific category of food.
    
    Arguments:
    category : input from route, food category
    """
    
    category = category.upper() # format for search
    items = ds.fromCategoryGetTypes(category=category)
    
    category = category.title() # format for printing
    if len(items) > 0:
        return render_template("get_foods_output.html",items=items,category=category, succeeded=True)
    else:
        return render_template("get_foods_output.html",items=items,category=category, succeeded=False)

@app.route("/health-facts/<description>", strict_slashes=False)
def get_nutrition(description):
    """
    Accesses the data set to print the related nutritional information for a specific food type.
    
    Arguments:
    description : input from route, specific food type
    """
    description = description.upper()
    labels, data = ds.fromDescriptionGetNutrition(description=description)
    for i in range(len(labels)):
        labels[i] = labels[i].title()
        labels[i] = labels[i].replace("_"," ")
    
    if len(data) > 0:
        return render_template("get_nutrition_output.html", description=description.title(), items=zip(labels, data), succeeded=True)
    else:
        return render_template("get_nutrition_output.html", description=description.title(), items=[], succeeded=False)

@app.errorhandler(404)
def page_not_found(e):
   return render_template("error.html")

if __name__== "__main__":
   app.run(debug=True, port=5139)