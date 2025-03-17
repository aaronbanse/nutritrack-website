# CS257-TeamTemplate
# Team Amazooglesoft
Emma\
Nora\
Nathan\
Aaron

# Nutritrack Overview
Our website is designed to allow users to search nutritional facts about certain types of foods that they are interested in.

### Features
* Scanability: Our website is structured for easy reading. There are clear buttons in our navigation bar that clearly state what users may be looking for. Additionally, our website has very clear color blocks, so users can clearly see where the different sections are.

* Satisficing: Users can quickly find what they need with intuitive navigation and the website is also visually pleasing without too much clutter.

* Muddling Through: The design ensures that users can explore our website without any strict guidance. There are also instructions that may be followed, but not necessary.

## Usability Fixes

### Issue 1  
The original website had information on nutrient quantities for various food items; however, many users requested informative guidelines for daily nutrient intake. This would allow users to be more informed about nutrition information in addition to providing users with a sense of scale.

#### Fix: `recommendations.html`  
To address this issue, `recommendations.html` was added. On the recommendations page, users can enter their sex and age range, allowing for a customizable experience specific to the user. After selecting their sex and age, the page provides the user with recommendations for daily nutrient intake as well as a link to more information about the specific nutrients.

---

### Issue 2  
The original website allowed users to search for a specific food, providing information on quantities of nutrients and a link to a comprehensive description of all nutrients. Many users suggested it would be much more convenient to be able to hover over a nutrient to quickly find nutrition information just for that nutrient. This would allow users to obtain information more efficiently without having to navigate and search for a specific nutrient among all of the nutrient descriptions.

#### Fix: `get_foods_output.html`  
To address this issue, `get_foods_output.html` was modified to return a description of the nutrient when it is hovered over. This provides users with a more seamless experience, allowing them to explore the nutrient information while briefly hovering over nutrients for descriptions. The Nutrient Information page remains usable for users who prefer to view the comprehensive list of nutrients.

## Code Smells Fixes

### Issue #1: `homepage.css`
The first code smell we are addressing is Duplication. The original coding in this project had a lot of duplicated code, particularly in the homepage.css. There were many excess lines in the CSS that applied the same properties to multiple div tags, when they could have been applied once higher up. This duplicaton made the code very redundant, longer than necessary, and made it harder to find the code that needed editing, and thus, harder to maintain. 

#### Fix:  
To address this issue, excess lines were deleted, and commonly used CSS variables, such as font-family and background-color, were moved to the body{} selector. This centralized styling, reducing redundancy and improving readbility and maintainability.

---

### Issue #2: `recommendations.html`
The second code smell we are addressing is Long Method. Though this code technically isn't a method, this seemed like the most apt description for the problem that was fixed. The code for displaying recommendations based on sex and age features clunky if/else statements and tons of reused code. The code is structured so that there is an entire block of html to display for each combination of age and sex. This uses far too much space and does not need to repeat any code. It also does not naturally indicate the relation between the input and output.

#### Fix: 
The code still utilizes if/else statements, but uses them to set variables which let us access cells from a defined table. This change takes up less than 20% of the space of the previous version. If else statements are used to group the given age into one of 7 age groups, which are used to determine recommendations from the table. The code is much more modular and readable this way. This code isn't available to compare asgainst the front end deliverable submission because it was written for the design improvements and then modified to remove the code smell. To view the old code and compare, view commit #56, the push labeled "jumps to output" under the history of templates/recommendations.html, or alternatively, the code snippet below.

```bash
                    {% elif age == "4-8" %}
                         {% if gender == 'male' %}
                             <div class="nutrientreturn">
                                 <h1>Macro Nutrients:</h1>
                                     <ul>
                                         <li>Protein(g): 19</li>
                                         <li>Carbohydrate(g): 130</li>
                                         <li>Dietary Fiber(g): 19.6</li>
                                         <li>Total Fat(% of Daily Intake): 25 - 35%</li>
                                     </ul>
                                 <h1>Minerals:</h1>
                                     <ul>
                                         <li>Calcium(mg): 1000</li>
                                         <li>Iron(mg): 10</li>
                                         <li>Potassium(mg): 3800</li>
                                         <li>Sodium(mg): 1900</li>
                                         <li>Copper(mg): 0.44</li>
                                     </ul>
                             </div>
                         {% else %}
                             <div class="nutrientreturn">
                                 <h1>Macro Nutrients:</h1>
                                     <ul>
                                         <li>Protein(g): 19</li>
                                         <li>Carbohydrate(g): 130</li>
                                         <li>Dietary Fiber(g): 16.8</li>
                                         <li>Total Fat(% of Daily Intake): 25-35%</li>
                                     </ul>
                                 <h1>Minerals:</h1>
                                     <ul>
                                         <li>Calcium(mg): 1000</li>
                                         <li>Iron(mg): 10</li>
                                         <li>Potassium(mg): 3800</li>
                                         <li>Sodium(mg): 1900</li>
                                         <li>Copper(mg): 0.44</li>
                                     </ul>
                             </div>
                         {% endif %}
                     {% elif age == "9-13" %}
                         {% if gender == 'male' %}
                             <div class="nutrientreturn">
                                 <h1>Macro Nutrients:</h1>
                                     <ul>
                                         <li>Protein(g): 34</li>
                                         <li>Carbohydrate(g): 130</li>
                                         <li>Dietary Fiber(g): 25.2</li>
```


# Command Line Interface
### Basic Usage Examples

To use this command line interface, make sure to set up a virtual environment with pandas (a software library for Python) installed. Without this setup, the command line will not run correctly. Make sure to run all commands within the active virtual environment. 

### Example Commands
```bash
$ python3 command_line.py --list CHEESE
CHEESE,BLUE
CHEESE,BRICK
CHEESE,BRIE
$ python3 command_line.py --healthfacts CHEESE,BLUE
Alpha Carotene: 0.0
Ash: 5.11
Beta Carotene: 74.0
Beta Cryptoxanthin: 0.0
Carbohydrate: 2.34
```
```bash
$ python3 flask_app.py
 * Serving Flask app 'flask_app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5139
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 120-841-765
```
Copy the link (http://127.0.0.1:5139) in your browser and our website will appear