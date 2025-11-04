from datetime import datetime, timedelta
from classtypes import *
import menu
import csv
import random
from faker import Faker
import uuid

fake = Faker()

WEEKS = 39

employees: list[Employee] = [
    Employee(id=uuid.uuid4(), name=fake.name(), email=fake.email(), role=Role.STAFF) for _ in range(1, 6)
]

employees[0].role = Role.MANAGER

# export a csv of the menu items, recipes, and ingredients
def export_menu_csv():
    with open("csv/menu_items.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "imageUrl", "archived"])
        for item in menu.items:
            writer.writerow([item.id, item.name, item.category, item.price, item.image_url, item.archived])

    with open("csv/recipes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["menu_item_id", "ingredient_id", "quantity"])
        for recipe in menu.recipes:
            writer.writerow([recipe.menu_item_id, recipe.ingredient_id, recipe.quantity])

    with open("csv/ingredients.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "current_stock", "order_stock", "unit_price"])
        for ingredient in menu.ingredients:
            writer.writerow([ingredient.id, ingredient.name, ingredient.category, ingredient.current_stock, ingredient.order_stock, ingredient.unit_price])

    with open("csv/nutrition_info.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ingredient_id", "calories", "fat_g", "sodium_g", "carbs_g", "sugar_g", "caffiene_mg"])
        for nutrition in menu.nutrition:
            writer.writerow([nutrition.ingredient_id, nutrition.calories, nutrition.fat_g, nutrition.sodium_g, nutrition.carbs_g, nutrition.sugar_g, nutrition.caffiene_mg])

    with open("csv/allergens.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ingredient_id", "allergen"])
        for allergen in menu.allergens:
            writer.writerow([allergen.ingredient_id, allergen.allergen])

def export_sales_csv(customers: list[Customer], orders: list[Order], order_contents: list[OrderContent]):
    with open("csv/customers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name"])
        for customer in customers:
            writer.writerow([customer.id, customer.name])

    with open("csv/orders.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "customer_id", "employee_id", "subtotal", "tax", "total", "date", "payment_method", "item_quantity"])
        for order in orders:
            writer.writerow([order.id, order.customer_id, order.employee_id, order.subtotal, order.tax, order.total, order.date, order.payment_method.value, order.item_quantity])

    with open("csv/order_contents.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "menu_item_id", "ingredient_id", "order_entry_id"])
        for content in order_contents:
            writer.writerow([content.order_id, content.menu_item_id, content.ingredient_id, content.order_entry_id])

def export_employees_csv():
    with open("csv/employees.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email", "role", "archived"])
        for employee in employees:
            writer.writerow([employee.id, employee.name, employee.email, employee.role.value, False])

def generateRandomOrder(clock: datetime):
    global next_order_entry_id

    orderItems: list[OrderContent] = []
    price = 0.0

    count = 0

    order_id = uuid.uuid4()

    for i in range(random.randint(1, 6)):
        menu_item = random.choice(menu.items)
        count += 1

        ingredient_ids = [i.ingredient_id for i in menu.recipes if i.menu_item_id == menu_item.id]
        ingredients = [i for i in menu.ingredients if i.id in ingredient_ids]

        # 30% chance to remove an ingredient
        if random.random() < 0.3 and len(ingredients) > 1:
            ingredients.remove(random.choice(ingredients))

        price += menu_item.price

        for i in ingredients:
            orderItems.append(OrderContent(order_id=order_id, menu_item_id=menu_item.id, ingredient_id=i.id, order_entry_id=uuid.uuid4()))

    # round to 2 decimal places
    price = round(price, 2)
    tax = round(price * 0.06, 2)
    total = round(price + tax, 2)

    payment = random.choices([PaymentMethod.CASH, PaymentMethod.CREDIT])[0]
    cid = uuid.uuid4()
    return (
        Customer(id=cid, name=fake.name()),
        Order(id=order_id, customer_id=cid, employee_id=eid, subtotal=price, tax=tax, total=total, date=clock, payment_method=payment, item_quantity=count),
        orderItems
    )


if __name__ == "__main__":
    export_menu_csv()

    # get days going back 39 weeks
    dates: list[datetime] = []
    now = datetime.now()
    for i in range(WEEKS * 7):
        dates.append(now - timedelta(days=i))

    customers: list[Customer] = []
    orders: list[Order] = []
    order_contents: list[OrderContent] = []

    peakDays: list[datetime] = []
    for d in dates:
        if random.random() < 0.02:
            num_orders = random.randint(300, 400)
            peakDays.append(d)
        else:
            num_orders = random.randint(100, 175)

        for _ in range(num_orders):
            eid = random.choice(employees).id
            customer, order, order_items = generateRandomOrder(d + timedelta(hours=random.randint(9, 20), minutes=random.randint(0, 59)))
            customers.append(customer)
            orders.append(order)
            order_contents.extend(order_items)

    totalSales = sum([o.total for o in orders])
    print(f"Generated {len(orders)} orders with total sales of ${totalSales:.2f}")
    print(f"Average sales per week: ${totalSales / WEEKS:.2f}")
    print(f"Average sales per day: ${totalSales / (WEEKS * 7):.2f}")
    print(f"Peak days: {len(peakDays)}")
    for d in peakDays:
        print(f" - {d.strftime('%Y-%m-%d')}")

    export_sales_csv(customers, orders, order_contents)

    employees.append(Employee(id=uuid.uuid4(), name="manager", email="manager@example.com", role=Role.MANAGER))
    employees.append(Employee(id=uuid.uuid4(), name="staff", email="staff@example.com", role=Role.STAFF))
    export_employees_csv()
