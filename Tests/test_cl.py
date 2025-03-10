import unittest
import subprocess
from command_line import *
from ProductionCode.get_food_data import *

class Test_Command_Line(unittest.TestCase):
    def test_main_command_line_list(self):
        """tests the command_line file --list function to determine if it is functional"""
        cmd = ["python3", "-u", "command_line.py", "--list", "CHEESE"]
        # format of the line below retrieved from linked python subprocess article in assignment
        code = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'CHEESE,BLUE\nCHEESE,BRICK\nCHEESE,BRIE\nCHEESE,CAMEMBERT\nCHEESE,CARAWAY\nCHEESE,CHEDDAR\nCHEESE,CHESHIRE\nCHEESE,COLBY\nCHEESE,COTTAGE,CRMD,LRG OR SML CURD\nCHEESE,COTTAGE,CRMD,W/FRUIT\nCHEESE,COTTAGE,NONFAT,UNCRMD,DRY,LRG OR SML CURD\nCHEESE,COTTAGE,LOWFAT,2% MILKFAT\nCHEESE,COTTAGE,LOWFAT,1% MILKFAT\nCHEESE,CREAM\nCHEESE,EDAM\nCHEESE,FETA\nCHEESE,FONTINA\nCHEESE,GJETOST\nCHEESE,GOUDA\nCHEESE,GRUYERE\nCHEESE,LIMBURGER\nCHEESE,MONTEREY\nCHEESE,MOZZARELLA,WHL MILK\nCHEESE,MOZZARELLA,WHL MILK,LO MOIST\nCHEESE,MOZZARELLA,PART SKIM MILK\nCHEESE,MOZZARELLA,PART SKIM MILK,LO MOIST\nCHEESE,MUENSTER\nCHEESE,NEUFCHATEL\nCHEESE,PARMESAN,GRATED\nCHEESE,PARMESAN,HARD\nCHEESE,PORT DE SALUT\nCHEESE,PROVOLONE\nCHEESE,RICOTTA,WHOLE MILK\nCHEESE,RICOTTA,PART SKIM MILK\nCHEESE,ROMANO\nCHEESE,ROQUEFORT\nCHEESE,SWISS\nCHEESE,TILSIT\nCHEESE,PAST PROCESS,AMERICAN,W/DI NA PO4\nCHEESE,PAST PROCESS,PIMENTO\nCHEESE,PAST PROCESS,SWISS,W/DI NA PO4\nCHEESE,PARMESAN,SHREDDED\nCHEESE,PAST PROCESS,AMERICAN,WO/DI NA PO4\nCHEESE,PAST PROCESS,SWISS,WO/DI NA PO4\nCHEESE,GOAT,HARD TYPE\nCHEESE,GOAT,SEMISOFT TYPE\nCHEESE,GOAT,SOFT TYPE\nCHEESE,MEXICAN,QUESO ANEJO\nCHEESE,MEXICAN,QUESO ASADERO\nCHEESE,MEXICAN,QUESO CHIHUAHUA\nCHEESE,LOFAT,CHEDDAR OR COLBY\nCHEESE,LOW-SODIUM,CHEDDAR OR COLBY\nCHEESE,CREAM,FAT FREE\nCHEESE,PARMESAN,DRY GRATED,RED FAT\nCHEESE,PROVOLONE,RED FAT\nCHEESE,MEXICAN,BLEND,RED FAT\nCHEESE,MONTEREY,LOW FAT\nCHEESE,PAST PROCESS,CHEDDAR OR AMERICAN,FAT-FREE\nCHEESE,COTTAGE,LOWFAT,1% MILKFAT,LACTOSE RED\nCHEESE,MUENSTER,LOW FAT\nCHEESE,MOZZARELLA,NON-FAT\nCHEESE,COTTAGE,W/VEG\nCHEESE,CREAM,LOW FAT\nCHEESE,PAST PROCESS,AMERICAN,LOFAT\nCHEESE,AMERICAN CHEDDAR,IMITN\nCHEESE,PARMESAN,LO NA\nCHEESE,COTTAGE,LOWFAT,1% MILKFAT,NO NA\nCHEESE,PAST PROCESS,SWISS,LOFAT\nCHEESE,COTTAGE,LOWFAT,1% MILKFAT,W/VEG\nCHEESE,PAST PROCESS,CHEDDAR OR AMERICAN,LO NA\nCHEESE,SWISS,LOW SODIUM\nCHEESE,SWISS,LOW FAT\nCHEESE,MOZZARELLA,LO NA')


        code.terminate()

    def test_main_command_line_list_edgeCase(self):
        """tests the command_line file --list function for an edge case where a food is not included in the data set"""
        cmd = ["python3", "-u", "command_line.py", "--list", "APPLE"]
        # format of the line below retrieved from linked python subprocess article in assignment
        code = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        output, err = code.communicate()
        self.assertEqual(output.strip(), '')
        code.terminate()
    
    def test_main_command_line_health_facts(self):
        """tests the command_line file --healthfacts function to determine if it is functional"""
        cmd = ["python3", "-u", "command_line.py", "--healthfacts", "CHEESE,BLUE"]
        # format of the line below retrieved from linked python subprocess article in assignment
        code = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        output, err = code.communicate()
        self.assertEqual(output.strip(), "alpha_carotene (µg): 0\nash (g): 5.11\nbeta_carotene (µg): 74\nbeta_cryptoxanthin (µg): 0\ncarbohydrate (g): 2.34\ncholesterol (mg): 75\ncholine (mg): 15\nfiber (g): 0.0\nkilocalories (kcal): 353\nlutein_and_zeaxanthin (µg): 0\nlycopene (µg): 0\nmanganese (mg): 0.009\nniacin (mg): 1.016\npantothenic_acid (mg): 1.729\nprotein (g): 21.4\nrefuse_percentage (): 0\nretinol (µg): 192\nriboflavin (mg): 0.382\nselenium (µg): 14.5\nsugar_total (g): 0.5\nthiamin (mg): 0.029\nwater (g): 42.41\nmonosaturated_fat (g): 7.778\npolysaturated_fat (g): 0.8\nsaturated_fat (g): 18.669\ntotal_lipid (g): 28.74\nfirst_household_weight (g): 28.35\nfirst_household_weight_description (): 1 oz\nsecond_household_weight (g): 17\nsecond_household_weight_description (): 1 cubic inch\ncalcium (mg): 528\ncopper (mg): 0.04\niron (mg): 0.31\nmagnesium (mg): 23\nphosphorus (mg): 387\npotassium (mg): 256\nsodium (mg): 1395\nzinc (mg): 2.66\nvitamin_a_iu (IU): 763\nvitamin_a_rae (µg): 198\nvitamin_b12 (µg): 1.22\nvitamin_b6 (mg): 0.166\nvitamin_c (mg): 0.0\nvitamin_e (mg): 0.25\nvitamin_k (µg): 2.4")
        code.terminate()
    
    def test_main_command_line_health_facts_edgeCase(self):
        """tests the command_line file --healthfacts function for an edge case where a food is not included in the data set"""
        cmd = ["python3", "-u", "command_line.py", "--healthfacts", "APPLE,HONEYCRISP"]
        # format of the line below retrieved from linked python subprocess article in assignment
        code = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'No food named APPLE,HONEYCRISP found.')
        code.terminate()


class Test_Get_Data(unittest.TestCase):
    def test_get_data(self):
        """tests the get_data function in the get_food_data file to determine that it is creating the correct DataFrame"""
        self.assertEqual("\n".join(list(get_data(dummy=True))),"Category\nDescription\nNutrient Data Bank Number\nAlpha Carotene\nAsh\nBeta Carotene\nBeta Cryptoxanthin\nCarbohydrate")
    
    def test__typeError_get_data(self):
        """tests an edge case of the get_data function in the get_food_data file to determine that
        the correct number of arguments were declared"""
        with self.assertRaises(TypeError):
            get_data("argument")

    def test_fetch_category(self):
        """tests the fetch_category function in the get_food_data file with a CHEESE example
        to determine that it is functional"""
        self.assertEqual("\n".join(list(fetch_category("CHEESE"))), 'CHEESE,BLUE\nCHEESE,BRICK\nCHEESE,BRIE')

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
        self.assertEqual("\n".join(list(health_facts("CHEESE,BLUE"))), 'Alpha Carotene\nAsh\nBeta Carotene\nBeta Cryptoxanthin\nCarbohydrate')

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