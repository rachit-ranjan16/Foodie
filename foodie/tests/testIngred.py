import unittest
from ..ingreds import ingreds


class testIngred(unittest.TestCase):

    def setUp(self):
        self.ing = ingreds(ing_list=['bread', 'butter', 'milk'])
        print(self.ing.ing_list)

    def testGetIngredients(self):
        # TODO figure out testing strategy
        pass

    def test_get_pretty_ingred_str(self):
        pretty_ings = self.ing.get_pretty_ingred_str()
        self.assertEqual(len(pretty_ings.split(',')), 3)
        self.assertEqual(pretty_ings[0:5], 'bread')

    def test_find_missing_ingreds(self):
        all_ings = ['bread', 'eggs', 'sugar', 'butter', 'flour', 'chocolate', 'milk']
        missed = self.ing.find_missing_ingreds(all_ings=all_ings)
        print(missed)
        self.assertEqual(missed['bread'], False)
        self.assertEqual(missed['butter'], False)
        self.assertEqual(missed['milk'], False)
        self.assertEqual(missed['chocolate'], True)