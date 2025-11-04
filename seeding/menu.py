from classtypes import *


ingredients = [
    Ingredient("Black Tea", "Tea", 100, 0, 0.10), #0
    Ingredient("Green Tea", "Tea", 100, 0, 0.12), #1
    Ingredient("Oolong Tea", "Tea", 100, 0, 0.15), #2
    Ingredient("Thai Tea Mix", "Tea", 100, 0, 0.20), #3
    Ingredient("Matcha Powder", "Tea", 100, 0, 0.50), #4
    Ingredient("Coffee", "Coffee", 100, 0, 0.25), #5
    Ingredient("Whole Milk", "Dairy", 100, 0, 0.30), #6
    Ingredient("Sweetened Condensed Milk", "Dairy", 100, 0, 0.40), #7
    Ingredient("Coconut Milk", "Dairy", 100, 0, 0.35), #8
    Ingredient("Heavy Cream", "Dairy", 100, 0, 0.45), #9
    Ingredient("Cream Cheese", "Dairy", 100, 0, 0.60), #10
    Ingredient("Vanilla Ice Cream", "Dairy", 100, 0, 0.75), #11
    Ingredient("Ube Ice Cream", "Dairy", 100, 0, 0.90), #12
    Ingredient("Simple Syrup", "Syrup", 100, 0, 0.05), #13
    Ingredient("Honey", "Syrup", 100, 0, 0.20), #14
    Ingredient("Brown Sugar Syrup", "Syrup", 100, 0, 0.25), #15
    Ingredient("Caramel Syrup", "Syrup", 100, 0, 0.30), #16
    Ingredient("Mango Purée", "Fruit", 100, 0, 0.40), #17
    Ingredient("Passion Fruit Syrup", "Fruit", 100, 0, 0.45), #18
    Ingredient("Peach Syrup", "Fruit", 100, 0, 0.35), #19
    Ingredient("Strawberry Purée", "Fruit", 100, 0, 0.40), #20
    Ingredient("Pineapple Juice", "Fruit", 100, 0, 0.30), #21
    Ingredient("Taro Powder", "Taro", 100, 0, 0.50), #22
    Ingredient("Black Tapioca Pearls", "Tapioca", 100, 0, 0.15), #23
    Ingredient("Brown Sugar Pearls", "Tapioca", 100, 0, 0.20), #24
    Ingredient("Coffee Jelly", "Jelly", 100, 0, 0.25), #25
    Ingredient("Honey Jelly", "Jelly", 100, 0, 0.25), #26
    Ingredient("Lychee Jelly", "Jelly", 100, 0, 0.25), #27
    Ingredient("Grass Jelly", "Jelly", 100, 0, 0.25), #28
    Ingredient("Red Beans (Sweetened)", "Beans", 100, 0, 0.20), #29
    Ingredient("Nata de Coco", "Coconut", 100, 0, 0.25), #30
    Ingredient("Oreo Cookies", "Cookies", 100, 0, 0.10), #31
    Ingredient("Lemon Juice", "Fruit", 100, 0, 0.15), #32
    Ingredient("Salt", "Seasoning", 100, 0, 0.02), #33
    Ingredient("Ice Cubes", "Ice", 100, 0, 0.01), #34
    Ingredient("Crushed Ice", "Ice", 100, 0, 0.01), #35
]

# of items = 16
items = [
    # Milky Series
    Menu("Classic Pearl Milk Tea", "Milky Series", 5.80),
    Menu("Taro Pearl Milk Tea", "Milky Series", 6.25),

    # Fresh Brew
    Menu("Classic Tea", "Fresh Brew", 4.65),
    Menu("Honey Tea", "Fresh Brew", 4.85),

    # Fruity Beverages
    Menu("Mango Green Tea", "Fruity Beverage", 5.80),
    Menu("Passion Chess", "Fruity Beverage", 6.25),
    Menu("Peach Tea w/ Honey Jelly", "Fruity Beverage", 6.25),

    # Non-Caffeinated
    Menu("Tiger Boba", "Non-Caffeinated", 6.50),
    Menu("Halo Halo", "Non-Caffeinated", 6.95),

    # New Matcha Series
    Menu("Matcha Pearl Milk Tea", "New Matcha Series", 6.50),
    Menu("Strawberry Matcha Fresh Milk", "New Matcha Series", 6.50),
    Menu("Mango Matcha Fresh Milk", "New Matcha Series", 6.50),

    # Ice-Blended
    Menu("Oreo w/ Pearl", "Ice-Blended", 6.75),
    Menu("Coffee w/ Ice Cream", "Ice-Blended", 6.75),
    Menu("Strawberry w/ Lychee Jelly & Ice Cream", "Ice-Blended", 6.75),
    Menu("Lava Flow", "Ice-Blended", 6.95),
]

