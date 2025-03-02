import sqlite3

from database.products import products
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
            category TEXT,
            snackable BOOL
            
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





    # Insert products into Products table
    cursor.executemany('''
        INSERT OR IGNORE INTO Products (id, name, image, calories, protein, fat, carbs, measurement, category, snackable)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
