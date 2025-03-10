from ProductionCode.datasource import DataSource
import unittest

class Test_Get_Category(unittest.TestCase):
    def test_connect(self):
        test = DataSource()
        self.assertNotEqual(test.connection, None)
    def test_from_category_get_types(self):
        test = DataSource()
        types = test.fromCategoryGetTypes('MILK')
        self.assertEqual(types, ['MILK,FILLED,FLUID,W/BLEND OF HYDR VEG OILS', 'MILK,FILLED,FLUID,W/LAURIC ACID OIL', 'MILK,WHL,3.25% MILKFAT', 'MILK,PRODUCER,FLUID,3.7% MILKFAT', 'MILK,RED FAT,FLUID,2%MILKFAT,W/ADDED VIT A', 'MILK,RED FAT,FLUID,2% MILKFAT,W/ NONFAT MILK SOL&VIT A', 'MILK,RED FAT,FLUID,2% MILKFAT,PROT FORT,W/ VIT A', 'MILK,LOWFAT,FLUID,1% MILKFAT,W/ VIT A', 'MILK,LOWFAT,FLUID,1% MILKFAT,W/ NONFAT MILK SOL&VIT A', 'MILK,LOWFAT,FLUID,1% MILKFAT,PROT FORT,W/ VIT A', 'MILK,NONFAT,FLUID,W/ VIT A (FAT FREE OR SKIM)', 'MILK,NONFAT,FLUID,W/ NONFAT MILK SOL&VIT A (FAT FREE/SKIM)', 'MILK,NONFAT,FLUID,PROT FORT,W/ VIT A (FAT FREE/SKIM)', 'MILK,BTTRMLK,FLUID,CULTURED,LOWFAT', 'MILK,LOW SODIUM,FLUID', 'MILK,DRY,WHOLE', 'MILK,DRY,NONFAT,REG,WO/ VIT A', 'MILK,DRY,NONFAT,INST,W/ VIT A', 'MILK,DRY,NONFAT,CA RED', 'MILK,BUTTERMILK,DRIED', 'MILK,CND,COND,SWTND', 'MILK,CND,EVAP,WO/ VIT A', 'MILK,CND,EVAP,NONFAT', 'MILK,CHOC,FLUID,COMM,', 'MILK,CHOC,FLUID,COMM,RED FAT', 'MILK,CHOC,FLUID,COMM,LOWFAT', 'MILK,CHOC BEV,HOT COCOA,HOMEMADE', 'MILK,GOAT,FLUID', 'MILK,HUMAN,MATURE,FLUID', 'MILK,INDIAN BUFFALO,FLUID', 'MILK,SHEEP,FLUID', 'MILK,NONFAT,FLUID,WO/ VIT A (FAT FREE OR SKIM)', 'MILK,RED FAT,FLUID,2% MILKFAT,W/ NONFAT MILK SOL,WO/ VIT A', 'MILK,CND,EVAP,W/ VIT A', 'MILK,DRY,NONFAT,REG,W/ VIT A', 'MILK,DRY,NONFAT,INST,WO/ VIT A', 'MILK,CHOC,FLUID,COMM,RED FAT,W/ ADDED CA', 'MILK,BTTRMLK,FLUID,CULTURED,RED FAT', 'MILK,FLUID,NONFAT,CA FORT (FAT FREE OR SKIM)', 'MILK,IMITATION,NON-SOY'])
    def test_from_category_get_types_edgecase(self):
        test = DataSource()
        types = test.fromCategoryGetTypes('')
        self.assertEqual(types,[])
    def test_from_description_get_nutrition(self):
        test = DataSource()
        types = test.fromDescriptionGetNutrition('MILK,WHL,3.25% MILKFAT')
        self.assertEqual(types, (['alpha_carotene (µg)', 'ash (g)', 'beta_carotene (µg)', 'beta_cryptoxanthin (µg)', 'carbohydrate (g)', 'cholesterol (mg)', 'choline (mg)', 'fiber (g)', 'kilocalories (kcal)', 'lutein_and_zeaxanthin (µg)', 'lycopene (µg)', 'manganese (mg)', 'niacin (mg)', 'pantothenic_acid (mg)', 'protein (g)', 'refuse_percentage ()', 'retinol (µg)', 'riboflavin (mg)', 'selenium (µg)', 'sugar_total (g)', 'thiamin (mg)', 'water (g)', 'monosaturated_fat (g)', 'polysaturated_fat (g)', 'saturated_fat (g)', 'total_lipid (g)', 'first_household_weight (g)', 'first_household_weight_description ()', 'second_household_weight (g)', 'second_household_weight_description ()', 'calcium (mg)', 'copper (mg)', 'iron (mg)', 'magnesium (mg)', 'phosphorus (mg)', 'potassium (mg)', 'sodium (mg)', 'zinc (mg)', 'vitamin_a_iu (IU)', 'vitamin_a_rae (µg)', 'vitamin_b12 (µg)', 'vitamin_b6 (mg)', 'vitamin_c (mg)', 'vitamin_e (mg)', 'vitamin_k (µg)'], ['0', '0.69', '5', '0', '4.52', '10', '14', '0.0', '60', '0', '0', '0.003', '0.107', '0.362', '3.22', '0', '28', '0.183', '3.7', '5.260000229', '0.044', '88.32', '0.812', '0.195', '1.865', '3.25', '244.0', '1 cup', '15', '1 tbsp', '113', '0.011', '0.03', '10', '91', '143', '40', '0.4', '102', '28', '0.44', '0.036', '0.0', '0.06', '0.2']))
    def test_from_description_get_nutrition_edgecase(self):
        test = DataSource()
        types = test.fromDescriptionGetNutrition('MILK')
        self.assertEqual(types,([],[]))