recipes = [
    # Classic Pearl Milk Tea
    Recipe(items[0].id, ingredients[0].id, 1),   # Black Tea
    Recipe(items[0].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[0].id, ingredients[13].id, 1),  # Simple Syrup
    Recipe(items[0].id, ingredients[23].id, 1),  # Black Tapioca Pearls
    Recipe(items[0].id, ingredients[34].id, 1),  # Ice Cubes

    # Taro Pearl Milk Tea
    Recipe(items[1].id, ingredients[1].id, 2),   # Green Tea
    Recipe(items[1].id, ingredients[22].id, 1),  # Taro Powder
    Recipe(items[1].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[1].id, ingredients[23].id, 1),  # Black Tapioca Pearls
    Recipe(items[1].id, ingredients[34].id, 1),  # Ice Cubes

    # Classic Tea
    Recipe(items[2].id, ingredients[0].id, 1),   # Black Tea
    Recipe(items[2].id, ingredients[13].id, 1),  # Simple Syrup
    Recipe(items[2].id, ingredients[34].id, 1),  # Ice Cubes

    # Honey Tea
    Recipe(items[3].id, ingredients[1].id, 2),   # Green Tea
    Recipe(items[3].id, ingredients[14].id, 1),  # Honey
    Recipe(items[3].id, ingredients[34].id, 1),  # Ice Cubes

    # Mango Green Tea
    Recipe(items[4].id, ingredients[0].id, 1),   # Green Tea
    Recipe(items[4].id, ingredients[18].id, 1), # Mango Purée
    Recipe(items[4].id, ingredients[32].id, 1), # Lemon Juice
    Recipe(items[4].id, ingredients[35].id, 1), # Ice Cubes

    # Passion Chess
    Recipe(items[5].id, ingredients[1].id, 2),   # Green Tea
    Recipe(items[5].id, ingredients[18].id, 1),  # Passion Fruit Syrup
    Recipe(items[5].id, ingredients[10].id, 1),  # Cream Cheese (for foam)
    Recipe(items[5].id, ingredients[8].id, 1),  # Heavy Cream (foam base)
    Recipe(items[5].id, ingredients[33].id, 1),  # Salt (pinch for foam)
    Recipe(items[5].id, ingredients[34].id, 1),  # Ice Cubes

    # Peach Tea w/ Honey Jelly
    Recipe(items[6].id, ingredients[0].id, 1),   # Black Tea
    Recipe(items[6].id, ingredients[19].id, 1),  # Peach Syrup
    Recipe(items[6].id, ingredients[26].id, 1),  # Honey Jelly
    Recipe(items[6].id, ingredients[34].id, 1),  # Ice Cubes

    # Tiger Boba
    Recipe(items[7].id, ingredients[15].id, 1),  # Brown Sugar Syrup
    Recipe(items[7].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[7].id, ingredients[24].id, 1),  # Brown Sugar Pearls
    Recipe(items[7].id, ingredients[33].id, 1),  # Ice Cubes

    # Halo Halo
    Recipe(items[8].id, ingredients[30].id, 1),  # Nata de Coco
    Recipe(items[8].id, ingredients[28].id, 1),  # Grass Jelly
    Recipe(items[8].id, ingredients[29].id, 1),  # Red Beans
    Recipe(items[8].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[8].id, ingredients[12].id, 1),  # Ube Ice Cream
    Recipe(items[8].id, ingredients[35].id, 1),  # Crushed Ice

    # Matcha Pearl Milk Tea
    Recipe(items[9].id, ingredients[4].id, 1),  # Matcha Powder
    Recipe(items[9].id, ingredients[6].id, 1),  # Whole Milk
    Recipe(items[9].id, ingredients[13].id, 1), # Simple Syrup
    Recipe(items[9].id, ingredients[23].id, 1), # Black Tapioca Pearls
    Recipe(items[9].id, ingredients[34].id, 1), # Ice Cubes

    # Strawberry Matcha Fresh Milk
    Recipe(items[10].id, ingredients[4].id, 1),  # Matcha Powder
    Recipe(items[10].id, ingredients[6].id, 1),  # Whole Milk
    Recipe(items[10].id, ingredients[20].id, 1), # Strawberry Purée
    Recipe(items[10].id, ingredients[34].id, 1), # Ice Cubes

    # Mango Matcha Fresh Milk
    Recipe(items[11].id, ingredients[4].id, 1),  # Matcha Powder
    Recipe(items[11].id, ingredients[6].id, 1),  # Whole Milk
    Recipe(items[11].id, ingredients[17].id, 1), # Mango Purée
    Recipe(items[11].id, ingredients[34].id, 1), # Ice Cubes

    # Oreo w/ Pearl
    Recipe(items[12].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[12].id, ingredients[31].id, 2),  # Oreo Cookies (2 pcs)
    Recipe(items[12].id, ingredients[13].id, 1),  # Simple Syrup
    Recipe(items[12].id, ingredients[23].id, 1),  # Black Tapioca Pearls
    Recipe(items[12].id, ingredients[35].id, 1),  # Crushed Ice

    # Coffee w/ Ice Cream
    Recipe(items[13].id, ingredients[5].id, 1),   # Coffee
    Recipe(items[13].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[13].id, ingredients[13].id, 1),  # Simple Syrup
    Recipe(items[13].id, ingredients[11].id, 1),  # Vanilla Ice Cream
    Recipe(items[13].id, ingredients[34].id, 1),  # Ice Cubes

    # Strawberry w/ Lychee Jelly & Ice Cream
    Recipe(items[14].id, ingredients[6].id, 1),   # Whole Milk
    Recipe(items[14].id, ingredients[20].id, 1),  # Strawberry Purée
    Recipe(items[14].id, ingredients[27].id, 1),  # Lychee Jelly
    Recipe(items[14].id, ingredients[11].id, 1),  # Vanilla Ice Cream
    Recipe(items[14].id, ingredients[35].id, 1),  # Crushed Ice

    # Lava Flow
    Recipe(items[15].id, ingredients[8].id, 1),   # Coconut Milk
    Recipe(items[15].id, ingredients[21].id, 1),  # Pineapple Juice
    Recipe(items[15].id, ingredients[20].id, 1),  # Strawberry Purée
    Recipe(items[15].id, ingredients[35].id, 1),  # Crushed Ice
]

