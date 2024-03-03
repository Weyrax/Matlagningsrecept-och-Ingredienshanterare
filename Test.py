import unittest
from main import RecipeManager

class TestRecipeManager(unittest.TestCase):
    def setUp(self):
        self.manager = RecipeManager()

    def test_add_and_get_recipe(self):
        self.manager.add_recipe("Testrecept", ["Ingrediens1", "Ingrediens2"], ["Steg 1", "Steg 2"])
        self.assertIn("Testrecept", self.manager.recipes, "Receptet ska finnas efter tillägg.")
        # Här kan du lägga till mer detaljerad kontroll av ingredienser och instruktioner

    def test_remove_recipe(self):
        self.manager.add_recipe("Testrecept", ["Ingrediens1"], ["Steg 1"])
        self.manager.remove_recipe("Testrecept")
        self.assertNotIn("Testrecept", self.manager.recipes, "Receptet ska inte finnas efter borttagning.")

    # Test för list_recipes och get_recipe kan inkludera att kontrollera output mot förväntad output, vilket kan kräva mocking.

if __name__ == '__main__':
    unittest.main()
