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