nutrition = [
    NutritionInfo(ingredients[0].id, 2, 0, 0, 0, 0, 50),   # Black Tea
    NutritionInfo(ingredients[1].id, 2, 0, 0, 0, 0, 35),   # Green Tea
    NutritionInfo(ingredients[2].id, 2, 0, 0, 0, 0, 40),   # Oolong Tea
    NutritionInfo(ingredients[3].id, 120, 0, 50, 28, 24, 40), # Thai Tea Mix
    NutritionInfo(ingredients[4].id, 5, 0, 0, 1, 0, 35),   # Matcha Powder
    NutritionInfo(ingredients[5].id, 2, 0, 0, 0, 0, 95),   # Coffee
    NutritionInfo(ingredients[6].id, 150, 8, 120, 12, 12, 0), # Whole Milk
    NutritionInfo(ingredients[7].id, 130, 3, 50, 22, 22, 0), # Sweetened Condensed Milk
    NutritionInfo(ingredients[8].id, 45, 4, 15, 2, 1, 0),  # Coconut Milk
    NutritionInfo(ingredients[9].id, 200, 22, 40, 2, 1, 0), # Heavy Cream
    NutritionInfo(ingredients[10].id, 80, 8, 90, 1, 1, 0),  # Cream Cheese
    NutritionInfo(ingredients[11].id, 210, 11, 80, 24, 20, 0), # Vanilla Ice Cream
    NutritionInfo(ingredients[12].id, 220, 11, 80, 26, 22, 0), # Ube Ice Cream
    NutritionInfo(ingredients[13].id, 50, 0, 0, 14, 14, 0), # Simple Syrup
    NutritionInfo(ingredients[14].id, 64, 0, 1, 17, 17, 0), # Honey
    NutritionInfo(ingredients[15].id, 60, 0, 0, 16, 16, 0), # Brown Sugar Syrup
    NutritionInfo(ingredients[16].id, 70, 0, 5, 18, 17, 0), # Caramel Syrup
    NutritionInfo(ingredients[17].id, 60, 0, 1, 15, 13, 0), # Mango Purée
    NutritionInfo(ingredients[18].id, 50, 0, 1, 13, 12, 0), # Passion Fruit Syrup
    NutritionInfo(ingredients[19].id, 45, 0, 1, 12, 11, 0), # Peach Syrup
    NutritionInfo(ingredients[20].id, 50, 0, 1, 12, 10, 0), # Strawberry Purée
    NutritionInfo(ingredients[21].id, 60, 0, 2, 15, 13, 0), # Pineapple Juice
    NutritionInfo(ingredients[22].id, 100, 0, 10, 24, 6, 0), # Taro Powder
    NutritionInfo(ingredients[23].id, 100, 0, 5, 26, 15, 0), # Black Tapioca Pearls
    NutritionInfo(ingredients[24].id, 110, 0, 5, 28, 18, 0), # Brown Sugar Pearls
    NutritionInfo(ingredients[25].id, 20, 0, 5, 5, 3, 10),  # Coffee Jelly
    NutritionInfo(ingredients[26].id, 40, 0, 5, 10, 8, 0),  # Honey Jelly
    NutritionInfo(ingredients[27].id, 35, 0, 5, 9, 7, 0),   # Lychee Jelly
    NutritionInfo(ingredients[28].id, 30, 0, 5, 8, 6, 0),   # Grass Jelly
    NutritionInfo(ingredients[29].id, 120, 0, 5, 24, 12, 0), # Red Beans (Sweetened)
    NutritionInfo(ingredients[30].id, 40, 0, 10, 11, 9, 0), # Nata de Coco
    NutritionInfo(ingredients[31].id, 53, 3, 40, 8, 4, 0),  # Oreo Cookies (per cookie)
    NutritionInfo(ingredients[32].id, 7, 0, 1, 2, 1, 0),    # Lemon Juice
    NutritionInfo(ingredients[33].id, 0, 0, 0, 0, 0, 0),    # Salt
    NutritionInfo(ingredients[34].id, 0, 0, 0, 0, 0, 0),    # Ice Cubes
    NutritionInfo(ingredients[35].id, 0, 0, 0, 0, 0, 0),    # Crushed Ice
]

