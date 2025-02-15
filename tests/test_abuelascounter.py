# mypy: allow-untyped-defs

from recipe_scrapers.abuelascounter import AbuelasCounter
from tests import ScraperTest


# test recipe's URL
# https://abuelascounter.com/alita-olivas-roast-chicken/
class TestAbuelasCounterScraper(ScraperTest):
    scraper_class = AbuelasCounter

    def test_host(self):
        self.assertEqual("abuelascounter.com", self.harvester_class.host())

    # @unittest.skip("canonical_url is not available from this webpage")
    def canonical_url(self):
        self.assertEqual(
            "https://abuelascounter.com/alita-olivas-roast-chicken/",
            self.harvester_class.host(),
        )

    def test_author(self):
        self.assertEqual("Abuelas Cuban Counter", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Alita Oliva’s Roast Chicken", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Entree", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(105, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://abuelascounter.com/wp-content/uploads/2023/01/Roast-Chicken-Recipe.jpeg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 - 3 pound whole roaster chicken",
                "4 yellow onions, peeled and sliced thinly",
                "1 onion, left whole",
                "2 teaspoons of garlic powder",
                "1/4 cup of soy sauce or dale’s marinade seasoning",
                "Juice of 1 lime",
                "Juice of 1 orange",
                "1/3 cup olive oil",
                "1/2 teaspoon of ground mustard",
                "1 teaspoon of onion powder",
                "1 teaspoon of paprika",
                "salt and black pepper",
                "2 teaspoons of apple cider vinegar",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join(
                [
                    "Preheat the oven to 425 degrees.",
                    "Spread the bottom of your roasting pan with the sliced onions. Season the onions with 2 tablespoons of oil and salt and pepper.",
                    "Time to Prep the Chicken: Remove the chicken giblets. Rinse the chicken inside and out under cold water. Pat the outside dry and put it in a roasting pan.",
                    "Whisk all the ingredients into the olive oil until emulsified.",
                    "Sprinkle the chicken with a generous amount of salt and pepper on all sides. Season liberally. You even want to add some salt to the cavity of the chicken. Don’t be afraid.",
                    "Add the whole onion to the inside of the cavity. You can also add fresh herbs or bay leaves to the cavity.",
                    "Pour the marinade over the chicken. Marinate it overnight in the fridge or just for a few minutes.",
                    "Roast the chicken for 30 minutes at 425 degrees then add ¼ cup of water to the bottom of the pan to be sure the onions don’t get too much color and drop the temperature to 350 degrees.",
                    "Roast for another 50-60 minutes. The chicken will roast for a about 90 minutes total.",
                    "The chicken is ready once the skin is golden brown and the juices run completely clear when you cut with a knife. If you are using a meat thermometer it should read 160 degrees between the breast and thigh area. Once you pull the chicken out of the oven let it rest for 15 minutes then carve and serve.",
                ]
            ),
            self.harvester_class.instructions(),
        )

    def test_cuisine(self):
        self.assertEqual("Cuban,American", self.harvester_class.cuisine())
