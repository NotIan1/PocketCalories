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
            measurement TEXT
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
        ("1", "Salt", "", 0, 0, 0, 0, "g"),
        ("2", "Sugar", "", 387, 0, 0, 100, "g"),
        ("3", "Olive Oil", "", 884, 0, 100, 0, "ml"),
        ("4", "Flour", "", 364, 10, 1, 76, "g"),
        ("5", "Butter", "", 717, 0, 81, 1, "g"),
        ("6", "Egg", "", 155, 13, 11, 1, "unit"),
        ("7", "Milk", "", 42, 3, 1, 5, "ml"),
        ("8", "Tomato", "", 18, 1, 0, 4, "g"),
        ("9", "Onion", "", 40, 1, 0, 9, "g"),
        ("10", "Garlic", "", 149, 6, 0, 33, "g"),
        ("11", "Chicken Breast", "", 165, 31, 3, 0, "g"),
        ("12", "Beef", "", 250, 26, 15, 0, "g"),
        ("13", "Carrot", "", 41, 1, 0, 10, "g"),
        ("14", "Potato", "", 77, 2, 0, 17, "g"),
        ("15", "Rice", "", 130, 2, 0, 28, "g"),
        ("16", "Pasta", "", 131, 5, 1, 25, "g"),
        ("17", "Cheese", "", 402, 25, 33, 1, "g"),
        ("18", "Yogurt", "", 59, 10, 0, 4, "ml"),
        ("19", "Spinach", "", 23, 3, 0, 4, "g"),
        ("20", "Broccoli", "", 34, 3, 0, 7, "g"),
        ("21", "Apple", "", 52, 0, 0, 14, "g"),
        ("22", "Banana", "", 96, 1, 0, 27, "g"),
        ("23", "Strawberry", "", 32, 1, 0, 8, "g"),
        ("24", "Honey", "", 304, 0, 0, 82, "g"),
        ("25", "Baking Powder", "", 53, 0, 0, 28, "g"),
        ("26", "Baking Soda", "", 0, 0, 0, 0, "g"),
        ("27", "Vanilla Extract", "", 288, 0, 0, 13, "ml"),
        ("28", "Cinnamon", "", 247, 4, 1, 81, "g"),
        ("29", "Nutmeg", "", 525, 6, 36, 49, "g"),
        ("30", "Lemon", "", 29, 1, 0, 9, "g"),
        ("31", "Orange", "", 47, 1, 0, 12, "g"),
        ("32", "Cucumber", "", 16, 1, 0, 4, "g"),
        ("33", "Bell Pepper", "", 31, 1, 0, 6, "g"),
        ("34", "Mushroom", "", 22, 3, 0, 3, "g"),
        ("35", "Zucchini", "", 17, 1, 0, 3, "g"),
        ("36", "Parsley", "", 36, 3, 1, 6, "g"),
        ("37", "Basil", "", 23, 3, 0, 2, "g"),
        ("38", "Thyme", "", 101, 6, 1, 24, "g"),
        ("39", "Rosemary", "", 131, 3, 6, 21, "g"),
        ("40", "Oregano", "", 265, 9, 4, 69, "g"),
        ("41", "Bay Leaf", "", 313, 8, 8, 75, "g"),
        ("42", "Mint", "", 44, 3, 1, 8, "g"),
        ("43", "Celery", "", 16, 1, 0, 3, "g"),
        ("44", "Lettuce", "", 15, 1, 0, 2, "g"),
        ("45", "Kale", "", 49, 4, 1, 9, "g"),
        ("46", "Cauliflower", "", 25, 2, 0, 5, "g"),
        ("47", "Cabbage", "", 25, 1, 0, 6, "g"),
        ("48", "Peas", "", 81, 5, 0, 14, "g"),
        ("49", "Green Beans", "", 31, 2, 0, 7, "g"),
        ("50", "Corn", "", 86, 3, 1, 19, "g"),
        ("51", "Chickpeas", "", 164, 9, 3, 27, "g"),
        ("52", "Lentils", "", 116, 9, 0, 20, "g"),
        ("53", "Black Beans", "", 132, 9, 0, 24, "g"),
        ("54", "Kidney Beans", "", 127, 9, 0, 22, "g"),
        ("55", "Quinoa", "", 120, 4, 2, 21, "g"),
        ("56", "Oats", "", 389, 17, 7, 66, "g"),
        ("57", "Almonds", "", 579, 21, 50, 22, "g"),
        ("58", "Walnuts", "", 654, 15, 65, 14, "g"),
        ("59", "Peanuts", "", 567, 26, 49, 16, "g"),
        ("60", "Cashews", "", 553, 18, 44, 30, "g"),
        ("61", "Sunflower Seeds", "", 584, 21, 51, 20, "g"),
        ("62", "Pumpkin Seeds", "", 559, 30, 49, 11, "g"),
        ("63", "Raisins", "", 299, 3, 0, 79, "g"),
        ("64", "Dates", "", 282, 2, 0, 75, "g"),
        ("65", "Apricots", "", 48, 1, 0, 11, "g"),
        ("66", "Pineapple", "", 50, 0, 0, 13, "g"),
        ("67", "Mango", "", 60, 1, 0, 15, "g"),
        ("68", "Grapes", "", 69, 0, 0, 18, "g"),
        ("69", "Blueberries", "", 57, 0, 0, 14, "g"),
        ("70", "Raspberries", "", 52, 1, 0, 12, "g"),
        ("71", "Blackberries", "", 43, 1, 0, 10, "g"),
        ("72", "Peach", "", 39, 1, 0, 10, "g"),
        ("73", "Plum", "", 46, 0, 0, 11, "g"),
        ("74", "Cherries", "", 50, 1, 0, 12, "g"),
        ("75", "Coconut", "", 354, 3, 33, 15, "g"),
        ("76", "Avocado", "", 160, 2, 15, 9, "g"),
        ("77", "Pomegranate", "", 83, 1, 1, 19, "g"),
        ("78", "Watermelon", "", 30, 1, 0, 8, "g"),
        ("79", "Cantaloupe", "", 34, 1, 0, 8, "g"),
        ("80", "Pear", "", 57, 0, 0, 15, "g"),
        ("81", "Fig", "", 74, 1, 0, 19, "g"),
        ("82", "Papaya", "", 43, 0, 0, 11, "g"),
        ("83", "Guava", "", 68, 2, 1, 14, "g"),
        ("84", "Kiwi", "", 61, 1, 0, 15, "g"),
        ("85", "Lime", "", 30, 0, 0, 10, "g"),
        ("86", "Ginger", "", 80, 2, 0, 18, "g"),
        ("87", "Turmeric", "", 312, 7, 4, 67, "g"),
        ("88", "Cloves", "", 274, 6, 13, 65, "g"),
        ("89", "Cardamom", "", 311, 11, 7, 68, "g"),
        ("90", "Fennel", "", 31, 1, 0, 7, "g"),
        ("91", "Coriander", "", 23, 2, 1, 3, "g"),
        ("92", "Mustard Seeds", "", 508, 26, 36, 28, "g"),
        ("93", "Poppy Seeds", "", 525, 18, 42, 28, "g"),
        ("94", "Sesame Seeds", "", 573, 18, 50, 23, "g"),
        ("95", "Saffron", "", 310, 11, 6, 65, "g"),
        ("96", "Almond Milk", "", 17, 0, 1, 1, "ml"),
        ("97", "Coconut Milk", "", 230, 2, 24, 6, "ml"),
        ("98", "Soy Sauce", "", 53, 8, 0, 5, "ml"),
        ("99", "Apple Cider Vinegar", "", 21, 0, 0, 1, "ml"),
        ("100", "Red Wine Vinegar", "", 19, 0, 0, 0, "ml")
    ]

    # Insert products into Products table
    cursor.executemany('''
        INSERT OR IGNORE INTO Products (id, name, image, calories, protein, fat, carbs, measurement)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', products)

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")
    fill_products_table()
    print("Products table filled with a wider range of 100 different products.")
