import unittest
import subprocess
from command_line import *
from ProductionCode.get_food_data import*
import pandas as pd
import pandas.testing as pdt

class Test_command_line(unittest.TestCase):
    def test_main_command_line_list(self):
        """tests the command_line file --list function to determine if it is functional"""
        cmd = ["python3", "-u", "command_line.py", "--list", "CHEESE"]
        # format of the line below retrieved from linked python subprocess article in assignment
        code = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'CHEESE,BLUE\nCHEESE,BRICK\nCHEESE,BRIE')
        code.terminate()
    
    def test_main_command_line_health_facts(self):
        """tests the command_line file --healthfacts function to determine if it is functional"""
        cmd = ["python3", "-u", "command_line.py", "--healthfacts", "CHEESE,BLUE"]
        # format of the line below retrieved from linked python subprocess article in assignment
        code = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'Alpha Carotene: 0.0\nAsh: 5.11\nBeta Carotene: 74.0\nBeta Cryptoxanthin: 0.0\nCarbohydrate: 2.34')
        code.terminate()


class Test_get_food_data(unittest.TestCase):
    def test_get_df(self):
        """tests the get_df function in the get_food_data file to determine that it is creating the correct DataFrame"""
        csv_df = pd.read_csv("Data/food_nutrition_sample.csv")
        pdt.assert_frame_equal(get_df(), csv_df)
    
    def test__typeError_get_df(self):
        """tests an edge case of the get_df function in the get_food_data file to determine that
        the correct number of arguments were declared"""
        with self.assertRaises(TypeError):
            get_df("argument")

    def test_fetch_category(self):
        """tests the fetch_category function in the get_food_data file with a CHEESE example
        to determine that it is functional"""
        df = get_df()
        category = "CHEESE"
        pdt.assert_series_equal(fetch_category("CHEESE"), df[df["Category"]==category]["Description"])

    def test_typeError_fetch_category(self):
        """tests an edge case of the fetch_category function in the get_food_data file to determine that
        enough arguments were declared"""
        with self.assertRaises(TypeError):
            fetch_category()
    
    def test_typeError2_fetch_category(self):
        """tests an edge case of the fetch_category function in the get_food_data file to determine that
        too many arguments were not declared"""
        with self.assertRaises(TypeError):
            fetch_category("argument 1", "argument 2")
    
    def test_health_facts(self):
        """tests the health_facts function in the get_food_data file with a CHEESE,BLUE example
        to determine that it is functional"""
        df = get_df()
        description = "CHEESE,BLUE"
        pdt.assert_frame_equal(health_facts("CHEESE,BLUE"), 
                               df[df["Description"] == description].drop(columns=["Category","Description","Nutrient Data Bank Number"]))

    def test_typeError_health_facts(self):
        """tests an edge case of the health_facts function in the get_food_data file to determine that
        enough arguments were declared"""
        with self.assertRaises(TypeError):
            health_facts()
    
    def test_typeError2_health_facts(self):
        """tests an edge case of the health_facts function in the get_food_data file to determine that
        too many arguments were not declared"""
        with self.assertRaises(TypeError):
            health_facts("argument 1", "argument 2")


if __name__ == '__main__':
    unittest.main()