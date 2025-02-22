import sqlite3

from database.recipes import recipes


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
            carbs INTEGER,
            meal_type TEXT
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



    for recipe in recipes:
        # Insert dish data into the Dishes table
        cursor.execute('''
            INSERT OR IGNORE INTO Dishes (
                id, name, image, description, time_to_make, serves, difficulty,
                recipe, calories, protein, fat, carbs, meal_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            recipe["id"], recipe["name"], recipe["image"], recipe["description"],
            recipe["time_to_make"], recipe["serves"], recipe["difficulty"],
            recipe["recipe"], recipe["calories"], recipe["protein"],
            recipe["fat"], recipe["carbs"], recipe["meal_type"]
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
