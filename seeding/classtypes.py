from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID
import uuid

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
    id: UUID = field(default_factory=uuid.uuid4)

@dataclass
class Menu:
    name: str
    category: str
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
    name: Optional[str]
    category: str
    current_stock: int
    order_stock: int
    unit_price: float
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
