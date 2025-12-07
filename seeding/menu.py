from classtypes import *


ingredients = [
    Ingredient(name=Translation(en="Black Tea", es="Té Negro", de="Schwarzer Tee", fr="Thé Noir"), category=Translation(en="Tea", es="Té", de="Tee", fr="Thé"), current_stock=100, order_stock=0, unit_price=0.10, topping=False, calories=2, fat_g=0, sodium_g=0, carbs_g=0, sugar_g=0, caffiene_mg=50, allergens="None"), #0
    Ingredient(name=Translation(en="Green Tea", es="Té Verde", de="Grüner Tee", fr="Thé Vert"), category=Translation(en="Tea", es="Té", de="Tee", fr="Thé"), current_stock=100, order_stock=0, unit_price=0.12, topping=False, calories=2, fat_g=0, sodium_g=0, carbs_g=0, sugar_g=0, caffiene_mg=35, allergens="None"), #1
    Ingredient(name=Translation(en="Oolong Tea", es="Té Oolong", de="Oolong-Tee", fr="Thé Oolong"), category=Translation(en="Tea", es="Té", de="Tee", fr="Thé"), current_stock=100, order_stock=0, unit_price=0.15, topping=False, calories=2, fat_g=0, sodium_g=0, carbs_g=0, sugar_g=0, caffiene_mg=40, allergens="None"), #2
    Ingredient(name=Translation(en="Thai Tea Mix", es="Mezcla de Té Tailandés", de="Thai-Tee-Mischung", fr="Mélange de Thé Thaï"), category=Translation(en="Tea", es="Té", de="Tee", fr="Thé"), current_stock=100, order_stock=0, unit_price=0.20, topping=False, calories=120, fat_g=0, sodium_g=50, carbs_g=28, sugar_g=24, caffiene_mg=40, allergens="None"), #3
    Ingredient(name=Translation(en="Matcha Powder", es="Polvo de Matcha", de="Matcha-Pulver", fr="Poudre de Matcha"), category=Translation(en="Tea", es="Té", de="Tee", fr="Thé"), current_stock=100, order_stock=0, unit_price=0.50, topping=False, calories=5, fat_g=0, sodium_g=0, carbs_g=1, sugar_g=0, caffiene_mg=35, allergens="None"), #4
    Ingredient(name=Translation(en="Coffee", es="Café", de="Kaffee", fr="Café"), category=Translation(en="Coffee", es="Café", de="Kaffee", fr="Café"), current_stock=100, order_stock=0, unit_price=0.25, topping=False, calories=2, fat_g=0, sodium_g=0, carbs_g=0, sugar_g=0, caffiene_mg=95, allergens="None"), #5
    Ingredient(name=Translation(en="Whole Milk", es="Leche Entera", de="Vollmilch", fr="Lait Entier"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.30, topping=False, calories=150, fat_g=8, sodium_g=120, carbs_g=12, sugar_g=12, caffiene_mg=0, allergens="Milk"), #6
    Ingredient(name=Translation(en="Sweetened Condensed Milk", es="Leche Condensada Azucarada", de="Gesüßte Kondensmilch", fr="Lait Concentré Sucré"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.40, topping=False, calories=130, fat_g=3, sodium_g=50, carbs_g=22, sugar_g=22, caffiene_mg=0, allergens="Milk"), #7
    Ingredient(name=Translation(en="Coconut Milk", es="Leche de Coco", de="Kokosmilch", fr="Lait de Coco"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.35, topping=False, calories=45, fat_g=4, sodium_g=15, carbs_g=2, sugar_g=1, caffiene_mg=0, allergens="Tree nuts (Coconut)"), #8
    Ingredient(name=Translation(en="Heavy Cream", es="Crema Espesa", de="Schlagsahne", fr="Crème Épaisse"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.45, topping=False, calories=200, fat_g=22, sodium_g=40, carbs_g=2, sugar_g=1, caffiene_mg=0, allergens="Milk"), #9
    Ingredient(name=Translation(en="Cream Cheese", es="Queso Crema", de="Frischkäse", fr="Fromage à la Crème"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.60, topping=False, calories=80, fat_g=8, sodium_g=90, carbs_g=1, sugar_g=1, caffiene_mg=0, allergens="Milk"), #10
    Ingredient(name=Translation(en="Vanilla Ice Cream", es="Helado de Vainilla", de="Vanilleeis", fr="Crème Glacée à la Vanille"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.75, topping=True, calories=210, fat_g=11, sodium_g=80, carbs_g=24, sugar_g=20, caffiene_mg=0, allergens="Milk"), #11
    Ingredient(name=Translation(en="Ube Ice Cream", es="Helado de Ube", de="Ube-Eis", fr="Crème Glacée à l'Ube"), category=Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), current_stock=100, order_stock=0, unit_price=0.90, topping=True, calories=220, fat_g=11, sodium_g=80, carbs_g=26, sugar_g=22, caffiene_mg=0, allergens="Milk"), #12
    Ingredient(name=Translation(en="Simple Syrup", es="Jarabe Simple", de="Einfacher Sirup", fr="Sirop Simple"), category=Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), current_stock=100, order_stock=0, unit_price=0.05, topping=False, calories=50, fat_g=0, sodium_g=0, carbs_g=14, sugar_g=14, caffiene_mg=0, allergens="None"), #13
    Ingredient(name=Translation(en="Honey", es="Miel", de="Honig", fr="Miel"), category=Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), current_stock=100, order_stock=0, unit_price=0.20, topping=False, calories=64, fat_g=0, sodium_g=1, carbs_g=17, sugar_g=17, caffiene_mg=0, allergens="None"), #14
    Ingredient(name=Translation(en="Brown Sugar Syrup", es="Jarabe de Azúcar Morena", de="Brauner Zuckersirup", fr="Sirop de Sucre Brun"), category=Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), current_stock=100, order_stock=0, unit_price=0.25, topping=False, calories=60, fat_g=0, sodium_g=0, carbs_g=16, sugar_g=16, caffiene_mg=0, allergens="None"), #15
    Ingredient(name=Translation(en="Caramel Syrup", es="Jarabe de Caramelo", de="Karamellsirup", fr="Sirop de Caramel"), category=Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), current_stock=100, order_stock=0, unit_price=0.30, topping=False, calories=70, fat_g=0, sodium_g=5, carbs_g=18, sugar_g=17, caffiene_mg=0, allergens="None"), #16
    Ingredient(name=Translation(en="Mango Purée", es="Puré de Mango", de="Mangopüree", fr="Purée de Mangue"), category=Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), current_stock=100, order_stock=0, unit_price=0.40, topping=False, calories=60, fat_g=0, sodium_g=1, carbs_g=15, sugar_g=13, caffiene_mg=0, allergens="Mango"), #17
    Ingredient(name=Translation(en="Passion Fruit Syrup", es="Jarabe de Maracuyá", de="Passionsfruchtsaft", fr="Sirop de Fruit de la Passion"), category=Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), current_stock=100, order_stock=0, unit_price=0.45, topping=False, calories=50, fat_g=0, sodium_g=1, carbs_g=13, sugar_g=12, caffiene_mg=0, allergens="Passion Fruit"), #18
    Ingredient(name=Translation(en="Peach Syrup", es="Jarabe de Durazno", de="Pfirsichsirup", fr="Sirop de Pêche"), category=Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), current_stock=100, order_stock=0, unit_price=0.35, topping=False, calories=45, fat_g=0, sodium_g=1, carbs_g=12, sugar_g=11, caffiene_mg=0, allergens="Peach"), #19
    Ingredient(name=Translation(en="Strawberry Purée", es="Puré de Fresa", de="Erdbeerpüree", fr="Purée de Fraise"), category=Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), current_stock=100, order_stock=0, unit_price=0.40, topping=False, calories=50, fat_g=0, sodium_g=1, carbs_g=12, sugar_g=10, caffiene_mg=0, allergens="Strawberry"), #20
    Ingredient(name=Translation(en="Pineapple Juice", es="Jugo de Piña", de="Ananassaft", fr="Jus d'Ananas"), category=Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), current_stock=100, order_stock=0, unit_price=0.30, topping=False, calories=60, fat_g=0, sodium_g=2, carbs_g=15, sugar_g=13, caffiene_mg=0, allergens="Pineapple"), #21
    Ingredient(name=Translation(en="Taro Powder", es="Polvo de Taro", de="Taro-Pulver", fr="Poudre de Taro"), category=Translation(en="Taro", es="Taro", de="Taro", fr="Taro"), current_stock=100, order_stock=0, unit_price=0.50, topping=False, calories=100, fat_g=0, sodium_g=10, carbs_g=24, sugar_g=6, caffiene_mg=0, allergens="None"), #22
    Ingredient(name=Translation(en="Black Tapioca Pearls", es="Perlas de Tapioca Negras", de="Schwarze Tapioka-Perlen", fr="Perles de Tapioca Noires"), category=Translation(en="Tapioca", es="Tapioca", de="Tapioka", fr="Tapioca"), current_stock=100, order_stock=0, unit_price=0.15, topping=True, calories=100, fat_g=0, sodium_g=5, carbs_g=26, sugar_g=15, caffiene_mg=0, allergens="None"), #23
    Ingredient(name=Translation(en="Brown Sugar Pearls", es="Perlas de Azúcar Morena", de="Braune Zuckerperlen", fr="Perles de Sucre Brun"), category=Translation(en="Tapioca", es="Tapioca", de="Tapioka", fr="Tapioca"), current_stock=100, order_stock=0, unit_price=0.20, topping=True, calories=110, fat_g=0, sodium_g=5, carbs_g=28, sugar_g=18, caffiene_mg=0, allergens="None"), #24
    Ingredient(name=Translation(en="Coffee Jelly", es="Gelatina de Café", de="Kaffee-Gelee", fr="Gelée de Café"), category=Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), current_stock=100, order_stock=0, unit_price=0.25, topping=True, calories=20, fat_g=0, sodium_g=5, carbs_g=5, sugar_g=3, caffiene_mg=10, allergens="None"), #25
    Ingredient(name=Translation(en="Honey Jelly", es="Gelatina de Miel", de="Honig-Gelee", fr="Gelée de Miel"), category=Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), current_stock=100, order_stock=0, unit_price=0.25, topping=True, calories=40, fat_g=0, sodium_g=5, carbs_g=10, sugar_g=8, caffiene_mg=0, allergens="None"), #26
    Ingredient(name=Translation(en="Lychee Jelly", es="Gelatina de Lichi", de="Litschi-Gelee", fr="Gelée de Litchi"), category=Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), current_stock=100, order_stock=0, unit_price=0.25, topping=True, calories=35, fat_g=0, sodium_g=5, carbs_g=9, sugar_g=7, caffiene_mg=0, allergens="Lychee"), #27
    Ingredient(name=Translation(en="Grass Jelly", es="Gelatina de Hierba", de="Gras-Gelee", fr="Gelée d'Herbe"), category=Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), current_stock=100, order_stock=0, unit_price=0.25, topping=True, calories=30, fat_g=0, sodium_g=5, carbs_g=8, sugar_g=6, caffiene_mg=0, allergens="None"), #28
    Ingredient(name=Translation(en="Red Beans (Sweetened)", es="Frijoles Rojos (Endulzados)", de="Rote Bohnen (Gesüßt)", fr="Haricots Rouges (Sucrés)"), category=Translation(en="Beans", es="Frijoles", de="Bohnen", fr="Haricots"), current_stock=100, order_stock=0, unit_price=0.20, topping=False, calories=120, fat_g=0, sodium_g=5, carbs_g=24, sugar_g=12, caffiene_mg=0, allergens="None"), #29
    Ingredient(name=Translation(en="Nata de Coco", es="Nata de Coco", de="Nata de Coco", fr="Nata de Coco"), category=Translation(en="Coconut", es="Coco", de="Kokosnuss", fr="Noix de Coco"), current_stock=100, order_stock=0, unit_price=0.25, topping=False, calories=40, fat_g=0, sodium_g=10, carbs_g=11, sugar_g=9, caffiene_mg=0, allergens="Tree nuts (Coconut)"), #30
    Ingredient(name=Translation(en="Oreo Cookies", es="Galletas Oreo", de="Oreo-Kekse", fr="Biscuits Oreo"), category=Translation(en="Cookies", es="Galletas", de="Kekse", fr="Biscuits"), current_stock=100, order_stock=0, unit_price=0.10, topping=False, calories=53, fat_g=3, sodium_g=40, carbs_g=8, sugar_g=4, caffiene_mg=0, allergens="Wheat; Milk; Soybeans"), #31
    Ingredient(name=Translation(en="Lemon Juice", es="Jugo de Limón", de="Zitronensaft", fr="Jus de Citron"), category=Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), current_stock=100, order_stock=0, unit_price=0.15, topping=False, calories=7, fat_g=0, sodium_g=1, carbs_g=2, sugar_g=1, caffiene_mg=0, allergens="None"), #32
    Ingredient(name=Translation(en="Salt", es="Sal", de="Salz", fr="Sel"), category=Translation(en="Seasoning", es="Condimento", de="Gewürz", fr="Assaisonnement"), current_stock=100, order_stock=0, unit_price=0.02, topping=False, calories=0, fat_g=0, sodium_g=0, carbs_g=0, sugar_g=0, caffiene_mg=0, allergens="None"), #33
]

