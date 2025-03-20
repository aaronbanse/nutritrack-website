import psycopg2
import ProductionCode.psqlConfig as config
from numpy import array as np_array

class DataSource:

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def fromCategoryGetTypes(self, category):
        '''
        From the table, accesses all foods of a specific Category (e.g. Cheese) that a user inputs
        using the command line.
        
        Arguments:
        category: accessed from the command line, a type of food, e.g. Cheese
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()

            query = "SELECT Description FROM food_nutrition WHERE Category = %s;"
            cursor.execute(query, (category,))
            descriptions = np_array(cursor.fetchall()).squeeze(1)

            return list(descriptions)

        except Exception:
            return  []

    def fromDescriptionGetNutrition(self, description):
            '''
            From the table, accesses a specific food from a Descrition (e.g. Cheese,Blue) that a user inputs
            using the command line, and returns the nutrition information.
            
            Arguments:
            description: accessed from the command line, a description of food, e.g. Cheese,Blue
            '''
            try:
                # set up a cursor
                cursor = self.connection.cursor()
                
                data_query = "SELECT * FROM food_nutrition WHERE Description = %s;"
                columns_query = "SELECT column_name FROM information_schema.columns WHERE table_name = 'food_nutrition';"

                # use np to squeeze
                cursor.execute(columns_query)
                labels = np_array(cursor.fetchall()).squeeze(1)[3:]
                cursor.execute(data_query, (description,))
                data = np_array(cursor.fetchall()).squeeze(0)[3:]

                return list(labels), list(data)

            except Exception:
                return [],[]
            
    def fromDescriptionGetNutrition(self, description):
        '''
        From the table, accesses a specific food from a Description (e.g. Cheese, Blue) that a user inputs
        and returns the nutrition information along with their respective units.
        
        Arguments:
        description: a description of food, e.g. Cheese, Blue
        '''
        try:
            # set up a cursor
            cursor = self.connection.cursor()
            
            data_query = "SELECT * FROM food_nutrition WHERE Description = %s;"
            columns_query = "SELECT column_name FROM information_schema.columns WHERE table_name = 'food_nutrition';"

            # use np to squeeze
            cursor.execute(columns_query)
            labels = np_array(cursor.fetchall()).squeeze(1)[3:]
            cursor.execute(data_query, (description,))
            data = np_array(cursor.fetchall()).squeeze(0)[3:]

            # Nutrient units mapping
            nutrient_units = {
                "alpha_carotene": "µg",
                "ash": "g",
                "beta_carotene": "µg",
                "beta_cryptoxanthin": "µg",
                "carbohydrate": "g",
                "cholesterol": "mg",
                "choline": "mg",
                "fiber": "g",
                "kilocalories": "kcal",
                "lutein_and_zeaxanthin": "µg",
                "lycopene": "µg",
                "manganese": "mg",
                "niacin": "mg",
                "pantothenic_acid": "mg",
                "protein": "g",
                "retinol": "µg",
                "riboflavin": "mg",
                "selenium": "µg",
                "sugar_total": "g",
                "thiamin": "mg",
                "water": "g",
                "monosaturated_fat": "g",
                "polysaturated_fat": "g",
                "saturated_fat": "g",
                "total_lipid": "g",
                "calcium": "mg",
                "copper": "mg",
                "iron": "mg",
                "magnesium": "mg",
                "phosphorus": "mg",
                "potassium": "mg",
                "sodium": "mg",
                "zinc": "mg",
                "vitamin_a_iu": "IU",
                "vitamin_a_rae": "µg",
                "vitamin_b12": "µg",
                "vitamin_b6": "mg",
                "vitamin_c": "mg",
                "vitamin_e": "mg",
                "vitamin_k": "µg",
                "first_household_weight": "g",
                "second_household_weight": "g"
            }

            # Append the units to the labels
            labels_with_units = [f"{label} ({nutrient_units.get(label, '')})" for label in labels]

            return list(labels_with_units), list(data)

        except Exception:
            return [], []