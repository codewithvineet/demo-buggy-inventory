"""
inventory.py — small retail-inventory utility module.
This module intentionally contains 5 bugs (seeded on purpose) used to
test the AutoReviewer agent's ability to detect, diagnose, and fix them.
DO NOT fix these manually — they exist for the agent to find.
"""


def apply_discount(price: float, percent: float) -> float:
    """
    Apply a percentage discount to a price.
    Example: apply_discount(100, 20) should return 80.0 (20% off).

    BUG (easy): percent is not converted to a fraction before subtracting,
    so a 20% discount wrongly removes 20 rupees worth of "percent units"
    instead of 20% of the price.
    """
    return price - percent  # BUG: should be price - (price * percent / 100)


def needs_restock(current_stock: int, threshold: int) -> bool:
    print("Checking stock level")  # leftover debug statement
    return current_stock <= threshold


def average_rating(ratings: list) -> float:
    """
    Return the average of a list of product ratings.
    Example: average_rating([]) should return 0.0 for a product with no reviews yet.

    BUG (medium): no check for an empty list, causing a ZeroDivisionError
    crash instead of gracefully returning 0.0.
    """
    return sum(ratings) / len(ratings)  # BUG: missing empty-list guard


def add_item_to_cart(item: str, cart: list = []) -> list:
    """
    Add an item to a shopping cart list and return the cart.
    Example: calling this fresh for a new customer should start with an empty cart.

    BUG (medium-hard): mutable default argument. Because `cart=[]` is created
    ONCE when the function is defined (not each call), every customer who
    doesn't pass their own cart ends up sharing and appending to the SAME list.
    """
    cart.append(item)  # BUG: default mutable argument causes shared state
    return cart


def calculate_total(prices: list, tax_rate: float) -> float:
    """
    Calculate the total cost of a list of item prices including tax.
    Example: calculate_total([100, 200], 0.10) should return 330.0 (10% tax added).

    BUG (hard): the function forgets to actually apply the tax rate at all —
    it just returns the sum of prices, silently ignoring the tax_rate parameter.
    """
    return sum(prices)  # BUG: should be sum(prices) * (1 + tax_rate)
