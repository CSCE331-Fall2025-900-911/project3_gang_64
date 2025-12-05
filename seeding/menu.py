from classtypes import *


ingredients = [
    Ingredient(Translation(en="Black Tea", es="Té Negro", de="Schwarzer Tee", fr="Thé Noir"), Translation(en="Tea", es="Té", de="Tee", fr="Thé"), 100, 0, 0.10, 2, 0, 0, 0, 0, 50, "None"), #0
    Ingredient(Translation(en="Green Tea", es="Té Verde", de="Grüner Tee", fr="Thé Vert"), Translation(en="Tea", es="Té", de="Tee", fr="Thé"), 100, 0, 0.12, 2, 0, 0, 0, 0, 35, "None"), #1
    Ingredient(Translation(en="Oolong Tea", es="Té Oolong", de="Oolong-Tee", fr="Thé Oolong"), Translation(en="Tea", es="Té", de="Tee", fr="Thé"), 100, 0, 0.15, 2, 0, 0, 0, 0, 40, "None"), #2
    Ingredient(Translation(en="Thai Tea Mix", es="Mezcla de Té Tailandés", de="Thai-Tee-Mischung", fr="Mélange de Thé Thaï"), Translation(en="Tea", es="Té", de="Tee", fr="Thé"), 100, 0, 0.20, 120, 0, 50, 28, 24, 40, "None"), #3
    Ingredient(Translation(en="Matcha Powder", es="Polvo de Matcha", de="Matcha-Pulver", fr="Poudre de Matcha"), Translation(en="Tea", es="Té", de="Tee", fr="Thé"), 100, 0, 0.50, 5, 0, 0, 1, 0, 35, "None"), #4
    Ingredient(Translation(en="Coffee", es="Café", de="Kaffee", fr="Café"), Translation(en="Coffee", es="Café", de="Kaffee", fr="Café"), 100, 0, 0.25, 2, 0, 0, 0, 0, 95, "None"), #5
    Ingredient(Translation(en="Whole Milk", es="Leche Entera", de="Vollmilch", fr="Lait Entier"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.30, 150, 8, 120, 12, 12, 0, "Milk"), #6
    Ingredient(Translation(en="Sweetened Condensed Milk", es="Leche Condensada Azucarada", de="Gesüßte Kondensmilch", fr="Lait Concentré Sucré"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.40, 130, 3, 50, 22, 22, 0, "Milk"), #7
    Ingredient(Translation(en="Coconut Milk", es="Leche de Coco", de="Kokosmilch", fr="Lait de Coco"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.35, 45, 4, 15, 2, 1, 0, "Tree nuts (Coconut)"), #8
    Ingredient(Translation(en="Heavy Cream", es="Crema Espesa", de="Schlagsahne", fr="Crème Épaisse"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.45, 200, 22, 40, 2, 1, 0, "Milk"), #9
    Ingredient(Translation(en="Cream Cheese", es="Queso Crema", de="Frischkäse", fr="Fromage à la Crème"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.60, 80, 8, 90, 1, 1, 0, "Milk"), #10
    Ingredient(Translation(en="Vanilla Ice Cream", es="Helado de Vainilla", de="Vanilleeis", fr="Crème Glacée à la Vanille"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.75, 210, 11, 80, 24, 20, 0, "Milk"), #11
    Ingredient(Translation(en="Ube Ice Cream", es="Helado de Ube", de="Ube-Eis", fr="Crème Glacée à l'Ube"), Translation(en="Dairy", es="Lácteos", de="Milchprodukte", fr="Produits Laitiers"), 100, 0, 0.90, 220, 11, 80, 26, 22, 0, "Milk"), #12
    Ingredient(Translation(en="Simple Syrup", es="Jarabe Simple", de="Einfacher Sirup", fr="Sirop Simple"), Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), 100, 0, 0.05, 50, 0, 0, 14, 14, 0, "None"), #13
    Ingredient(Translation(en="Honey", es="Miel", de="Honig", fr="Miel"), Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), 100, 0, 0.20, 64, 0, 1, 17, 17, 0, "None"), #14
    Ingredient(Translation(en="Brown Sugar Syrup", es="Jarabe de Azúcar Morena", de="Brauner Zuckersirup", fr="Sirop de Sucre Brun"), Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), 100, 0, 0.25, 60, 0, 0, 16, 16, 0, "None"), #15
    Ingredient(Translation(en="Caramel Syrup", es="Jarabe de Caramelo", de="Karamellsirup", fr="Sirop de Caramel"), Translation(en="Syrup", es="Jarabe", de="Sirup", fr="Sirop"), 100, 0, 0.30, 70, 0, 5, 18, 17, 0, "None"), #16
    Ingredient(Translation(en="Mango Purée", es="Puré de Mango", de="Mangopüree", fr="Purée de Mangue"), Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), 100, 0, 0.40, 60, 0, 1, 15, 13, 0, "Mango"), #17
    Ingredient(Translation(en="Passion Fruit Syrup", es="Jarabe de Maracuyá", de="Passionsfruchtsaft", fr="Sirop de Fruit de la Passion"), Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), 100, 0, 0.45, 50, 0, 1, 13, 12, 0, "Passion Fruit"), #18
    Ingredient(Translation(en="Peach Syrup", es="Jarabe de Durazno", de="Pfirsichsirup", fr="Sirop de Pêche"), Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), 100, 0, 0.35, 45, 0, 1, 12, 11, 0, "Peach"), #19
    Ingredient(Translation(en="Strawberry Purée", es="Puré de Fresa", de="Erdbeerpüree", fr="Purée de Fraise"), Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), 100, 0, 0.40, 50, 0, 1, 12, 10, 0, "Strawberry"), #20
    Ingredient(Translation(en="Pineapple Juice", es="Jugo de Piña", de="Ananassaft", fr="Jus d'Ananas"), Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), 100, 0, 0.30, 60, 0, 2, 15, 13, 0, "Pineapple"), #21
    Ingredient(Translation(en="Taro Powder", es="Polvo de Taro", de="Taro-Pulver", fr="Poudre de Taro"), Translation(en="Taro", es="Taro", de="Taro", fr="Taro"), 100, 0, 0.50, 100, 0, 10, 24, 6, 0, "None"), #22
    Ingredient(Translation(en="Black Tapioca Pearls", es="Perlas de Tapioca Negras", de="Schwarze Tapioka-Perlen", fr="Perles de Tapioca Noires"), Translation(en="Tapioca", es="Tapioca", de="Tapioka", fr="Tapioca"), 100, 0, 0.15, 100, 0, 5, 26, 15, 0, "None"), #23
    Ingredient(Translation(en="Brown Sugar Pearls", es="Perlas de Azúcar Morena", de="Braune Zuckerperlen", fr="Perles de Sucre Brun"), Translation(en="Tapioca", es="Tapioca", de="Tapioka", fr="Tapioca"), 100, 0, 0.20, 110, 0, 5, 28, 18, 0, "None"), #24
    Ingredient(Translation(en="Coffee Jelly", es="Gelatina de Café", de="Kaffee-Gelee", fr="Gelée de Café"), Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), 100, 0, 0.25, 20, 0, 5, 5, 3, 10, "None"), #25
    Ingredient(Translation(en="Honey Jelly", es="Gelatina de Miel", de="Honig-Gelee", fr="Gelée de Miel"), Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), 100, 0, 0.25, 40, 0, 5, 10, 8, 0, "None"), #26
    Ingredient(Translation(en="Lychee Jelly", es="Gelatina de Lichi", de="Litschi-Gelee", fr="Gelée de Litchi"), Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), 100, 0, 0.25, 35, 0, 5, 9, 7, 0, "Lychee"), #27
    Ingredient(Translation(en="Grass Jelly", es="Gelatina de Hierba", de="Gras-Gelee", fr="Gelée d'Herbe"), Translation(en="Jelly", es="Gelatina", de="Gelee", fr="Gelée"), 100, 0, 0.25, 30, 0, 5, 8, 6, 0, "None"), #28
    Ingredient(Translation(en="Red Beans (Sweetened)", es="Frijoles Rojos (Endulzados)", de="Rote Bohnen (Gesüßt)", fr="Haricots Rouges (Sucrés)"), Translation(en="Beans", es="Frijoles", de="Bohnen", fr="Haricots"), 100, 0, 0.20, 120, 0, 5, 24, 12, 0, "None"), #29
    Ingredient(Translation(en="Nata de Coco", es="Nata de Coco", de="Nata de Coco", fr="Nata de Coco"), Translation(en="Coconut", es="Coco", de="Kokosnuss", fr="Noix de Coco"), 100, 0, 0.25, 40, 0, 10, 11, 9, 0, "Tree nuts (Coconut)"), #30
    Ingredient(Translation(en="Oreo Cookies", es="Galletas Oreo", de="Oreo-Kekse", fr="Biscuits Oreo"), Translation(en="Cookies", es="Galletas", de="Kekse", fr="Biscuits"), 100, 0, 0.10, 53, 3, 40, 8, 4, 0, "Wheat; Milk; Soybeans"), #31
    Ingredient(Translation(en="Lemon Juice", es="Jugo de Limón", de="Zitronensaft", fr="Jus de Citron"), Translation(en="Fruit", es="Fruta", de="Frucht", fr="Fruit"), 100, 0, 0.15, 7, 0, 1, 2, 1, 0, "None"), #32
    Ingredient(Translation(en="Salt", es="Sal", de="Salz", fr="Sel"), Translation(en="Seasoning", es="Condimento", de="Gewürz", fr="Assaisonnement"), 100, 0, 0.02, 0, 0, 0, 0, 0, 0, "None"), #33
    Ingredient(Translation(en="Ice Cubes", es="Cubitos de Hielo", de="Eiswürfel", fr="Glaçons"), Translation(en="Ice", es="Hielo", de="Eis", fr="Glace"), 100, 0, 0.01, 0, 0, 0, 0, 0, 0, "None"), #34
    Ingredient(Translation(en="Crushed Ice", es="Hielo Picado", de="Crushed Ice", fr="Glace Pilée"), Translation(en="Ice", es="Hielo", de="Eis", fr="Glace"), 100, 0, 0.01, 0, 0, 0, 0, 0, 0, "None"), #35
]

