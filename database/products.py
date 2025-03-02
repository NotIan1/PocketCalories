products = [
    ("1", "salt", "Salt.jpg", 0, 0, 0, 0, "g", "other", False),                # A pinch -> ~0 cal
    ("2", "sugar", "Sugar.jpg", 16, 0, 0, 100, "g", "carb", False),            # ~1 tsp
    ("3", "olive oil", "Olive_oil.jpg", 120, 0, 100, 0, "ml", "fat", False),   # ~1 tbsp
    ("4", "flour", "Flour.jpg", 100, 10, 1, 76, "g", "carb", False),           # ~3/4 cup
    ("5", "butter", "Butter.jpg", 100, 0, 81, 1, "g", "fat", False),           # ~1 tbsp
    ("6", "egg", "Egg.jpg", 70, 13, 11, 1, "unit", "protein", False),          # 1 large egg
    ("7", "milk", "Milk.jpg", 60, 3, 1, 5, "ml", "carb", False),               # ~1/2 cup
    ("8", "tomato", "Tomatoes.jpg", 22, 1, 0, 4, "g", "carb", True),           # 1 medium tomato
    ("9", "onion", "Onions.jpg", 44, 1, 0, 9, "g", "carb", False),             # 1 medium onion
    ("10", "garlic", " Garlic.jpg", 5, 6, 0, 33, "g", "carb", False),          # ~1 clove
    ("11", "chicken breast", "Chicken_breast.jpg", 200, 31, 3, 0, "g", "protein", False),
    ("12", "beef", "Beef.jpg", 250, 26, 15, 0, "g", "protein", False),         # ~4 oz portion
    ("13", "carrot", "Carrots.jpg", 25, 1, 0, 10, "g", "carb", True),          # 1 medium
    ("14", "potato", "Potato.jpg", 110, 2, 0, 17, "g", "carb", False),         # 1 small (~150 g)
    ("15", "rice", "Rice.jpg", 200, 2, 0, 28, "g", "carb", False),             # ~1 cup cooked
    ("16", "pasta", "Pasta.jpg", 200, 5, 1, 25, "g", "carb", False),           # ~1 cup cooked
    ("17", "cheese", "Cheese.jpg", 110, 25, 33, 1, "g", "fat", True),          # ~1 slice (28 g)
    ("18", "yogurt", "Yogurt.jpg", 120, 10, 0, 4, "ml", "protein", True),      # ~1 small container
    ("19", "spinach", "Spinach.jpg", 7, 3, 0, 4, "g", "carb", False),          # ~1 cup raw
    ("20", "broccoli", "Broccoli.jpg", 31, 3, 0, 7, "g", "carb", False),       # ~1 cup chopped
    ("21", "apple", "Apples.jpg", 95, 0, 0, 14, "g", "carb", True),            # 1 medium
    ("22", "banana", "Banana.jpg", 105, 1, 0, 27, "g", "carb", True),          # 1 medium
    ("23", "strawberry", "Strawberry.jpg", 18, 1, 0, 8, "g", "carb", True),    # ~1/2 cup
    ("24", "honey", "Honey.jpg", 64, 0, 0, 82, "g", "carb", False),            # ~1 tbsp
    ("25", "baking powder", "Baking_powder.jpg", 2, 0, 0, 28, "g", "carb", False),
    ("26", "baking soda", "Baking_soda.jpg", 0, 0, 0, 0, "g", "other", False),
    ("27", "vanilla extract", "Vanilla_extract.jpg", 12, 0, 0, 13, "ml", "carb", False),
    ("28", "cinnamon", "Cinnamon.jpg", 6, 4, 1, 81, "g", "carb", False),       # ~1 tsp
    ("29", "nutmeg", "Nutmeg.jpg", 6, 6, 36, 49, "g", "carb", False),          # ~1 tsp
    ("30", "lemon", "Lemon.jpg", 17, 1, 0, 9, "g", "carb", False),             # 1 medium
    ("31", "orange", "Orange.jpg", 62, 1, 0, 12, "g", "carb", True),           # 1 medium
    ("32", "cucumber", "Cucumber.jpg", 8, 1, 0, 4, "g", "carb", True),         # ~1/2 cup slices
    ("33", "bell pepper", "Bell_pepper.jpg", 31, 1, 0, 6, "g", "carb", True),  # 1 medium
    ("34", "mushroom", "Mushroom.jpg", 4, 3, 0, 3, "g", "carb", False),        # 1 medium
    ("35", "zucchini", "Zucchini.jpg", 19, 1, 0, 3, "g", "carb", False),       # ~1 cup sliced
    ("36", "parsley", "parsley.jpg", 2, 3, 1, 6, "g", "carb", False),          # ~1 tbsp
    ("37", "basil", "basil.jpg", 2, 3, 0, 2, "g", "protein", False),           # ~1 tbsp
    ("38", "thyme", "thyme.jpg", 1, 6, 1, 24, "g", "carb", False),            # ~1 tsp
    ("39", "rosemary", "rosemary.jpg", 2, 3, 6, 21, "g", "carb", False),       # ~1 tbsp
    ("40", "oregano", "oregano.jpg", 3, 9, 4, 69, "g", "carb", False),         # ~1 tsp
    ("41", "bay leaf", "bay_leaf.jpg", 1, 8, 8, 75, "g", "carb", False),       # 1 leaf
    ("42", "mint", "mint.jpg", 2, 3, 1, 8, "g", "carb", False),               # ~1 tbsp
    ("43", "celery", "celery.jpg", 6, 1, 0, 3, "g", "carb", True),             # 1 medium stalk
    ("44", "lettuce", "lettuce.jpg", 5, 1, 0, 2, "g", "carb", False),          # ~1 cup shredded
    ("45", "kale", "kale.jpg", 33, 4, 1, 9, "g", "carb", False),               # ~1 cup chopped
    ("46", "cauliflower", "cauliflower.jpg", 25, 2, 0, 5, "g", "carb", True),  # ~1 cup
    ("47", "cabbage", "cabbage.jpg", 22, 1, 0, 6, "g", "carb", False),         # ~1 cup
    ("48", "peas", "peas.jpg", 62, 5, 0, 14, "g", "carb", True),               # ~1/2 cup
    ("49", "green beans", "green_beans.jpg", 31, 2, 0, 7, "g", "carb", False), # ~1 cup
    ("50", "corn", "corn.jpg", 88, 3, 1, 19, "g", "carb", False),             # ~1 ear
    ("51", "chickpeas", "chickpeas.jpg", 269, 9, 3, 27, "g", "carb", False),   # ~1 cup cooked
    ("52", "lentils", "lentils.jpg", 230, 9, 0, 20, "g", "carb", False),       # ~1 cup cooked
    ("53", "black beans", "black_beans.jpg", 227, 9, 0, 24, "g", "carb", False),
    ("54", "kidney beans", "kidney_beans.jpg", 225, 9, 0, 22, "g", "carb", False),
    ("55", "quinoa", "quinoa.jpg", 222, 4, 2, 21, "g", "carb", False),         # ~1 cup cooked
    ("56", "oats", "oats.jpg", 150, 17, 7, 66, "g", "carb", False),            # ~1/2 cup dry
    ("57", "almonds", "almonds.jpg", 164, 21, 50, 22, "g", "fat", True),       # ~1 oz
    ("58", "walnuts", "walnuts.jpg", 185, 15, 65, 14, "g", "fat", True),       # ~1 oz
    ("59", "peanuts", "peanuts.jpg", 161, 26, 49, 16, "g", "fat", True),       # ~1 oz
    ("60", "cashews", "cashews.jpg", 155, 18, 44, 30, "g", "fat", True),       # ~1 oz
    ("61", "sunflower seeds", "sunflower_seeds.jpg", 164, 21, 51, 20, "g", "fat", True),
    ("62", "pumpkin seeds", "pumpkin_seeds.jpg", 126, 30, 49, 11, "g", "fat", True),
    ("63", "raisins", "raisins.jpg", 129, 3, 0, 79, "g", "carb", True),        # ~1/4 cup
    ("64", "dates", "dates.jpg", 66, 2, 0, 75, "g", "carb", True),            # ~1 large date
    ("65", "apricots", "apricots.jpg", 34, 1, 0, 11, "g", "carb", True),       # ~2 small apricots
    ("66", "pineapple", "pineapple.jpg", 82, 0, 0, 13, "g", "carb", True),     # ~1 cup chunks
    ("67", "mango", "mango.jpg", 99, 1, 0, 15, "g", "carb", True),            # ~1 cup
    ("68", "grapes", "grapes.jpg", 62, 0, 0, 18, "g", "carb", True),          # ~1 cup
    ("69", "blueberries", "blueberries.jpg", 85, 0, 0, 14, "g", "carb", True), # ~1 cup
    ("70", "raspberries", "raspberries.jpg", 64, 1, 0, 12, "g", "carb", True),
    ("71", "blackberries", "blackberries.jpg", 62, 1, 0, 10, "g", "carb", True),
    ("72", "peach", "peach.jpg", 58, 1, 0, 10, "g", "carb", True),
    ("73", "plum", "plum.jpg", 30, 0, 0, 11, "g", "carb", True),
    ("74", "cherries", "cherries.jpg", 77, 1, 0, 12, "g", "carb", True),
    ("75", "coconut", "coconut.jpg", 283, 3, 33, 15, "g", "fat", True),        # ~1 cup shredded
    ("76", "avocado", "avocado.jpg", 234, 2, 15, 9, "g", "fat", True),         # 1 medium
    ("77", "pomegranate", "pomegranate.jpg", 234, 1, 1, 19, "g", "carb", True),# 1 whole
    ("78", "watermelon", "watermelon.jpg", 46, 1, 0, 8, "g", "carb", True),    # ~1 cup
    ("79", "cantaloupe", "cantaloupe.jpg", 53, 1, 0, 8, "g", "carb", True),
    ("80", "pear", "pear.jpg", 101, 0, 0, 15, "g", "carb", True),
    ("81", "fig", "fig.jpg", 37, 1, 0, 19, "g", "carb", True),                # 1 medium
    ("82", "papaya", "papaya.jpg", 55, 0, 0, 11, "g", "carb", True),           # ~1 cup
    ("83", "guava", "guava.jpg", 37, 2, 1, 14, "g", "carb", True),            # 1 small
    ("84", "kiwi", "kiwi.jpg", 42, 1, 0, 15, "g", "carb", True),              # 1 medium
    ("85", "lime", "lime.jpg", 20, 0, 0, 10, "g", "carb", False),             # 1 whole
    ("86", "ginger", "ginger.jpg", 5, 2, 0, 18, "g", "carb", False),          # ~1 inch
    ("87", "turmeric", "turmeric.jpg", 10, 7, 4, 67, "g", "carb", False),      # ~1 tbsp
    ("88", "cloves", "cloves.jpg", 6, 6, 13, 65, "g", "carb", False),         # ~1 tsp
    ("89", "cardamom", "cardamom.jpg", 18, 11, 7, 68, "g", "carb", False),     # ~1 tbsp
    ("90", "fennel", "fennel.jpg", 27, 1, 0, 7, "g", "carb", False),           # ~1 cup
    ("91", "coriander", "coriander.jpg", 5, 2, 1, 3, "g", "carb", False),      # ~1 tbsp
    ("92", "mustard seeds", "mustard_seeds.jpg", 20, 26, 36, 28, "g", "fat", False),
    ("93", "poppy seeds", "poppy_seeds.jpg", 46, 18, 42, 28, "g", "fat", False),
    ("94", "sesame seeds", "sesame_seeds.jpg", 51, 18, 50, 23, "g", "fat", False),
    ("95", "saffron", "saffron.jpg", 2, 11, 6, 65, "g", "carb", False),        # pinch
    ("96", "almond milk", "almond_milk.jpg", 30, 0, 1, 1, "ml", "carb", False),# ~1 cup
    ("97", "coconut milk", "coconut_milk.jpg", 150, 2, 24, 6, "ml", "fat", False),
    ("98", "soy sauce", "soy_sauce.jpg", 10, 8, 0, 5, "ml", "protein", False), # ~1 tbsp
    ("99", "apple cider vinegar", "apple_cider_vinegar.jpg", 3, 0, 0, 1, "ml", "carb", False),
    ("100", "red wine vinegar", "red_wine_vinegar.jpg", 3, 0, 0, 0, "ml", "other", False),
    ("101", "extra virgin olive oil", "extra_virgin_olive_oil.jpg", 120, 0, 100, 0, "ml", "fat", False),
    ("102", "rye flour", "rye_flour.jpg", 100, 10, 1, 76, "g", "carb", False),
    ("103", "spelt flour", "spelt_flour.jpg", 100, 14, 2, 70, "g", "carb", False),
    ("104", "cocoa powder", "cocoa_powder.jpg", 12, 20, 13, 58, "g", "carb", False),  # ~1 tbsp
    # (105) "egg" REMOVED - duplicate
    ("106", "maple syrup", "maple_syrup.jpg", 52, 0, 0, 67, "g", "carb", False),       # ~1 tbsp
    ("107", "dark chocolate", "dark_chocolate.jpg", 170, 7, 42, 45, "g", "fat", True), # ~1 oz
    ("108", "sunflower oil", "sunflower_oil.jpg", 120, 0, 100, 0, "ml", "fat", False), # ~1 tbsp
    ("109", "black tea", "black_tea.jpg", 2, 0, 0, 0, "g", "other", False),           # ~1 cup brewed
    ("110", "malt extract", "malt_extract.jpg", 80, 5, 0, 69, "g", "carb", False),     # ~1 tbsp
    ("111", "dark muscovado sugar", "dark_muscovado_sugar.jpg", 16, 0, 0, 95, "g", "carb", False),
    ("112", "mixed dried fruit", "mixed_dried_fruit.jpg", 130, 2, 0, 75, "g", "carb", True),  # ~1/4 cup
    ("113", "plain flour", "plain_flour.jpg", 100, 10, 1, 76, "g", "carb", False),
    ("114", "bicarbonate of soda", "bicarbonate_of_soda.jpg", 0, 0, 0, 0, "g", "other", False),
    ("115", "full-fat milk", "full-fat_milk.jpg", 75, 3, 3, 5, "ml", "carb", False),  # ~1/2 cup
    ("116", "natural yogurt", "natural_yogurt.jpg", 100, 10, 0, 4, "ml", "protein", True),
    ("117", "frozen fruits of the forest", "frozen_fruits_of_the_forest.jpg", 70, 1, 0, 12, "g", "carb", True),
    ("118", "chia seeds", "chia_seeds.jpg", 138, 17, 31, 42, "g", "fat", True),       # ~1 oz
    ("119", "goji berries", "goji_berries.jpg", 98, 14, 1, 77, "g", "carb", True),     # ~1 oz
    ("120", "mixed seeds", "mixed_seeds.jpg", 160, 20, 47, 23, "g", "fat", True),      # ~1 oz
    ("121", "soft dried apricots", "soft_dried_apricots.jpg", 84, 3, 0, 63, "g", "carb", True),
    ("122", "soft dried dates", "soft_dried_dates.jpg", 66, 2, 0, 75, "g", "carb", True),
    ("123", "dried cherries", "dried_cherries.jpg", 80, 2, 1, 78, "g", "carb", True),
    ("124", "coconut oil", "coconut_oil.jpg", 120, 0, 100, 0, "ml", "fat", False),     # ~1 tbsp
    ("125", "toasted sesame seeds", "toasted_sesame_seeds.jpg", 51, 0, 0, 0, "g", "other", False),
    ("126", "shrimp", "shrimp.jpg", 99, 24, 0, 0, "g", "protein", False),             # ~3 oz portion
    ("127", "lemon juice", "lemon_juice.jpg", 3, 1, 0, 7, "ml", "other", False),      # ~1 tbsp
    ("128", "pepper", "pepper.jpg", 6, 10, 3, 64, "g", "other", False),               # ~1 tsp
    ("129", "romaine lettuce", "romaine_lettuce.jpg", 8, 1, 0, 3, "g", "carb", False),# ~1 cup shredded
    ("130", "croutons", "croutons.jpg", 50, 12, 10, 71, "g", "carb", False),          # ~1/4 cup
    ("131", "parmesan cheese", "parmesan_cheese.jpg", 110, 38, 29, 4, "g", "fat", True), # ~1 oz
    ("132", "caesar dressing", "caesar_dressing.jpg", 80, 3, 29, 7, "ml", "fat", False), # ~1 tbsp
    # (133) "bell peppers" REMOVED - duplicate
    ("134", "ground beef", "ground_beef.jpg", 250, 17, 20, 0, "g", "protein", False),   # ~4 oz
    ("135", "tomato sauce", "tomato_sauce.jpg", 70, 2, 0, 15, "g", "carb", False),      # ~1/2 cup
    ("136", "brown sugar", "brown_sugar.jpg", 17, 0, 0, 98, "g", "carb", False),        # ~1 tsp
    ("137", "chocolate chips", "chocolate_chips.jpg", 70, 4, 25, 61, "g", "fat", True),  # ~1 tbsp
    ("138", "potatoes", "potatoes.jpg", 110, 2, 0, 17, "g", "carb", False),
    # (139) "carrot" REMOVED - duplicate
    ("140", "curry paste", "curry_paste.jpg", 40, 3, 6, 20, "g", "other", False),       # ~1 tbsp
    ("141", "salmon fillets", "salmon_fillets.jpg", 200, 22, 12, 0, "g", "protein", False), # ~3–4 oz
    ("142", "dill", "dill.jpg", 2, 3, 1, 7, "g", "other", False),                       # ~1 tbsp
    ("143", "cherry tomatoes", "cherry_tomatoes.jpg", 27, 1, 0, 3, "g", "carb", True),  # ~1 cup
    ("144", "red onion", "red_onion.jpg", 46, 1, 0, 9, "g", "carb", False),             # 1 medium
    ("145", "garam masala", "garam_masala.jpg", 7, 4, 3, 15, "g", "other", False),      # ~1 tsp
    ("146", "cumin", "cumin.jpg", 8, 18, 22, 44, "g", "other", False),                  # ~1 tsp
    ("147", "tomato puree", "tomato_puree.jpg", 33, 3, 1, 14, "g", "carb", False),      # ~2 tbsp
    ("148", "cream", "cream.jpg", 52, 2, 36, 3, "ml", "fat", False),                    # ~1 tbsp
    ("149", "pizza dough", "pizza_dough.jpg", 200, 9, 3, 47, "g", "carb", False),       # ~1 slice worth
    ("150", "mozzarella cheese", "mozzarella_cheese.jpg", 85, 28, 17, 3, "g", "fat", True),
    ("151", "fresh basil", "fresh_basil.jpg", 1, 3, 0, 2, "g", "other", False),
    ("152", "vegetable broth", "vegetable_broth.jpg", 12, 1, 0, 2, "ml", "other", False), # ~1 cup
    ("153", "tomato paste", "tomato_paste.jpg", 33, 3, 1, 14, "g", "carb", False),
    ("154", "bread", "bread.jpg", 80, 9, 3, 49, "g", "carb", False),                    # ~1 slice
    ("155", "chili flakes", "chili_flakes.jpg", 6, 12, 14, 50, "g", "other", False),    # ~1 tsp
    ("156", "white fish fillets", "white_fish_fillets.jpg", 120, 20, 1, 0, "g", "protein", False),
    ("157", "tortillas", "tortillas.jpg", 150, 8, 7, 50, "g", "carb", False),           # 1 medium
    ("158", "lime juice", "lime_juice.jpg", 3, 0, 0, 8, "ml", "other", False),          # ~1 tbsp
    ("159", "mayonnaise", "mayonnaise.jpg", 90, 1, 75, 1, "g", "fat", False),           # ~1 tbsp
    ("160", "chili powder", "chili_powder.jpg", 6, 14, 13, 31, "g", "other", False),    # ~1 tsp
    ("161", "feta cheese", "feta_cheese.jpg", 75, 14, 21, 4, "g", "fat", True),         # ~1 oz
    ("162", "phyllo pastry", "phyllo_pastry.jpg", 75, 8, 3, 54, "g", "carb", False),     # ~2 sheets
    ("163", "snap peas", "snap_peas.jpg", 27, 3, 0, 7, "g", "carb", True),              # ~1 cup
    ("164", "sesame oil", "sesame_oil.jpg", 120, 0, 100, 0, "ml", "fat", False),        # ~1 tbsp
    ("165", "burger buns", "burger_buns.jpg", 150, 8, 3, 45, "g", "carb", False),       # 1 bun
    ("166", "ketchup", "ketchup.jpg", 15, 1, 0, 26, "g", "carb", False),                # ~1 tbsp
    ("167", "mustard", "mustard.jpg", 9, 4, 4, 7, "g", "other", False),                 # ~1 tbsp
    ("168", "spaghetti", "spaghetti.jpg", 200, 6, 1, 31, "g", "carb", False),           # ~1 cup cooked
    ("169", "canned tomatoes", "canned_tomatoes.jpg", 40, 0, 0, 4, "g", "carb", False), # ~1 cup
    ("170", "ice cubes", "ice_cubes.jpg", 0, 0, 0, 0, "other", "other", False),
    ("171", "beef strips", "beef_strips.jpg", 250, 26, 15, 0, "g", "protein", False),
    ("173", "sour cream", "sour_cream.jpg", 60, 2, 20, 4, "ml", "fat", False),          # ~2 tbsp
    ("174", "beef broth", "beef_broth.jpg", 31, 1, 0, 1, "ml", "other", False),         # ~1 cup
    ("175", "egg noodles", "egg_noodles.jpg", 221, 5, 2, 25, "g", "carb", False),       # ~1 cup cooked
    ("176", "greek yogurt", "greek_yogurt.jpg", 130, 10, 0, 4, "ml", "protein", True),  # ~150 g
    ("177", "granola", "granola.jpg", 240, 14, 20, 64, "g", "carb", True),              # ~1/2 cup
    ("178", "berries", "berries.jpg", 42, 1, 0, 14, "g", "carb", True),                 # ~1/2 cup
    ("179", "self-raising flour", "self-raising_flour.jpg", 100, 10, 1, 75, "g", "carb", False),
    ("180", "caster sugar", "caster_sugar.jpg", 16, 0, 0, 100, "g", "carb", False),     # ~1 tsp
    ("181", "lemon zest", "lemon_zest.jpg", 3, 1, 0, 16, "g", "other", False),          # ~1 tsp
    ("182", "icing sugar", "icing_sugar.jpg", 31, 0, 0, 100, "g", "carb", False)        # ~1 tbsp
]