# of items = 16
items = [
    # Milky Series
    Menu(name=Translation(en="Classic Pearl Milk Tea", es="Té con Leche y Perlas Clásico", de="Klassischer Perlen-Milchtee", fr="Thé au Lait aux Perles Classique"), category=Translation(en="Milky Series", es="Serie Láctea", de="Milchserie", fr="Série Laiteuse"), price=5.80, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/90481017-9d8b-40a0-8567-b0a7903b03cd.jpeg"),
    Menu(name=Translation(en="Taro Pearl Milk Tea", es="Té con Leche y Perlas de Taro", de="Taro-Perlen-Milchtee", fr="Thé au Lait aux Perles de Taro"), category=Translation(en="Milky Series", es="Serie Láctea", de="Milchserie", fr="Série Laiteuse"), price=6.25, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/5336c161-4f07-48ac-b973-0f112a662cfc.jpeg"),

    # Fresh Brew
    Menu(name=Translation(en="Classic Tea", es="Té Clásico", de="Klassischer Tee", fr="Thé Classique"), category=Translation(en="Fresh Brew", es="Infusión Fresca", de="Frischer Aufguss", fr="Infusion Fraîche"), price=4.65, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/db180e83-5b37-42d4-81bb-985390380d10.jpeg"),
    Menu(name=Translation(en="Honey Tea", es="Té con Miel", de="Honig-Tee", fr="Thé au Miel"), category=Translation(en="Fresh Brew", es="Infusión Fresca", de="Frischer Aufguss", fr="Infusion Fraîche"), price=4.85, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/f2093c6e-ffee-4204-9687-eac963ab00b3.jpeg"),

    # Fruity Beverages
    Menu(name=Translation(en="Mango Green Tea", es="Té Verde de Mango", de="Mango-Grüntee", fr="Thé Vert à la Mangue"), category=Translation(en="Fruity Beverage", es="Bebida Afrutada", de="Fruchtiges Getränk", fr="Boisson Fruitée"), price=5.80, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/674af5be-9134-46a7-be52-0c90c92f59ec.jpeg"),
    Menu(name=Translation(en="Passion Chess", es="Ajedrez de Maracuyá", de="Passionsfrucht-Schach", fr="Échecs de Fruit de la Passion"), category=Translation(en="Fruity Beverage", es="Bebida Afrutada", de="Fruchtiges Getränk", fr="Boisson Fruitée"), price=6.25, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/3e16d757-e9d5-4b4c-b90b-671af05bd4f7.jpeg"),
    Menu(name=Translation(en="Peach Tea w/ Honey Jelly", es="Té de Durazno con Gelatina de Miel", de="Pfirsich-Tee mit Honig-Gelee", fr="Thé à la Pêche avec Gelée de Miel"), category=Translation(en="Fruity Beverage", es="Bebida Afrutada", de="Fruchtiges Getränk", fr="Boisson Fruitée"), price=6.25, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/e9a0d911-fddb-437d-b662-908c94792f0d.jpeg"),

    # Non-Caffeinated
    Menu(name=Translation(en="Tiger Boba", es="Boba Tigre", de="Tiger-Boba", fr="Boba Tigre"), category=Translation(en="Non-Caffeinated", es="Sin Cafeína", de="Koffeinfrei", fr="Sans Caféine"), price=6.50, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/e5316999-7d07-4d38-b672-c07d89ab25ce.png"),
    Menu(name=Translation(en="Halo Halo", es="Halo Halo", de="Halo Halo", fr="Halo Halo"), category=Translation(en="Non-Caffeinated", es="Sin Cafeína", de="Koffeinfrei", fr="Sans Caféine"), price=6.95, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/7bcd2370-722e-44c8-ae25-a5a9b375bb3d.webp"),

    # New Matcha Series
    Menu(name=Translation(en="Matcha Pearl Milk Tea", es="Té con Leche y Perlas de Matcha", de="Matcha-Perlen-Milchtee", fr="Thé au Lait aux Perles de Matcha"), category=Translation(en="New Matcha Series", es="Nueva Serie Matcha", de="Neue Matcha-Serie", fr="Nouvelle Série Matcha"), price=6.50, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/3f4bed35-0a68-4fa9-8a29-f8544c9a2739.png"),
    Menu(name=Translation(en="Strawberry Matcha Fresh Milk", es="Leche Fresca de Matcha con Fresa", de="Erdbeer-Matcha-Frischmilch", fr="Lait Frais au Matcha et à la Fraise"), category=Translation(en="New Matcha Series", es="Nueva Serie Matcha", de="Neue Matcha-Serie", fr="Nouvelle Série Matcha"), price=6.50, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/efe3d01c-129a-4d84-be95-a358c5685745.png"),
    Menu(name=Translation(en="Mango Matcha Fresh Milk", es="Leche Fresca de Matcha con Mango", de="Mango-Matcha-Frischmilch", fr="Lait Frais au Matcha et à la Mangue"), category=Translation(en="New Matcha Series", es="Nueva Serie Matcha", de="Neue Matcha-Serie", fr="Nouvelle Série Matcha"), price=6.50, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/789fca44-8636-4cbe-947c-7ec9aab99680.png"),

    # Ice-Blended
    Menu(name=Translation(en="Oreo w/ Pearl", es="Oreo con Perlas", de="Oreo mit Perlen", fr="Oreo aux Perles"), category=Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), price=6.75, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/bec7035d-2b87-430a-8ee1-1dd7ac96bcce.jpeg"),
    Menu(name=Translation(en="Coffee w/ Ice Cream", es="Café con Helado", de="Kaffee mit Eiscreme", fr="Café à la Crème Glacée"), category=Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), price=6.75, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/c9ec508b-1142-47fe-8d7a-656700821165.jpeg"),
    Menu(name=Translation(en="Strawberry w/ Lychee Jelly & Ice Cream", es="Fresa con Gelatina de Lichi y Helado", de="Erdbeere mit Litschi-Gelee und Eiscreme", fr="Fraise avec Gelée de Litchi et Crème Glacée"), category=Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), price=6.75, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/94be56d1-83c0-4c7b-892a-befc2090eefd.png"),
    Menu(name=Translation(en="Lava Flow", es="Flujo de Lava", de="Lavafluss", fr="Flux de Lave"), category=Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), price=6.95, image_url="https://pub-2af9e072394d4d859d3f92c6c319bc13.r2.dev/edf3b6da-9308-4120-b7b6-cac04b90312f.webp"),
]

recipes = [
    # Classic Pearl Milk Tea
    Recipe(menu_item_id=items[0].id, ingredient_id=ingredients[0].id, quantity=1),   # Black Tea
    Recipe(menu_item_id=items[0].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[0].id, ingredient_id=ingredients[13].id, quantity=1),  # Simple Syrup
    Recipe(menu_item_id=items[0].id, ingredient_id=ingredients[23].id, quantity=1),  # Black Tapioca Pearls

    # Taro Pearl Milk Tea
    Recipe(menu_item_id=items[1].id, ingredient_id=ingredients[1].id, quantity=2),   # Green Tea
    Recipe(menu_item_id=items[1].id, ingredient_id=ingredients[22].id, quantity=1),  # Taro Powder
    Recipe(menu_item_id=items[1].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[1].id, ingredient_id=ingredients[23].id, quantity=1),  # Black Tapioca Pearls

    # Classic Tea
    Recipe(menu_item_id=items[2].id, ingredient_id=ingredients[0].id, quantity=1),   # Black Tea
    Recipe(menu_item_id=items[2].id, ingredient_id=ingredients[13].id, quantity=1),  # Simple Syrup

    # Honey Tea
    Recipe(menu_item_id=items[3].id, ingredient_id=ingredients[1].id, quantity=2),   # Green Tea
    Recipe(menu_item_id=items[3].id, ingredient_id=ingredients[14].id, quantity=1),  # Honey

    # Mango Green Tea
    Recipe(menu_item_id=items[4].id, ingredient_id=ingredients[0].id, quantity=1),   # Green Tea
    Recipe(menu_item_id=items[4].id, ingredient_id=ingredients[18].id, quantity=1), # Mango Purée
    Recipe(menu_item_id=items[4].id, ingredient_id=ingredients[32].id, quantity=1), # Lemon Juice

    # Passion Chess
    Recipe(menu_item_id=items[5].id, ingredient_id=ingredients[1].id, quantity=2),   # Green Tea
    Recipe(menu_item_id=items[5].id, ingredient_id=ingredients[18].id, quantity=1),  # Passion Fruit Syrup
    Recipe(menu_item_id=items[5].id, ingredient_id=ingredients[10].id, quantity=1),  # Cream Cheese (for foam)
    Recipe(menu_item_id=items[5].id, ingredient_id=ingredients[8].id, quantity=1),  # Heavy Cream (foam base)
    Recipe(menu_item_id=items[5].id, ingredient_id=ingredients[33].id, quantity=1),  # Salt (pinch for foam)

    # Peach Tea w/ Honey Jelly
    Recipe(menu_item_id=items[6].id, ingredient_id=ingredients[0].id, quantity=1),   # Black Tea
    Recipe(menu_item_id=items[6].id, ingredient_id=ingredients[19].id, quantity=1),  # Peach Syrup
    Recipe(menu_item_id=items[6].id, ingredient_id=ingredients[26].id, quantity=1),  # Honey Jelly

    # Tiger Boba
    Recipe(menu_item_id=items[7].id, ingredient_id=ingredients[15].id, quantity=1),  # Brown Sugar Syrup
    Recipe(menu_item_id=items[7].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[7].id, ingredient_id=ingredients[24].id, quantity=1),  # Brown Sugar Pearls

    # Halo Halo
    Recipe(menu_item_id=items[8].id, ingredient_id=ingredients[30].id, quantity=1),  # Nata de Coco
    Recipe(menu_item_id=items[8].id, ingredient_id=ingredients[28].id, quantity=1),  # Grass Jelly
    Recipe(menu_item_id=items[8].id, ingredient_id=ingredients[29].id, quantity=1),  # Red Beans
    Recipe(menu_item_id=items[8].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[8].id, ingredient_id=ingredients[12].id, quantity=1),  # Ube Ice Cream

    # Matcha Pearl Milk Tea
    Recipe(menu_item_id=items[9].id, ingredient_id=ingredients[4].id, quantity=1),  # Matcha Powder
    Recipe(menu_item_id=items[9].id, ingredient_id=ingredients[6].id, quantity=1),  # Whole Milk
    Recipe(menu_item_id=items[9].id, ingredient_id=ingredients[13].id, quantity=1), # Simple Syrup
    Recipe(menu_item_id=items[9].id, ingredient_id=ingredients[23].id, quantity=1), # Black Tapioca Pearls

    # Strawberry Matcha Fresh Milk
    Recipe(menu_item_id=items[10].id, ingredient_id=ingredients[4].id, quantity=1),  # Matcha Powder
    Recipe(menu_item_id=items[10].id, ingredient_id=ingredients[6].id, quantity=1),  # Whole Milk
    Recipe(menu_item_id=items[10].id, ingredient_id=ingredients[20].id, quantity=1), # Strawberry Purée

    # Mango Matcha Fresh Milk
    Recipe(menu_item_id=items[11].id, ingredient_id=ingredients[4].id, quantity=1),  # Matcha Powder
    Recipe(menu_item_id=items[11].id, ingredient_id=ingredients[6].id, quantity=1),  # Whole Milk
    Recipe(menu_item_id=items[11].id, ingredient_id=ingredients[17].id, quantity=1), # Mango Purée

    # Oreo w/ Pearl
    Recipe(menu_item_id=items[12].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[12].id, ingredient_id=ingredients[31].id, quantity=2),  # Oreo Cookies (2 pcs)
    Recipe(menu_item_id=items[12].id, ingredient_id=ingredients[13].id, quantity=1),  # Simple Syrup
    Recipe(menu_item_id=items[12].id, ingredient_id=ingredients[23].id, quantity=1),  # Black Tapioca Pearls

    # Coffee w/ Ice Cream
    Recipe(menu_item_id=items[13].id, ingredient_id=ingredients[5].id, quantity=1),   # Coffee
    Recipe(menu_item_id=items[13].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[13].id, ingredient_id=ingredients[13].id, quantity=1),  # Simple Syrup
    Recipe(menu_item_id=items[13].id, ingredient_id=ingredients[11].id, quantity=1),  # Vanilla Ice Cream

    # Strawberry w/ Lychee Jelly & Ice Cream
    Recipe(menu_item_id=items[14].id, ingredient_id=ingredients[6].id, quantity=1),   # Whole Milk
    Recipe(menu_item_id=items[14].id, ingredient_id=ingredients[20].id, quantity=1),  # Strawberry Purée
    Recipe(menu_item_id=items[14].id, ingredient_id=ingredients[27].id, quantity=1),  # Lychee Jelly
    Recipe(menu_item_id=items[14].id, ingredient_id=ingredients[11].id, quantity=1),  # Vanilla Ice Cream

    # Lava Flow
    Recipe(menu_item_id=items[15].id, ingredient_id=ingredients[8].id, quantity=1),   # Coconut Milk
    Recipe(menu_item_id=items[15].id, ingredient_id=ingredients[21].id, quantity=1),  # Pineapple Juice
    Recipe(menu_item_id=items[15].id, ingredient_id=ingredients[20].id, quantity=1),  # Strawberry Purée
]