# of items = 16
items = [
    # Milky Series
    Menu(Translation(en="Classic Pearl Milk Tea", es="Té con Leche y Perlas Clásico", de="Klassischer Perlen-Milchtee", fr="Thé au Lait aux Perles Classique"), Translation(en="Milky Series", es="Serie Láctea", de="Milchserie", fr="Série Laiteuse"), 5.80),
    Menu(Translation(en="Taro Pearl Milk Tea", es="Té con Leche y Perlas de Taro", de="Taro-Perlen-Milchtee", fr="Thé au Lait aux Perles de Taro"), Translation(en="Milky Series", es="Serie Láctea", de="Milchserie", fr="Série Laiteuse"), 6.25),

    # Fresh Brew
    Menu(Translation(en="Classic Tea", es="Té Clásico", de="Klassischer Tee", fr="Thé Classique"), Translation(en="Fresh Brew", es="Infusión Fresca", de="Frischer Aufguss", fr="Infusion Fraîche"), 4.65),
    Menu(Translation(en="Honey Tea", es="Té con Miel", de="Honig-Tee", fr="Thé au Miel"), Translation(en="Fresh Brew", es="Infusión Fresca", de="Frischer Aufguss", fr="Infusion Fraîche"), 4.85),

    # Fruity Beverages
    Menu(Translation(en="Mango Green Tea", es="Té Verde de Mango", de="Mango-Grüntee", fr="Thé Vert à la Mangue"), Translation(en="Fruity Beverage", es="Bebida Afrutada", de="Fruchtiges Getränk", fr="Boisson Fruitée"), 5.80),
    Menu(Translation(en="Passion Chess", es="Ajedrez de Maracuyá", de="Passionsfrucht-Schach", fr="Échecs de Fruit de la Passion"), Translation(en="Fruity Beverage", es="Bebida Afrutada", de="Fruchtiges Getränk", fr="Boisson Fruitée"), 6.25),
    Menu(Translation(en="Peach Tea w/ Honey Jelly", es="Té de Durazno con Gelatina de Miel", de="Pfirsich-Tee mit Honig-Gelee", fr="Thé à la Pêche avec Gelée de Miel"), Translation(en="Fruity Beverage", es="Bebida Afrutada", de="Fruchtiges Getränk", fr="Boisson Fruitée"), 6.25),

    # Non-Caffeinated
    Menu(Translation(en="Tiger Boba", es="Boba Tigre", de="Tiger-Boba", fr="Boba Tigre"), Translation(en="Non-Caffeinated", es="Sin Cafeína", de="Koffeinfrei", fr="Sans Caféine"), 6.50),
    Menu(Translation(en="Halo Halo", es="Halo Halo", de="Halo Halo", fr="Halo Halo"), Translation(en="Non-Caffeinated", es="Sin Cafeína", de="Koffeinfrei", fr="Sans Caféine"), 6.95),

    # New Matcha Series
    Menu(Translation(en="Matcha Pearl Milk Tea", es="Té con Leche y Perlas de Matcha", de="Matcha-Perlen-Milchtee", fr="Thé au Lait aux Perles de Matcha"), Translation(en="New Matcha Series", es="Nueva Serie Matcha", de="Neue Matcha-Serie", fr="Nouvelle Série Matcha"), 6.50),
    Menu(Translation(en="Strawberry Matcha Fresh Milk", es="Leche Fresca de Matcha con Fresa", de="Erdbeer-Matcha-Frischmilch", fr="Lait Frais au Matcha et à la Fraise"), Translation(en="New Matcha Series", es="Nueva Serie Matcha", de="Neue Matcha-Serie", fr="Nouvelle Série Matcha"), 6.50),
    Menu(Translation(en="Mango Matcha Fresh Milk", es="Leche Fresca de Matcha con Mango", de="Mango-Matcha-Frischmilch", fr="Lait Frais au Matcha et à la Mangue"), Translation(en="New Matcha Series", es="Nueva Serie Matcha", de="Neue Matcha-Serie", fr="Nouvelle Série Matcha"), 6.50),

    # Ice-Blended
    Menu(Translation(en="Oreo w/ Pearl", es="Oreo con Perlas", de="Oreo mit Perlen", fr="Oreo aux Perles"), Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), 6.75),
    Menu(Translation(en="Coffee w/ Ice Cream", es="Café con Helado", de="Kaffee mit Eiscreme", fr="Café à la Crème Glacée"), Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), 6.75),
    Menu(Translation(en="Strawberry w/ Lychee Jelly & Ice Cream", es="Fresa con Gelatina de Lichi y Helado", de="Erdbeere mit Litschi-Gelee und Eiscreme", fr="Fraise avec Gelée de Litchi et Crème Glacée"), Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), 6.75),
    Menu(Translation(en="Lava Flow", es="Flujo de Lava", de="Lavafluss", fr="Flux de Lave"), Translation(en="Ice-Blended", es="Mezclado con Hielo", de="Mit Eis Gemischt", fr="Mélangé avec Glace"), 6.95),
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
