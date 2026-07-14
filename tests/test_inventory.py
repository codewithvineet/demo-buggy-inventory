"""
test_inventory.py — tests for inventory.py

These tests encode the CORRECT expected behavior. With the seeded bugs
in inventory.py, several of these tests should currently FAIL.
This is intentional — AutoReviewer's job is to make all of them pass
by diagnosing and fixing the source code (never edit the tests themselves).
"""

import pytest
from src.inventory import (
    apply_discount,
    needs_restock,
    average_rating,
    add_item_to_cart,
    calculate_total,
)


def test_apply_discount_basic():
    # 20% off a 50-rupee item should be 40.0, not 30.0
    assert apply_discount(50, 20) == 40.0


def test_apply_discount_zero_percent():
    assert apply_discount(50, 0) == 50.0


def test_needs_restock_at_threshold():
    # stock exactly at the threshold should trigger a restock
    assert needs_restock(5, 5) is True


def test_needs_restock_above_threshold():
    assert needs_restock(10, 5) is False


def test_average_rating_normal_case():
    assert average_rating([4, 5, 3]) == pytest.approx(4.0)


def test_average_rating_empty_list():
    # a brand-new product with no reviews yet should show 0.0, not crash
    assert average_rating([]) == 0.0


def test_add_item_to_cart_is_isolated_per_customer():
    # two different customers' carts should NOT share state when neither
    # customer passes their own cart list explicitly
    customer_a_cart = add_item_to_cart("apple")
    customer_b_cart = add_item_to_cart("banana")
    assert customer_a_cart == ["apple"]
    assert customer_b_cart == ["banana"]


def test_calculate_total_includes_tax():
    assert calculate_total([100, 200], 0.10) == pytest.approx(330.0)
