import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('recipe_database.db')
    cursor = conn.cursor()

    # Create Dishes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dishes (
            id TEXT PRIMARY KEY,
            name TEXT,
            image TEXT,
            description TEXT,
            time_to_make INTEGER,
            serves INTEGER,
            difficulty TEXT,
            recipe TEXT,
            calories INTEGER,
            protein INTEGER,
            fat INTEGER,
            carbs INTEGER
        )
    ''')

    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id TEXT PRIMARY KEY,
            name TEXT,
            image TEXT,
            calories INTEGER,
            protein INTEGER,
            fat INTEGER,
            carbs INTEGER,
            measurement TEXT,
            category TEXT
        )
    ''')

    # Create many_to_many table for Dishes and Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DishProduct (
            dish_id TEXT,
            product_id TEXT,
            quantity TEXT,
            PRIMARY KEY (dish_id, product_id),
            FOREIGN KEY (dish_id) REFERENCES Dishes(id),
            FOREIGN KEY (product_id) REFERENCES Products(id)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def fill_products_table():
    # Connect to SQLite database
    conn = sqlite3.connect('recipe_database.db')
    cursor = conn.cursor()

    # List of 100 different products to insert

    products = [
        ("1", "salt", "Salt.jpg", 0, 0, 0, 0, "g", "other"),
        ("2", "sugar", "Sugar.jpg", 387, 0, 0, 100, "g", "carb"),
        ("3", "olive oil", "Olive_oil.jpg", 884, 0, 100, 0, "ml", "fat"),
        ("4", "flour", "Flour.jpg", 364, 10, 1, 76, "g", "carb"),
        ("5", "butter", "Butter.jpg", 717, 0, 81, 1, "g", "fat"),
        ("6", "egg", "Egg.jpg", 155, 13, 11, 1, "unit", "protein"),
        ("7", "milk", "Milk.jpg", 42, 3, 1, 5, "ml", "carb"),
        ("8", "tomato", "Tomatoes.jpg", 18, 1, 0, 4, "g", "carb"),
        ("9", "onion", "Onions.jpg", 40, 1, 0, 9, "g", "carb"),
        ("10", "garlic", " Garlic.jpg", 149, 6, 0, 33, "g", "carb"),
        ("11", "chicken breast", "Chicken_breast.jpg", 165, 31, 3, 0, "g", "protein"),
        ("12", "beef", "Beef.jpg", 250, 26, 15, 0, "g", "protein"),
        ("13", "carrot", "Carrots.jpg", 41, 1, 0, 10, "g", "carb"),
        ("14", "potato", "Potato.jpg", 77, 2, 0, 17, "g", "carb"),
        ("15", "rice", "Rice.jpg", 130, 2, 0, 28, "g", "carb"),
        ("16", "pasta", "Pasta.jpg", 131, 5, 1, 25, "g", "carb"),
        ("17", "cheese", "Cheese.jpg", 402, 25, 33, 1, "g", "fat"),
        ("18", "yogurt", "Yogurt.jpg", 59, 10, 0, 4, "ml", "protein"),
        ("19", "spinach", "Spinach.jpg", 23, 3, 0, 4, "g", "carb"),
        ("20", "broccoli", "Broccoli.jpg", 34, 3, 0, 7, "g", "carb"),
        ("21", "apple", "Apples.jpg", 52, 0, 0, 14, "g", "carb"),
        ("22", "banana", "Banana.jpg", 96, 1, 0, 27, "g", "carb"),
        ("23", "strawberry", "Strawberry.jpg", 32, 1, 0, 8, "g", "carb"),
        ("24", "honey", "Honey.jpg", 304, 0, 0, 82, "g", "carb"),
        ("25", "baking powder", "Baking_powder.jpg", 53, 0, 0, 28, "g", "carb"),
        ("26", "baking soda", "Baking_soda.jpg", 0, 0, 0, 0, "g", "other"),
        ("27", "vanilla extract", "Vanilla_extract.jpg", 288, 0, 0, 13, "ml", "carb"),
        ("28", "cinnamon", "Cinnamon.jpg", 247, 4, 1, 81, "g", "carb"),
        ("29", "nutmeg", "Nutmeg.jpg", 525, 6, 36, 49, "g", "carb"),
        ("30", "lemon", "Lemon.jpg", 29, 1, 0, 9, "g", "carb"),
        ("31", "orange", "Orange.jpg", 47, 1, 0, 12, "g", "carb"),
        ("32", "cucumber", "Cucumber.jpg", 16, 1, 0, 4, "g", "carb"),
        ("33", "bell pepper", "Bell_pepper.jpg", 31, 1, 0, 6, "g", "carb"),
        ("34", "mushroom", "Mushroom.jpg", 22, 3, 0, 3, "g", "carb"),
        ("35", "zucchini", "Zucchini.jpg", 17, 1, 0, 3, "g", "carb"),
        ("36", "parsley", "parsley.jpg", 36, 3, 1, 6, "g", "carb"),
        ("37", "basil", "basil.jpg", 23, 3, 0, 2, "g", "protein"),
        ("38", "thyme", "thyme.jpg", 101, 6, 1, 24, "g", "carb"),
        ("39", "rosemary", "rosemary.jpg", 131, 3, 6, 21, "g", "carb"),
        ("40", "oregano", "oregano.jpg", 265, 9, 4, 69, "g", "carb"),
        ("41", "bay leaf", "bay_leaf.jpg", 313, 8, 8, 75, "g", "carb"),
        ("42", "mint", "mint.jpg", 44, 3, 1, 8, "g", "carb"),
        ("43", "celery", "celery.jpg", 16, 1, 0, 3, "g", "carb"),
        ("44", "lettuce", "lettuce.jpg", 15, 1, 0, 2, "g", "carb"),
        ("45", "kale", "kale.jpg", 49, 4, 1, 9, "g", "carb"),
        ("46", "cauliflower", "cauliflower.jpg", 25, 2, 0, 5, "g", "carb"),
        ("47", "cabbage", "cabbage.jpg", 25, 1, 0, 6, "g", "carb"),
        ("48", "peas", "peas.jpg", 81, 5, 0, 14, "g", "carb"),
        ("49", "green beans", "green_beans.jpg", 31, 2, 0, 7, "g", "carb"),
        ("50", "corn", "corn.jpg", 86, 3, 1, 19, "g", "carb"),
        ("51", "chickpeas", "chickpeas.jpg", 164, 9, 3, 27, "g", "carb"),
        ("52", "lentils", "lentils.jpg", 116, 9, 0, 20, "g", "carb"),
        ("53", "black beans", "black_beans.jpg", 132, 9, 0, 24, "g", "carb"),
        ("54", "kidney beans", "kidney_beans.jpg", 127, 9, 0, 22, "g", "carb"),
        ("55", "quinoa", "quinoa.jpg", 120, 4, 2, 21, "g", "carb"),
        ("56", "oats", "oats.jpg", 389, 17, 7, 66, "g", "carb"),
        ("57", "almonds", "almonds.jpg", 579, 21, 50, 22, "g", "fat"),
        ("58", "walnuts", "walnuts.jpg", 654, 15, 65, 14, "g", "fat"),
        ("59", "peanuts", "peanuts.jpg", 567, 26, 49, 16, "g", "fat"),
        ("60", "cashews", "cashews.jpg", 553, 18, 44, 30, "g", "fat"),
        ("61", "sunflower seeds", "sunflower_seeds.jpg", 584, 21, 51, 20, "g", "fat"),
        ("62", "pumpkin seeds", "pumpkin_seeds.jpg", 559, 30, 49, 11, "g", "fat"),
        ("63", "raisins", "raisins.jpg", 299, 3, 0, 79, "g", "carb"),
        ("64", "dates", "dates.jpg", 282, 2, 0, 75, "g", "carb"),
        ("65", "apricots", "apricots.jpg", 48, 1, 0, 11, "g", "carb"),
        ("66", "pineapple", "pineapple.jpg", 50, 0, 0, 13, "g", "carb"),
        ("67", "mango", "mango.jpg", 60, 1, 0, 15, "g", "carb"),
        ("68", "grapes", "grapes.jpg", 69, 0, 0, 18, "g", "carb"),
        ("69", "blueberries", "blueberries.jpg", 57, 0, 0, 14, "g", "carb"),
        ("70", "raspberries", "raspberries.jpg", 52, 1, 0, 12, "g", "carb"),
        ("71", "blackberries", "blackberries.jpg", 43, 1, 0, 10, "g", "carb"),
        ("72", "peach", "peach.jpg", 39, 1, 0, 10, "g", "carb"),
        ("73", "plum", "plum.jpg", 46, 0, 0, 11, "g", "carb"),
        ("74", "cherries", "cherries.jpg", 50, 1, 0, 12, "g", "carb"),
        ("75", "coconut", "coconut.jpg", 354, 3, 33, 15, "g", "fat"),
        ("76", "avocado", "avocado.jpg", 160, 2, 15, 9, "g", "fat"),
        ("77", "pomegranate", "pomegranate.jpg", 83, 1, 1, 19, "g", "carb"),
        ("78", "watermelon", "watermelon.jpg", 30, 1, 0, 8, "g", "carb"),
        ("79", "cantaloupe", "cantaloupe.jpg", 34, 1, 0, 8, "g", "carb"),
        ("80", "pear", "pear.jpg", 57, 0, 0, 15, "g", "carb"),
        ("81", "fig", "fig.jpg", 74, 1, 0, 19, "g", "carb"),
        ("82", "papaya", "papaya.jpg", 43, 0, 0, 11, "g", "carb"),
        ("83", "guava", "guava.jpg", 68, 2, 1, 14, "g", "carb"),
        ("84", "kiwi", "kiwi.jpg", 61, 1, 0, 15, "g", "carb"),
        ("85", "lime", "lime.jpg", 30, 0, 0, 10, "g", "carb"),
        ("86", "ginger", "ginger.jpg", 80, 2, 0, 18, "g", "carb"),
        ("87", "turmeric", "turmeric.jpg", 312, 7, 4, 67, "g", "carb"),
        ("88", "cloves", "cloves.jpg", 274, 6, 13, 65, "g", "carb"),
        ("89", "cardamom", "cardamom.jpg", 311, 11, 7, 68, "g", "carb"),
        ("90", "fennel", "fennel.jpg", 31, 1, 0, 7, "g", "carb"),
        ("91", "coriander", "coriander.jpg", 23, 2, 1, 3, "g", "carb"),
        ("92", "mustard seeds", "mustard_seeds.jpg", 508, 26, 36, 28, "g", "fat"),
        ("93", "poppy seeds", "poppy_seeds.jpg", 525, 18, 42, 28, "g", "fat"),
        ("94", "sesame seeds", "sesame_seeds.jpg", 573, 18, 50, 23, "g", "fat"),
        ("95", "saffron", "saffron.jpg", 310, 11, 6, 65, "g", "carb"),
        ("96", "almond milk", "almond_milk.jpg", 17, 0, 1, 1, "ml", "carb"),
        ("97", "coconut milk", "coconut_milk.jpg", 230, 2, 24, 6, "ml", "fat"),
        ("98", "soy sauce", "soy_sauce.jpg", 53, 8, 0, 5, "ml", "protein"),
        ("99", "apple cider vinegar", "apple_cider_vinegar.jpg", 21, 0, 0, 1, "ml", "carb"),
        ("100", "red wine vinegar", "red_wine_vinegar.jpg", 19, 0, 0, 0, "ml", "other"),
        ("101", "extra virgin olive oil", "extra_virgin_olive_oil.jpg", 884, 0, 100, 0, "ml", "fat"),
        ("102", "rye flour", "rye_flour.jpg", 357, 10, 1, 76, "g", "carb"),
        ("103", "spelt flour", "spelt_flour.jpg", 338, 14, 2, 70, "g", "carb"),
        ("104", "cocoa powder", "cocoa_powder.jpg", 228, 20, 13, 58, "g", "carb"),
        # (105) "egg" REMOVED - duplicate of (6) "egg"
        ("106", "maple syrup", "maple_syrup.jpg", 260, 0, 0, 67, "g", "carb"),
        ("107", "dark chocolate", "dark_chocolate.jpg", 598, 7, 42, 45, "g", "fat"),
        ("108", "sunflower oil", "sunflower_oil.jpg", 884, 0, 100, 0, "ml", "fat"),
        ("109", "black tea", "black_tea.jpg", 1, 0, 0, 0, "g", "other"),
        ("110", "malt extract", "malt_extract.jpg", 325, 5, 0, 69, "g", "carb"),
        ("111", "dark muscovado sugar", "dark_muscovado_sugar.jpg", 380, 0, 0, 95, "g", "carb"),
        ("112", "mixed dried fruit", "mixed_dried_fruit.jpg", 300, 2, 0, 75, "g", "carb"),
        ("113", "plain flour", "plain_flour.jpg", 364, 10, 1, 76, "g", "carb"),
        ("114", "bicarbonate of soda", "bicarbonate_of_soda.jpg", 0, 0, 0, 0, "g", "other"),
        ("115", "full-fat milk", "full-fat_milk.jpg", 61, 3, 3, 5, "ml", "carb"),
        ("116", "natural yogurt", "natural_yogurt.jpg", 59, 10, 0, 4, "ml", "protein"),
        ("117", "frozen fruits of the forest", "frozen_fruits_of_the_forest.jpg", 50, 1, 0, 12, "g", "carb"),
        ("118", "chia seeds", "chia_seeds.jpg", 486, 17, 31, 42, "g", "fat"),
        ("119", "goji berries", "goji_berries.jpg", 349, 14, 1, 77, "g", "carb"),
        ("120", "mixed seeds", "mixed_seeds.jpg", 570, 20, 47, 23, "g", "fat"),
        ("121", "soft dried apricots", "soft_dried_apricots.jpg", 241, 3, 0, 63, "g", "carb"),
        ("122", "soft dried dates", "soft_dried_dates.jpg", 282, 2, 0, 75, "g", "carb"),
        ("123", "dried cherries", "dried_cherries.jpg", 325, 2, 1, 78, "g", "carb"),
        ("124", "coconut oil", "coconut_oil.jpg", 862, 0, 100, 0, "ml", "fat"),
        ("125", "toasted sesame seeds", "toasted_sesame_seeds.jpg", 0, 0, 0, 0, "g", "other"),
        # update if you have data
        ("126", "shrimp", "shrimp.jpg", 99, 24, 0, 0, "g", "protein"),
        ("127", "lemon juice", "lemon_juice.jpg", 22, 1, 0, 7, "ml", "other"),
        ("128", "pepper", "pepper.jpg", 251, 10, 3, 64, "g", "other"),
        ("129", "romaine lettuce", "romaine_lettuce.jpg", 17, 1, 0, 3, "g", "carb"),
        ("130", "croutons", "croutons.jpg", 404, 12, 10, 71, "g", "carb"),
        ("131", "parmesan cheese", "parmesan_cheese.jpg", 431, 38, 29, 4, "g", "fat"),
        ("132", "caesar dressing", "caesar_dressing.jpg", 320, 3, 29, 7, "ml", "fat"),
        # (133) "bell peppers" REMOVED - duplicate of (33) "bell pepper"
        ("134", "ground beef", "ground_beef.jpg", 254, 17, 20, 0, "g", "protein"),
        ("135", "tomato sauce", "tomato_sauce.jpg", 74, 2, 0, 15, "g", "carb"),
        ("136", "brown sugar", "brown_sugar.jpg", 380, 0, 0, 98, "g", "carb"),
        ("137", "chocolate chips", "chocolate_chips.jpg", 502, 4, 25, 61, "g", "fat"),
        ("138", "potatoes", "potatoes.jpg", 77, 2, 0, 17, "g", "carb"),
        # (139) "carrot" REMOVED - duplicate of (13) "carrot"
        ("140", "curry paste", "curry_paste.jpg", 150, 3, 6, 20, "g", "other"),
        ("141", "salmon fillets", "salmon_fillets.jpg", 206, 22, 12, 0, "g", "protein"),
        ("142", "dill", "dill.jpg", 43, 3, 1, 7, "g", "other"),
        ("143", "cherry tomatoes", "cherry_tomatoes.jpg", 18, 1, 0, 3, "g", "carb"),
        ("144", "red onion", "red_onion.jpg", 37, 1, 0, 9, "g", "carb"),
        ("145", "garam masala", "garam_masala.jpg", 97, 4, 3, 15, "g", "other"),
        ("146", "cumin", "cumin.jpg", 375, 18, 22, 44, "g", "other"),
        ("147", "tomato puree", "tomato_puree.jpg", 82, 3, 1, 14, "g", "carb"),
        ("148", "cream", "cream.jpg", 340, 2, 36, 3, "ml", "fat"),
        ("149", "pizza dough", "pizza_dough.jpg", 266, 9, 3, 47, "g", "carb"),
        ("150", "mozzarella cheese", "mozzarella_cheese.jpg", 280, 28, 17, 3, "g", "fat"),
        ("151", "fresh basil", "fresh_basil.jpg", 23, 3, 0, 2, "g", "other"),
        ("152", "vegetable broth", "vegetable_broth.jpg", 15, 1, 0, 2, "ml", "other"),
        ("153", "tomato paste", "tomato_paste.jpg", 82, 3, 1, 14, "g", "carb"),
        ("154", "bread", "bread.jpg", 265, 9, 3, 49, "g", "carb"),
        ("155", "chili flakes", "chili_flakes.jpg", 314, 12, 14, 50, "g", "other"),
        ("156", "white fish fillets", "white_fish_fillets.jpg", 96, 20, 1, 0, "g", "protein"),
        ("157", "tortillas", "tortillas.jpg", 310, 8, 7, 50, "g", "carb"),
        ("158", "lime juice", "lime_juice.jpg", 25, 0, 0, 8, "ml", "other"),
        ("159", "mayonnaise", "mayonnaise.jpg", 680, 1, 75, 1, "g", "fat"),
        ("160", "chili powder", "chili_powder.jpg", 282, 14, 13, 31, "g", "other"),
        ("161", "feta cheese", "feta_cheese.jpg", 264, 14, 21, 4, "g", "fat"),
        ("162", "phyllo pastry", "phyllo_pastry.jpg", 310, 8, 3, 54, "g", "carb"),
        ("163", "snap peas", "snap_peas.jpg", 42, 3, 0, 7, "g", "carb"),
        ("164", "sesame oil", "sesame_oil.jpg", 884, 0, 100, 0, "ml", "fat"),
        ("165", "burger buns", "burger_buns.jpg", 250, 8, 3, 45, "g", "carb"),
        ("166", "ketchup", "ketchup.jpg", 112, 1, 0, 26, "g", "carb"),
        ("167", "mustard", "mustard.jpg", 66, 4, 4, 7, "g", "other"),
        ("168", "spaghetti", "spaghetti.jpg", 158, 6, 1, 31, "g", "carb"),
        ("169", "canned tomatoes", "canned_tomatoes.jpg", 18, 0, 0, 4, "g", "carb"),
        ("170", "ice cubes", "ice_cubes.jpg", 0, 0, 0, 0, "other", "other"),
        ("171", "beef strips", "beef_strips.jpg", 250, 26, 15, 0, "g", "protein"),
        # (172) "mushrooms" REMOVED - duplicate of (34) "mushroom"
        ("173", "sour cream", "sour_cream.jpg", 193, 2, 20, 4, "ml", "fat"),
        ("174", "beef broth", "beef_broth.jpg", 8, 1, 0, 1, "ml", "other"),
        ("175", "egg noodles", "egg_noodles.jpg", 138, 5, 2, 25, "g", "carb"),
        ("176", "greek yogurt", "greek_yogurt.jpg", 59, 10, 0, 4, "ml", "protein"),
        ("177", "granola", "granola.jpg", 489, 14, 20, 64, "g", "carb"),
        ("178", "berries", "berries.jpg", 57, 1, 0, 14, "g", "carb"),
        ("179", "self-raising flour", "self-raising_flour.jpg", 360, 10, 1, 75, "g", "carb"),
        ("180", "caster sugar", "caster_sugar.jpg", 387, 0, 0, 100, "g", "carb"),
        ("181", "lemon zest", "lemon_zest.jpg", 47, 1, 0, 16, "g", "other"),
        ("182", "icing sugar", "icing_sugar.jpg", 389, 0, 0, 100, "g", "carb")
    ]



    # Insert products into Products table
    cursor.executemany('''
        INSERT OR IGNORE INTO Products (id, name, image, calories, protein, fat, carbs, measurement, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', products)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
import sqlite3

def insert_recipes():
    conn = sqlite3.connect('recipe_database.db')
    cursor = conn.cursor()

    recipes = recipes = [
    {
        "id": "1",
        "name": "Dark Chocolate, Banana & Rye Loaf",
        "image": "dark_chocolate_banana_loaf.jpg",
        "description": "A rich and moist loaf with dark chocolate and banana.",
        "time_to_make": 70,
        "serves": 8,
        "difficulty": "Easy",
        "ingredients": {
            "extra virgin olive oil": "50ml",
            "rye flour": "100g",
            "spelt flour": "100g",
            "baking powder": "2 tsp",
            "cocoa powder": "25g",
            "egg": "2",
            "coconut milk": "150ml",
            "maple syrup": "100ml",
            "banana": "2 ripe",
            "dark chocolate": "50g, chopped",
        },
        "recipe": (
            "1. Heat oven to 180°C/160°C fan/gas 4. Grease and line a 900g loaf tin.\n"
            "2. Combine dry ingredients except chocolate. In another bowl, whisk wet ingredients and banana.\n"
            "3. Mix wet and dry ingredients, add chocolate, and pour into the tin.\n"
            "4. Bake for 50-55 minutes until a skewer comes out clean."
        ),
        "calories": 300,
        "protein": 5,
        "fat": 12,
        "carbs": 45,
    },
    {
        "id": "2",
        "name": "Malt Loaf",
        "image": "malt_loaf.jpg",
        "description": "A sticky, rich loaf perfect for tea time.",
        "time_to_make": 65,
        "serves": 20,
        "difficulty": "Easy",
        "ingredients": {
            "sunflower oil": "for greasing",
            "black tea": "250ml, hot",
            "malt extract": "100g",
            "dark muscovado sugar": "100g",
            "mixed dried fruit": "300g",
            "egg": "2",
            "plain flour": "250g",
            "baking powder": "2 tsp",
            "bicarbonate of soda": "1 tsp",
        },
        "recipe": (
            "1. Heat oven to 150°C/130°C fan/gas 2. Line two 450g loaf tins with parchment.\n"
            "2. Mix tea, malt, sugar, and fruit. Stir well, then add egg.\n"
            "3. Add flour, baking powder, and bicarbonate of soda. Pour into tins.\n"
            "4. Bake for 50 minutes until risen. Brush with malt and leave to cool."
        ),
        "calories": 220,
        "protein": 4,
        "fat": 5,
        "carbs": 40,
    },
    {
        "id": "3",
        "name": "Breakfast Super-Shake",
        "image": "breakfast_super_shake.jpeg",
        "description": "A quick and nutritious shake for busy mornings.",
        "time_to_make": 5,
        "serves": 1,
        "difficulty": "Easy",
        "ingredients": {
            "full-fat milk": "200ml",
            "natural yogurt": "100g",
            "banana": "1 ripe",
            "frozen fruits of the forest": "50g",
            "blueberries": "30g",
            "chia seeds": "1 tbsp",
            "cinnamon": "1/2 tsp",
            "goji berries": "1 tbsp",
            "mixed seeds": "1 tbsp",
            "honey": "1 tsp",
        },
        "recipe": (
            "1. Blend all ingredients until smooth.\n"
            "2. Pour into a glass and enjoy."
        ),
        "calories": 180,
        "protein": 6,
        "fat": 3,
        "carbs": 30,
    },
    {
        "id": "4",
        "name": "Energy Balls with Dates",
        "image": "energy_balls.jpg",
        "description": "Quick and healthy snacks for an energy boost.",
        "time_to_make": 10,
        "serves": 6,
        "difficulty": "Easy",
        "ingredients": {
            "soft dried apricots": "50g",
            "soft dried dates": "50g",
            "dried cherries": "30g",
            "coconut oil": "1 tbsp",
            "toasted sesame seeds": "2 tbsp",
        },
        "recipe": (
            "1. Blend apricots, dates, and cherries in a food processor until finely chopped.\n"
            "2. Add coconut oil, mix well, and shape into balls.\n"
            "3. Roll in sesame seeds and store in an airtight container."
        ),
        "calories": 120,
        "protein": 2,
        "fat": 4,
        "carbs": 20,
    },
    {
        "id": "5",
        "name": "Garlic Butter Shrimp",
        "image": "garlic_butter_shrimp.jpg",
        "description": "Juicy shrimp sautéed in garlic butter with a hint of lemon.",
        "time_to_make": 15,
        "serves": 4,
        "difficulty": "Easy",
        "ingredients": {
            "shrimp": "500g, peeled and deveined",
            "garlic": "4 cloves, minced",
            "butter": "50g",
            "lemon juice": "2 tbsp",
            "parsley": "2 tbsp, chopped",
            "salt": "to taste",
            "pepper": "to taste",
        },
        "recipe": (
            "1. Melt butter in a large skillet over medium heat.\n"
            "2. Add garlic and sauté until fragrant.\n"
            "3. Stir in shrimp and cook until pink and opaque, about 2-3 minutes per side.\n"
            "4. Drizzle with lemon juice, sprinkle with parsley, and serve hot."
        ),
        "calories": 250,
        "protein": 20,
        "fat": 15,
        "carbs": 5,
    },
        {
            "id": "6",
            "name": "Caesar Salad",
            "image": "caesar_salad.jpg",
            "description": "A classic Caesar salad with crisp lettuce and creamy dressing.",
            "time_to_make": 10,
            "serves": 2,
            "difficulty": "Easy",
            "ingredients": {
                "romaine lettuce": "1 large head, chopped",
                "croutons": "50g",
                "parmesan cheese": "30g, grated",
                "caesar dressing": "100ml",
                "chicken breast": "200g, grilled and sliced",
            },
            "recipe": (
                "1. Toss chopped romaine lettuce with caesar dressing in a large bowl.\n"
                "2. Add croutons and grated parmesan cheese. Toss to combine.\n"
                "3. Top with sliced grilled chicken if desired, and serve immediately."
            ),
            "calories": 220,
            "protein": 7,
            "fat": 14,
            "carbs": 15,
        },
        {
            "id": "7",
            "name": "Stuffed bell pepper",
            "image": "stuffed_bell_pepper.jpg",
            "description": "bell pepper filled with a savory mix of rice, beef, and vegetables.",
            "time_to_make": 60,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "bell pepper": "4 large, tops removed and seeds cleaned",
                "ground beef": "300g",
                "rice": "150g, cooked",
                "onion": "1, finely chopped",
                "garlic": "2 cloves, minced",
                "tomato sauce": "200ml",
                "cheese": "100g, grated",
                "salt": "to taste",
                "pepper": "to taste",
            },
            "recipe": (
                "1. Preheat oven to 375°F (190°C). Slice the tops off bell pepper and remove seeds.\n"
                "2. Cook ground beef with onion and garlic until browned. Add rice and tomato sauce, and season with salt and pepper.\n"
                "3. Fill peppers with the beef mixture and top with shredded cheese.\n"
                "4. Bake for 35-40 minutes until peppers are tender and cheese is melted."
            ),
            "calories": 350,
            "protein": 20,
            "fat": 12,
            "carbs": 40,
        },
        {
            "id": "8",
            "name": "Chocolate Chip Cookies",
            "image": "chocolate_chip_cookies.jpg",
            "description": "Classic cookies loaded with chocolate chips.",
            "time_to_make": 25,
            "serves": 24,
            "difficulty": "Easy",
            "ingredients": {
                "butter": "150g, softened",
                "sugar": "100g",
                "brown sugar": "100g",
                "egg": "2",
                "vanilla extract": "1 tsp",
                "flour": "300g",
                "baking soda": "1 tsp",
                "salt": "1/2 tsp",
                "chocolate chips": "200g",
            },
            "recipe": (
                "1. Preheat oven to 350°F (175°C). Line baking sheets with parchment paper.\n"
                "2. Cream butter, sugar, and brown sugar until fluffy. Beat in egg and vanilla extract.\n"
                "3. Mix in flour, baking soda, and salt. Fold in chocolate chips.\n"
                "4. Drop spoonfuls of dough onto baking sheets and bake for 10-12 minutes until golden."
            ),
            "calories": 150,
            "protein": 2,
            "fat": 7,
            "carbs": 20,
        },
        {
            "id": "9",
            "name": "Vegetable Curry",
            "image": "vegetable_curry.jpg",
            "description": "A flavorful and hearty vegetable curry with a creamy sauce.",
            "time_to_make": 40,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "potatoes": "200g, diced",
                "carrot": "150g, sliced",
                "peas": "100g",
                "cauliflower": "150g, florets",
                "coconut milk": "400ml",
                "curry paste": "2 tbsp",
                "onion": "1, chopped",
                "garlic": "2 cloves, minced",
                "ginger": "1 tbsp, minced",
            },
            "recipe": (
                "1. Heat oil in a large pot and sauté onion, garlic, and ginger until fragrant.\n"
                "2. Stir in curry paste and cook for 1-2 minutes.\n"
                "3. Add vegetables and coconut milk. Simmer for 20-25 minutes until tender.\n"
                "4. Serve hot with rice or naan."
            ),
            "calories": 320,
            "protein": 7,
            "fat": 15,
            "carbs": 35,
        },
        {
            "id": "10",
            "name": "Baked Salmon with Herbs",
            "image": "baked_salmon.jpg",
            "description": "Tender baked salmon topped with a mix of fresh herbs.",
            "time_to_make": 20,
            "serves": 2,
            "difficulty": "Easy",
            "ingredients": {
                "salmon fillets": "2 (200g each)",
                "olive oil": "2 tbsp",
                "lemon juice": "1 tbsp",
                "parsley": "1 tbsp, chopped",
                "dill": "1 tbsp, chopped",
                "garlic": "2 cloves, minced",
                "salt": "to taste",
                "pepper": "to taste",
            },
            "recipe": (
                "1. Preheat oven to 375°F (190°C). Line a baking sheet with foil.\n"
                "2. Place salmon on the baking sheet and drizzle with olive oil and lemon juice.\n"
                "3. Top with minced garlic, chopped parsley, and dill. Season with salt and pepper.\n"
                "4. Bake for 12-15 minutes until salmon flakes easily with a fork."
            ),
            "calories": 300,
            "protein": 25,
            "fat": 18,
            "carbs": 3,
        },
        {
            "id": "11",
            "name": "Quinoa Salad",
            "image": "quinoa_salad.jpg",
            "description": "A healthy and refreshing quinoa salad with fresh vegetables.",
            "time_to_make": 20,
            "serves": 2,
            "difficulty": "Easy",
            "ingredients": {
                "quinoa": "100g, cooked",
                "cucumber": "1, diced",
                "cherry tomatoes": "100g, halved",
                "red onion": "1 small, finely chopped",
                "parsley": "2 tbsp, chopped",
                "lemon juice": "2 tbsp",
                "olive oil": "1 tbsp",
                "salt": "to taste",
                "pepper": "to taste",
            },
            "recipe": (
                "1. Cook quinoa according to package instructions and let cool.\n"
                "2. In a bowl, combine chopped cucumber, cherry tomatoes, red onion, and parsley.\n"
                "3. Toss with cooled quinoa, olive oil, lemon juice, salt, and pepper.\n"
                "4. Serve immediately or chill for later."
            ),
            "calories": 250,
            "protein": 8,
            "fat": 8,
            "carbs": 35,
        },
        {
            "id": "12",
            "name": "Chicken Tikka Masala",
            "image": "chicken_tikka_masala.jpg",
            "description": "A creamy and flavorful Indian curry with marinated chicken.",
            "time_to_make": 60,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "chicken breast": "500g, cubed",
                "yogurt": "100g",
                "garam masala": "1 tsp",
                "turmeric": "1 tsp",
                "cumin": "1 tsp",
                "tomato puree": "200ml",
                "cream": "100ml",
                "garlic": "2 cloves, minced",
                "ginger": "1 tbsp, minced",
            },
            "recipe": (
                "1. Marinate chicken with yogurt, garlic, ginger, and spices for 30 minutes.\n"
                "2. Sear the marinated chicken in a hot skillet until browned and set aside.\n"
                "3. In the same skillet, cook garlic and ginger with spices. Add tomato puree and cream.\n"
                "4. Simmer the chicken in the sauce for 20 minutes. Serve with rice or naan."
            ),
            "calories": 400,
            "protein": 30,
            "fat": 18,
            "carbs": 20,
        },
        {
            "id": "13",
            "name": "Margherita Pizza",
            "image": "margherita_pizza.jpg",
            "description": "A simple and classic pizza with tomato sauce, mozzarella, and basil.",
            "time_to_make": 30,
            "serves": 2,
            "difficulty": "Easy",
            "ingredients": {
                "pizza dough": "250g",
                "tomato sauce": "100ml",
                "mozzarella cheese": "150g, sliced",
                "fresh basil": "5-6 leaves",
                "olive oil": "1 tbsp",
                "salt": "to taste",
            },
            "recipe": (
                "1. Preheat oven to 220°C (425°F). Roll out pizza dough and place on a baking tray.\n"
                "2. Spread tomato sauce over the dough, leaving a border around the edges.\n"
                "3. Top with sliced mozzarella and drizzle with olive oil.\n"
                "4. Bake for 10-12 minutes. Garnish with fresh basil before serving."
            ),
            "calories": 300,
            "protein": 12,
            "fat": 10,
            "carbs": 40,
        },
        {
            "id": "14",
            "name": "Lentil Soup",
            "image": "lentil_soup.jpg",
            "description": "A hearty and nutritious lentil soup with vegetables.",
            "time_to_make": 40,
            "serves": 4,
            "difficulty": "Easy",
            "ingredients": {
                "lentils": "200g, rinsed",
                "carrot": "2, diced",
                "celery": "2 stalks, diced",
                "onion": "1, chopped",
                "garlic": "2 cloves, minced",
                "vegetable broth": "1 liter",
                "tomato paste": "2 tbsp",
                "olive oil": "2 tbsp",
                "cumin": "1 tsp",
            },
            "recipe": (
                "1. Heat olive oil in a pot and sauté onion, garlic, carrot, and celery until softened.\n"
                "2. Add lentils, vegetable broth, tomato paste, and cumin.\n"
                "3. Simmer for 25-30 minutes until lentils are tender.\n"
                "4. Serve hot with crusty bread."
            ),
            "calories": 250,
            "protein": 12,
            "fat": 5,
            "carbs": 35,
        },
        {
            "id": "15",
            "name": "Avocado Toast",
            "image": "avocado_toast.jpg",
            "description": "A quick and delicious breakfast option with creamy avocado.",
            "time_to_make": 5,
            "serves": 1,
            "difficulty": "Easy",
            "ingredients": {
                "bread": "2 slices",
                "avocado": "1 ripe, mashed",
                "lemon juice": "1 tsp",
                "chili flakes": "1/2 tsp",
                "salt": "to taste",
                "pepper": "to taste",
            },
            "recipe": (
                "1. Toast the bread slices until golden.\n"
                "2. Mash avocado with lemon juice, salt, and pepper.\n"
                "3. Spread avocado mixture on the toast and sprinkle with chili flakes.\n"
                "4. Serve immediately."
            ),
            "calories": 200,
            "protein": 5,
            "fat": 12,
            "carbs": 20,
        },
        {
            "id": "16",
            "name": "Fish Tacos",
            "image": "fish_tacos.jpg",
            "description": "Crispy fish tacos with a tangy slaw and creamy sauce.",
            "time_to_make": 30,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "white fish fillets": "400g",
                "tortillas": "8 small",
                "cabbage": "200g, shredded",
                "lime juice": "2 tbsp",
                "mayonnaise": "2 tbsp",
                "chili powder": "1 tsp",
                "salt": "to taste",
                "pepper": "to taste",
            },
            "recipe": (
                "1. Season fish with salt, pepper, and chili powder. Cook in a skillet until flaky.\n"
                "2. Prepare slaw by mixing shredded cabbage with lime juice and mayonnaise.\n"
                "3. Warm tortillas and fill with fish and slaw.\n"
                "4. Serve with extra lime wedges and hot sauce."
            ),
            "calories": 300,
            "protein": 20,
            "fat": 10,
            "carbs": 30,
        },
        {
            "id": "17",
            "name": "Spinach & Feta Pie",
            "image": "spinach_feta_pie.jpg",
            "description": "A savory Greek-inspired pie with spinach and feta cheese.",
            "time_to_make": 50,
            "serves": 6,
            "difficulty": "Medium",
            "ingredients": {
                "spinach": "300g, fresh",
                "feta cheese": "200g, crumbled",
                "phyllo pastry": "6 sheets",
                "onion": "1, finely chopped",
                "garlic": "2 cloves, minced",
                "olive oil": "3 tbsp",
                "egg": "2",
                "nutmeg": "1/4 tsp",
            },
            "recipe": (
                "1. Preheat oven to 180°C (350°F). Sauté onion and garlic in olive oil until softened.\n"
                "2. Add spinach and cook until wilted. Stir in crumbled feta, egg, and nutmeg.\n"
                "3. Layer phyllo pastry in a baking dish, brushing each layer with olive oil.\n"
                "4. Add spinach mixture and top with more pastry layers. Bake for 30-35 minutes."
            ),
            "calories": 280,
            "protein": 10,
            "fat": 18,
            "carbs": 20,
        },
        {
            "id": "18",
            "name": "Vegetable Stir-Fry",
            "image": "vegetable_stir_fry.jpg",
            "description": "A colorful and healthy stir-fry with mixed vegetables.",
            "time_to_make": 20,
            "serves": 2,
            "difficulty": "Easy",
            "ingredients": {
                "broccoli": "100g, florets",
                "bell pepper": "2, sliced",
                "carrot": "100g, julienned",
                "snap peas": "100g",
                "soy sauce": "2 tbsp",
                "garlic": "2 cloves, minced",
                "ginger": "1 tbsp, minced",
                "sesame oil": "1 tbsp",
            },
            "recipe": (
                "1. Heat sesame oil in a large skillet or wok.\n"
                "2. Add garlic and ginger, stir-fry until fragrant.\n"
                "3. Add vegetables and cook until tender but crisp.\n"
                "4. Drizzle with soy sauce and serve hot."
            ),
            "calories": 200,
            "protein": 5,
            "fat": 8,
            "carbs": 28,
        },
        {
            "id": "19",
            "name": "Classic Pancakes",
            "image": "classic_pancakes.jpg",
            "description": "Fluffy pancakes perfect for a weekend breakfast.",
            "time_to_make": 15,
            "serves": 4,
            "difficulty": "Easy",
            "ingredients": {
                "flour": "200g",
                "sugar": "50g",
                "baking powder": "2 tsp",
                "milk": "250ml",
                "egg": "2",
                "butter": "30g, melted",
                "vanilla extract": "1 tsp",
            },
            "recipe": (
                "1. Mix flour, sugar, and baking powder in a bowl.\n"
                "2. Whisk milk, egg, and vanilla extract in another bowl.\n"
                "3. Combine wet and dry ingredients, then stir in melted butter.\n"
                "4. Heat a pan and cook pancakes until bubbles form, then flip. Serve warm."
            ),
            "calories": 250,
            "protein": 6,
            "fat": 10,
            "carbs": 30,
        },
        {
            "id": "20",
            "name": "Classic Beef Burger",
            "image": "classic_beef_burger.jpg",
            "description": "A juicy beef burger with all the classic toppings.",
            "time_to_make": 25,
            "serves": 4,
            "difficulty": "Easy",
            "ingredients": {
                "ground beef": "500g",
                "burger buns": "4",
                "lettuce": "4 leaves",
                "tomato": "1 large, sliced",
                "cheese": "4 slices",
                "ketchup": "4 tbsp",
                "mustard": "2 tbsp",
            },
            "recipe": (
                "1. Shape ground beef into patties and season with salt and pepper.\n"
                "2. Grill or pan-fry patties until cooked to your liking.\n"
                "3. Toast burger buns and assemble with lettuce, tomato, cheese, and sauces.\n"
                "4. Serve hot with fries or salad."
            ),
            "calories": 500,
            "protein": 25,
            "fat": 20,
            "carbs": 45,
        },
        {
            "id": "21",
            "name": "Spaghetti Bolognese",
            "image": "spaghetti_bolognese.jpg",
            "description": "A hearty Italian classic with rich meat sauce.",
            "time_to_make": 60,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "spaghetti": "300g",
                "ground beef": "300g",
                "onion": "1, chopped",
                "garlic": "2 cloves, minced",
                "tomato paste": "2 tbsp",
                "canned tomatoes": "400g",
                "olive oil": "2 tbsp",
                "parmesan cheese": "50g, grated",
                "basil": "1 tbsp, chopped",
            },
            "recipe": (
                "1. Heat olive oil in a pan. Sauté onion and garlic until translucent.\n"
                "2. Add ground beef and cook until browned.\n"
                "3. Stir in tomato paste and canned tomatoes. Simmer for 30 minutes.\n"
                "4. Cook spaghetti according to package instructions. Toss with the sauce and serve with parmesan."
            ),
            "calories": 450,
            "protein": 20,
            "fat": 12,
            "carbs": 60,
        },
        {
            "id": "22",
            "name": "Vegetarian Chili",
            "image": "vegetarian_chili.jpg",
            "description": "A comforting and flavorful vegetarian chili.",
            "time_to_make": 45,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "kidney beans": "400g, canned, drained",
                "black beans": "400g, canned, drained",
                "bell pepper": "2, diced",
                "onion": "1, chopped",
                "garlic": "3 cloves, minced",
                "tomato paste": "2 tbsp",
                "canned tomatoes": "400g",
                "chili powder": "1 tbsp",
                "cumin": "1 tsp",
                "olive oil": "2 tbsp",
            },
            "recipe": (
                "1. Heat olive oil in a pot and sauté onion and garlic until soft.\n"
                "2. Add bell pepper, chili powder, and cumin. Cook for 5 minutes.\n"
                "3. Stir in beans, tomato paste, and canned tomatoes. Simmer for 30 minutes.\n"
                "4. Serve hot with rice, tortilla chips, or bread."
            ),
            "calories": 300,
            "protein": 12,
            "fat": 8,
            "carbs": 40,
        },
        {
            "id": "23",
            "name": "Banana Smoothie",
            "image": "banana_smoothie.jpg",
            "description": "A creamy and refreshing banana smoothie.",
            "time_to_make": 5,
            "serves": 2,
            "difficulty": "Easy",
            "ingredients": {
                "banana": "2, ripe",
                "milk": "300ml",
                "yogurt": "150g",
                "honey": "2 tsp",
                "ice cubes": "4",
            },
            "recipe": (
                "1. Combine banana, milk, yogurt, and honey in a blender.\n"
                "2. Add ice cubes and blend until smooth.\n"
                "3. Pour into glasses and serve immediately."
            ),
            "calories": 150,
            "protein": 6,
            "fat": 3,
            "carbs": 28,
        },
        {
            "id": "24",
            "name": "Beef Stroganoff",
            "image": "beef_stroganoff.jpg",
            "description": "A rich and creamy beef stroganoff served with noodles.",
            "time_to_make": 40,
            "serves": 4,
            "difficulty": "Medium",
            "ingredients": {
                "beef strips": "500g",
                "mushroom": "200g, sliced",
                "onion": "1, chopped",
                "garlic": "2 cloves, minced",
                "sour cream": "150ml",
                "beef broth": "200ml",
                "butter": "2 tbsp",
                "flour": "2 tbsp",
                "egg noodles": "300g",
            },
            "recipe": (
                "1. Heat butter in a skillet and sauté onions, garlic, and mushroom until softened.\n"
                "2. Add beef strips and cook until browned.\n"
                "3. Stir in flour and beef broth. Simmer for 10-15 minutes until thickened.\n"
                "4. Mix in sour cream and serve over cooked egg noodles."
            ),
            "calories": 450,
            "protein": 25,
            "fat": 18,
            "carbs": 45,
        },
        {
            "id": "25",
            "name": "Greek Yogurt Parfait",
            "image": "greek_yogurt_parfait.jpg",
            "description": "A healthy and delicious parfait with layers of yogurt, granola, and fruit.",
            "time_to_make": 5,
            "serves": 1,
            "difficulty": "Easy",
            "ingredients": {
                "greek yogurt": "200g",
                "granola": "50g",
                "berries": "100g",
                "honey": "1 tsp",
            },
            "recipe": (
                "1. Layer Greek yogurt, granola, and berries in a glass.\n"
                "2. Drizzle with honey and serve immediately."
            ),
            "calories": 200,
            "protein": 10,
            "fat": 5,
            "carbs": 30,
        },
        {
            "id": "26",
            "name": "Tomato Basil Pasta",
            "image": "tomato_basil_pasta.jpg",
            "description": "A quick and flavorful pasta dish with fresh tomatoes and basil.",
            "time_to_make": 25,
            "serves": 4,
            "difficulty": "Easy",
            "ingredients": {
                "pasta": "400g",
                "cherry tomatoes": "300g, halved",
                "garlic": "3 cloves, minced",
                "olive oil": "3 tbsp",
                "fresh basil": "10 leaves, chopped",
                "parmesan cheese": "50g, grated",
                "salt": "to taste",
                "pepper": "to taste",
            },
            "recipe": (
                "1. Cook pasta according to package instructions. Reserve 1/2 cup pasta water.\n"
                "2. Heat olive oil in a pan. Add garlic and cook until fragrant. Add tomatoes and cook until softened.\n"
                "3. Toss pasta with the tomato mixture. Add reserved pasta water if needed.\n"
                "4. Season with salt and pepper. Top with fresh basil and parmesan cheese."
            ),
            "calories": 400,
            "protein": 12,
            "fat": 10,
            "carbs": 60,
        },


        {
            "id": "27",
            "name": "Lemon Drizzle Cake",
            "image": "lemon_drizzle_cake.jpg",
            "description": "A zesty, moist cake perfect for afternoon tea.",
            "time_to_make": 50,
            "serves": 12,
            "difficulty": "Medium",
            "ingredients": {
                "self-raising flour": "200g",
                "caster sugar": "200g",
                "butter": "200g, softened",
                "egg": "4",
                "lemon zest": "2 tbsp",
                "lemon juice": "50ml",
                "icing sugar": "100g",
            },
            "recipe": (
                "1. Heat oven to 180°C/160°C fan/gas 4. Grease and line a 20cm round cake tin.\n"
                "2. Mix flour, sugar, egg, and butter until smooth. Add lemon zest and juice.\n"
                "3. Pour into the tin and bake for 35-40 minutes until a skewer comes out clean.\n"
                "4. Mix icing sugar with lemon juice to make a glaze. Pour over the warm cake."
            ),
            "calories": 270,
            "protein": 4,
            "fat": 12,
            "carbs": 38,
        },
    ]

    for recipe in recipes:
        # Insert dish data into the Dishes table
        cursor.execute('''
            INSERT OR IGNORE INTO Dishes (
                id, name, image, description, time_to_make, serves, difficulty,
                recipe, calories, protein, fat, carbs
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            recipe["id"], recipe["name"], recipe["image"], recipe["description"],
            recipe["time_to_make"], recipe["serves"], recipe["difficulty"],
            recipe["recipe"], recipe["calories"], recipe["protein"],
            recipe["fat"], recipe["carbs"]
        ))

        # Map ingredients to products
        for ingredient, quantity in recipe["ingredients"].items():
            # Find the product ID by ingredient name
            cursor.execute('''
                SELECT id FROM Products WHERE name = ?
            ''', (ingredient,))
            product_id = cursor.fetchone()

            # If the product exists, link it to the dish
            if product_id:
                cursor.execute('''
                    INSERT OR IGNORE INTO DishProduct (
                        dish_id, product_id, quantity
                    ) VALUES (?, ?, ?)
                ''', (recipe["id"], product_id[0], quantity))
            else:
                print(f"Warning: Ingredient '{ingredient}' not found in Products table.")

    conn.commit()
    conn.close()



if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")
    fill_products_table()
    print("Products table filled with a wider range of 100 different products.")
    insert_recipes()
    print("Recipes inserted successfully.")
