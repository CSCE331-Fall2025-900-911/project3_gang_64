from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID
import uuid


@dataclass
class Translation:
    en: str
    es: str
    de: str
    fr: str
    
class Role(Enum):
    MANAGER = "manager"
    STAFF = "staff"

class PaymentMethod(Enum):
    CASH = "cash"
    CREDIT = "credit"

@dataclass
class Employee:
    name: str
    email: str
    role: Role
    archived: bool = False
    id: UUID = field(default_factory=uuid.uuid4)

@dataclass
class Customer:
    name: Optional[str] = None
    email: Optional[str] = None
    id: UUID = field(default_factory=uuid.uuid4)

@dataclass
class Menu:
    name: Translation
    category: Translation
    price: float
    image_url: Optional[str] = None
    archived: bool = False
    id: UUID = field(default_factory=uuid.uuid4)

@dataclass
class Order:
    customer_id: UUID
    employee_id: Optional[UUID]
    subtotal: float
    tax: float
    total: float
    date: datetime
    payment_method: PaymentMethod
    item_quantity: int = 0
    id: UUID = field(default_factory=uuid.uuid4)

@dataclass
class Ingredient:
    name: Translation
    category: Translation
    current_stock: int
    order_stock: int
    unit_price: float
    topping: bool = False
    ice: bool = False
    calories: int = 0
    fat_g: int = 0
    sodium_g: int = 0
    carbs_g: int = 0
    sugar_g: int = 0
    caffiene_mg: int = 0
    allergens: str = "None"
    id: UUID = field(default_factory=uuid.uuid4)

@dataclass
class Recipe:
    menu_item_id: UUID
    ingredient_id: UUID
    quantity: int

@dataclass
class OrderContent:
    order_id: UUID
    menu_item_id: UUID
    ingredient_id: UUID
    order_entry_id: UUID


@dataclass
class NutritionInfo:
    ingredient_id: UUID
    calories: int
    fat_g: int
    sodium_g: int
    carbs_g: int
    sugar_g: int
    caffiene_mg: int

@dataclass
class AllergenInfo:
    ingredient_id: UUID
    allergen: str