allergens = [
    AllergenInfo(ingredients[0].id, "None"),                     # Black Tea
    AllergenInfo(ingredients[1].id, "None"),                     # Green Tea
    AllergenInfo(ingredients[2].id, "None"),                     # Oolong Tea
    AllergenInfo(ingredients[3].id, "None"),                     # Thai Tea Mix
    AllergenInfo(ingredients[4].id, "None"),                     # Matcha Powder
    AllergenInfo(ingredients[5].id, "None"),                     # Coffee
    AllergenInfo(ingredients[6].id, "Milk"),                     # Whole Milk
    AllergenInfo(ingredients[7].id, "Milk"),                     # Sweetened Condensed Milk
    AllergenInfo(ingredients[8].id, "Tree nuts (Coconut)"),      # Coconut Milk
    AllergenInfo(ingredients[9].id, "Milk"),                     # Heavy Cream
    AllergenInfo(ingredients[10].id, "Milk"),                    # Cream Cheese
    AllergenInfo(ingredients[11].id, "Milk"),                    # Vanilla Ice Cream
    AllergenInfo(ingredients[12].id, "Milk"),                    # Ube Ice Cream
    AllergenInfo(ingredients[13].id, "None"),                    # Simple Syrup
    AllergenInfo(ingredients[14].id, "None"),                    # Honey
    AllergenInfo(ingredients[15].id, "None"),                    # Brown Sugar Syrup
    AllergenInfo(ingredients[16].id, "None"),                    # Caramel Syrup
    AllergenInfo(ingredients[17].id, "Mango"),                   # Mango Purée
    AllergenInfo(ingredients[18].id, "Passion Fruit"),           # Passion Fruit Syrup
    AllergenInfo(ingredients[19].id, "Peach"),                   # Peach Syrup
    AllergenInfo(ingredients[20].id, "Strawberry"),              # Strawberry Purée
    AllergenInfo(ingredients[21].id, "Pineapple"),               # Pineapple Juice
    AllergenInfo(ingredients[22].id, "None"),                    # Taro Powder
    AllergenInfo(ingredients[23].id, "None"),                    # Black Tapioca Pearls
    AllergenInfo(ingredients[24].id, "None"),                    # Brown Sugar Pearls
    AllergenInfo(ingredients[25].id, "None"),                    # Coffee Jelly
    AllergenInfo(ingredients[26].id, "None"),                    # Honey Jelly
    AllergenInfo(ingredients[27].id, "Lychee"),                  # Lychee Jelly
    AllergenInfo(ingredients[28].id, "None"),                    # Grass Jelly
    AllergenInfo(ingredients[29].id, "None"),                    # Red Beans (Sweetened)
    AllergenInfo(ingredients[30].id, "Tree nuts (Coconut)"),     # Nata de Coco
    AllergenInfo(ingredients[31].id, "Wheat"),                   # Oreo Cookies (per cookie)
    AllergenInfo(ingredients[31].id, "Milk"),                    # Oreo Cookies (per cookie)
    AllergenInfo(ingredients[31].id, "Soybeans"),                # Oreo Cookies (per cookie)
    AllergenInfo(ingredients[32].id, "None"),                    # Lemon Juice
    AllergenInfo(ingredients[33].id, "None"),                    # Salt
    AllergenInfo(ingredients[34].id, "None"),                    # Ice Cubes
    AllergenInfo(ingredients[35].id, "None"),                    # Crushed Ice
]