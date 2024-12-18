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
            ingredients TEXT,
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
            variable INTEGER,
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
    ("1", "Salt", "Salt.jpg", 0, 0, 0, 0, "g", "Other"),
    ("2", "Sugar", "Sugar.jpg", 387, 0, 0, 100, "g", "Carb"),
    ("3", "Olive Oil", "Olive Oil.jpg", 884, 0, 100, 0, "ml", "Fat"),
    ("4", "Flour", "Flour.jpg", 364, 10, 1, 76, "g", "Carb"),
    ("5", "Butter", "Butter.jpg", 717, 0, 81, 1, "g", "Fat"),
    ("6", "Egg", "Egg.jpg", 155, 13, 11, 1, "unit", "Protein"),
    ("7", "Milk", "Milk.jpg", 42, 3, 1, 5, "ml", "Carb"),
    ("8", "Tomato", "Tomatoes.jpg", 18, 1, 0, 4, "g", "Carb"),
    ("9", "Onion", "Onions.jpg", 40, 1, 0, 9, "g", "Carb"),
    ("10", "Garlic", "Garlic.jpg", 149, 6, 0, 33, "g", "Carb"),
    ("11", "Chicken Breast", "Chicken Breast.jpg", 165, 31, 3, 0, "g", "Protein"),
    ("12", "Beef", "Beef.jpg", 250, 26, 15, 0, "g", "Protein"),
    ("13", "Carrot", "Carrots.jpg", 41, 1, 0, 10, "g", "Carb"),
    ("14", "Potato", "Potato.jpg", 77, 2, 0, 17, "g", "Carb"),
    ("15", "Rice", "Rice.jpg", 130, 2, 0, 28, "g", "Carb"),
    ("16", "Pasta", "Pasta.jpg", 131, 5, 1, 25, "g", "Carb"),
    ("17", "Cheese", "Cheese.jpg", 402, 25, 33, 1, "g", "Fat"),
    ("18", "Yogurt", "Yogurt.jpg", 59, 10, 0, 4, "ml", "Protein"),
    ("19", "Spinach", "Spinach.jpg", 23, 3, 0, 4, "g", "Carb"),
    ("20", "Broccoli", "Broccoli.jpg", 34, 3, 0, 7, "g", "Carb"),
    ("21", "Apple", "Apples.jpg", 52, 0, 0, 14, "g", "Carb"),
    ("22", "Banana", "Banana.jpg", 96, 1, 0, 27, "g", "Carb"),
    ("23", "Strawberry", "Strawberry.jpg", 32, 1, 0, 8, "g", "Carb"),
    ("24", "Honey", "Honey.jpg", 304, 0, 0, 82, "g", "Carb"),
    ("25", "Baking Powder", "Baking Powder.jpg", 53, 0, 0, 28, "g", "Carb"),
    ("26", "Baking Soda", "Baking Soda.jpg", 0, 0, 0, 0, "g", "Other"),
    ("27", "Vanilla Extract", "Vanilla Extract.jpg", 288, 0, 0, 13, "ml", "Carb"),
    ("28", "Cinnamon", "Cinnamon.jpg", 247, 4, 1, 81, "g", "Carb"),
    ("29", "Nutmeg", "Nutmeg.jpg", 525, 6, 36, 49, "g", "Carb"),
    ("30", "Lemon", "Lemon.jpg", 29, 1, 0, 9, "g", "Carb"),
    ("31", "Orange", "Orange.jpg", 47, 1, 0, 12, "g", "Carb"),
    ("32", "Cucumber", "Cucumber.jpg", 16, 1, 0, 4, "g", "Carb"),
    ("33", "Bell Pepper", "Bell Pepper.jpg", 31, 1, 0, 6, "g", "Carb"),
    ("34", "Mushroom", "Mushroom.jpg", 22, 3, 0, 3, "g", "Carb"),
    ("35", "Zucchini", "Zucchini.jpg", 17, 1, 0, 3, "g", "Carb"),
    ("36", "Parsley", "Parsley.jpg", 36, 3, 1, 6, "g", "Carb"),
    ("37", "Basil", "Basil.jpg", 23, 3, 0, 2, "g", "Protein"),
    ("38", "Thyme", "Thyme.jpg", 101, 6, 1, 24, "g", "Carb"),
    ("39", "Rosemary", "Rosemary.jpg", 131, 3, 6, 21, "g", "Carb"),
    ("40", "Oregano", "Oregano.jpg", 265, 9, 4, 69, "g", "Carb"),
    ("41", "Bay Leaf", "Bay Leaf.jpg", 313, 8, 8, 75, "g", "Carb"),
    ("42", "Mint", "Mint.jpg", 44, 3, 1, 8, "g", "Carb"),
    ("43", "Celery", "Celery.jpg", 16, 1, 0, 3, "g", "Carb"),
    ("44", "Lettuce", "Lettuce.jpg", 15, 1, 0, 2, "g", "Carb"),
    ("45", "Kale", "Kale.jpg", 49, 4, 1, 9, "g", "Carb"),
    ("46", "Cauliflower", "Cauliflower.jpg", 25, 2, 0, 5, "g", "Carb"),
    ("47", "Cabbage", "Cabbage.jpg", 25, 1, 0, 6, "g", "Carb"),
    ("48", "Peas", "Peas.jpg", 81, 5, 0, 14, "g", "Carb"),
    ("49", "Green Beans", "Green Beans.jpg", 31, 2, 0, 7, "g", "Carb"),
    ("50", "Corn", "Corn.jpg", 86, 3, 1, 19, "g", "Carb"),
    ("51", "Chickpeas", "Chickpeas.jpg", 164, 9, 3, 27, "g", "Carb"),
    ("52", "Lentils", "Lentils.jpg", 116, 9, 0, 20, "g", "Carb"),
    ("53", "Black Beans", "Black Beans.jpg", 132, 9, 0, 24, "g", "Carb"),
    ("54", "Kidney Beans", "Kidney Beans.jpg", 127, 9, 0, 22, "g", "Carb"),
    ("55", "Quinoa", "Quinoa.jpg", 120, 4, 2, 21, "g", "Carb"),
    ("56", "Oats", "Oats.jpg", 389, 17, 7, 66, "g", "Carb"),
    ("57", "Almonds", "Almonds.jpg", 579, 21, 50, 22, "g", "Fat"),
    ("58", "Walnuts", "Walnuts.jpg", 654, 15, 65, 14, "g", "Fat"),
    ("59", "Peanuts", "Peanuts.jpg", 567, 26, 49, 16, "g", "Fat"),
    ("60", "Cashews", "Cashews.jpg", 553, 18, 44, 30, "g", "Fat"),
    ("61", "Sunflower Seeds", "Sunflower Seeds.jpg", 584, 21, 51, 20, "g", "Fat"),
    ("62", "Pumpkin Seeds", "Pumpkin Seeds.jpg", 559, 30, 49, 11, "g", "Fat"),
    ("63", "Raisins", "Raisins.jpg", 299, 3, 0, 79, "g", "Carb"),
    ("64", "Dates", "Dates.jpg", 282, 2, 0, 75, "g", "Carb"),
    ("65", "Apricots", "Apricots.jpg", 48, 1, 0, 11, "g", "Carb"),
    ("66", "Pineapple", "Pineapple.jpg", 50, 0, 0, 13, "g", "Carb"),
    ("67", "Mango", "Mango.jpg", 60, 1, 0, 15, "g", "Carb"),
    ("68", "Grapes", "Grapes.jpg", 69, 0, 0, 18, "g", "Carb"),
    ("69", "Blueberries", "Blueberries.jpg", 57, 0, 0, 14, "g", "Carb"),
    ("70", "Raspberries", "Raspberries.jpg", 52, 1, 0, 12, "g", "Carb"),
    ("71", "Blackberries", "Blackberries.jpg", 43, 1, 0, 10, "g", "Carb"),
    ("72", "Peach", "Peach.jpg", 39, 1, 0, 10, "g", "Carb"),
    ("73", "Plum", "Plum.jpg", 46, 0, 0, 11, "g", "Carb"),
    ("74", "Cherries", "Cherries.jpg", 50, 1, 0, 12, "g", "Carb"),
    ("75", "Coconut", "Coconut.jpg", 354, 3, 33, 15, "g", "Fat"),
    ("76", "Avocado", "Avocado.jpg", 160, 2, 15, 9, "g", "Fat"),
    ("77", "Pomegranate", "Pomegranate.jpg", 83, 1, 1, 19, "g", "Carb"),
    ("78", "Watermelon", "Watermelon.jpg", 30, 1, 0, 8, "g", "Carb"),
    ("79", "Cantaloupe", "Cantaloupe.jpg", 34, 1, 0, 8, "g", "Carb"),
    ("80", "Pear", "Pear.jpg", 57, 0, 0, 15, "g", "Carb"),
    ("81", "Fig", "Fig.jpg", 74, 1, 0, 19, "g", "Carb"),
    ("82", "Papaya", "Papaya.jpg", 43, 0, 0, 11, "g", "Carb"),
    ("83", "Guava", "Guava.jpg", 68, 2, 1, 14, "g", "Carb"),
    ("84", "Kiwi", "Kiwi.jpg", 61, 1, 0, 15, "g", "Carb"),
    ("85", "Lime", "Lime.jpg", 30, 0, 0, 10, "g", "Carb"),
    ("86", "Ginger", "Ginger.jpg", 80, 2, 0, 18, "g", "Carb"),
    ("87", "Turmeric", "Turmeric.jpg", 312, 7, 4, 67, "g", "Carb"),
    ("88", "Cloves", "Cloves.jpg", 274, 6, 13, 65, "g", "Carb"),
    ("89", "Cardamom", "Cardamom.jpg", 311, 11, 7, 68, "g", "Carb"),
    ("90", "Fennel", "Fennel.jpg", 31, 1, 0, 7, "g", "Carb"),
    ("91", "Coriander", "Coriander.jpg", 23, 2, 1, 3, "g", "Carb"),
    ("92", "Mustard Seeds", "Mustard Seeds.jpg", 508, 26, 36, 28, "g", "Fat"),
    ("93", "Poppy Seeds", "Poppy Seeds.jpg", 525, 18, 42, 28, "g", "Fat"),
    ("94", "Sesame Seeds", "Sesame Seeds.jpg", 573, 18, 50, 23, "g", "Fat"),
    ("95", "Saffron", "Saffron.jpg", 310, 11, 6, 65, "g", "Carb"),
    ("96", "Almond Milk", "Almond Milk.jpg", 17, 0, 1, 1, "ml", "Carb"),
    ("97", "Coconut Milk", "Coconut Milk.jpg", 230, 2, 24, 6, "ml", "Fat"),
    ("98", "Soy Sauce", "Soy Sauce.jpg", 53, 8, 0, 5, "ml", "Protein"),
    ("99", "Apple Cider Vinegar", "Apple Cider Vinegar.jpg", 21, 0, 0, 1, "ml", "Carb"),
    ("100", "Red Wine Vinegar", "Red Wine Vinegar.jpg", 19, 0, 0, 0, "ml", "Other")
]



    # Insert products into Products table
    cursor.executemany('''
        INSERT OR IGNORE INTO Products (id, name, image, calories, protein, fat, carbs, measurement, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', products)

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")
    fill_products_table()
    print("Products table filled with a wider range of 100 different products.")
