from ProductionCode.datasource import DataSource
import sys

#A simple file to just demonstrate the DataSource functionality
test = DataSource()

# Added functionality to allow the user to search for categories in the
# command line. If the user fails to input a food, the default is cheese.
if len(sys.argv) > 2:
    user_input = (f"{sys.argv[2]}").upper()
    if sys.argv[1] == "--list":
        user_command = test.fromCategoryGetTypes(user_input)
    elif sys.argv[1] == "--healthfacts":
        user_command = test.fromDescriptionGetNutrition(user_input)
else:
    user_input = "CHEESE"
    user_command = test.fromCategoryGetTypes(user_input)
print(user_command)