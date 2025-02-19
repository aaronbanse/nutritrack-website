import psycopg2
import ProductionCode.psqlConfig as config
import numpy as np

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

            query = "SELECT \"Description\" FROM food_nutrition WHERE \"Category\" = %s;"
            cursor.execute(query, (category,))
            # use np to squeeze
            descriptions = np.array(cursor.fetchall()).squeeze(1)
            
            return list(descriptions)

        except Exception as e:
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
            
            data_query = "SELECT * FROM food_nutrition WHERE \"Description\" = %s;"
            columns_query = "SELECT column_name FROM information_schema.columns WHERE table_name = 'food_nutrition';"

            # use np to squeeze
            cursor.execute(columns_query)
            labels = np.array(cursor.fetchall()).squeeze(1)[3:]
            cursor.execute(data_query, (description,))
            data = np.array(cursor.fetchall()).squeeze(0)[3:]
            
            return list(labels), list(data)

        except Exception as e:
            return [],[]