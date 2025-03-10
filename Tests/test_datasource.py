from ProductionCode.datasource import DataSource
import unittest

class Test_Get_Category(unittest.TestCase):
    def test_connect(self):
        test = DataSource()
        self.assertNotEqual(test.connection, None)
    def test_from_category_get_types(self):
        test = DataSource()
        types = test.fromCategoryGetTypes('MILK')
        self.assertEqual(types[:4], ['MILK,FILLED,FLUID,W/BLEND OF HYDR VEG OILS', 'MILK,FILLED,FLUID,W/LAURIC ACID OIL', 'MILK,WHL,3.25% MILKFAT', 'MILK,PRODUCER,FLUID,3.7% MILKFAT'])
    def test_from_category_get_types_edgecase(self):
        test = DataSource()
        types = test.fromCategoryGetTypes('')
        self.assertEqual(types,[])
    def test_from_description_get_nutrition(self):
        test = DataSource()
        types = test.fromDescriptionGetNutrition('MILK,WHL,3.25% MILKFAT')
        self.assertEqual((types[0][:5],types[1][:5]), (['alpha_carotene (µg)', 'ash (g)', 'beta_carotene (µg)', 'beta_cryptoxanthin (µg)', 'carbohydrate (g)'],['0','0.69','5','0','4.52']))
    def test_from_description_get_nutrition_edgecase(self):
        test = DataSource()
        types = test.fromDescriptionGetNutrition('MILK')
        self.assertEqual(types,([],[]))
