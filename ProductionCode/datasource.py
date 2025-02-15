import psycopg2
import ProductionCode.psqlConfig as config

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

            # make the query using %s as a placeholder for the variable
            query = "SELECT \"Description\" FROM food_nutrition WHERE \"Category\" = %s;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (category,))
            print(cursor.fetchall())

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
        
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

            # make the query using %s as a placeholder for the variable
            query = "SELECT * FROM food_nutrition WHERE \"Description\" = %s;"

            # executing the query and saying that the type variable 
            # should be placed where %s was, the trailing comma is important!
            cursor.execute(query, (description,))
            print(cursor.fetchall())

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None