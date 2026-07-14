# demo-buggy-inventory

A small Python + pytest project used as a **test fixture** for the AutoReviewer agent.

## Purpose
This repo intentionally contains **5 seeded bugs** in `src/inventory.py`, each with a corresponding test in `tests/test_inventory.py` that currently fails. AutoReviewer's job is to:
1. Detect these issues via static review
2. Run the test suite and observe the real failures
3. Diagnose the root cause of each
4. Generate and apply a fix
5. Re-run tests to verify the fix actually works

**Do not fix the bugs manually** — this repo exists specifically so the agent has real, verifiable problems to solve.

## Current known state (baseline)
Running `pytest tests/ -v` right now should show:
- **5 failed, 3 passed**

The 5 failing tests are:
1. `test_apply_discount_basic` — discount math bug
2. `test_needs_restock_at_threshold` — off-by-one comparison bug
3. `test_average_rating_empty_list` — missing empty-list guard (crashes)
4. `test_add_item_to_cart_is_isolated_per_customer` — mutable default argument bug
5. `test_calculate_total_includes_tax` — tax calculation forgotten entirely

## Setup
```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Structure
```
demo-buggy-inventory/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/
│   ├── __init__.py
│   └── inventory.py       # contains the 5 seeded bugs
└── tests/
    ├── __init__.py
    └── test_inventory.py   # correct expected behavior — do not edit
```
