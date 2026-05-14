import pytest
from product import Product

@pytest.fixture
def product():
    return Product("Smartfon", 100.0, 10)

def test_is_available(product):
    assert product.is_available() == True

def test_is_not_available():
    empty_product = Product("Myszka", 50.0, 0)
    assert empty_product.is_available() == False

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (20, 30),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity

def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(100)

# --- ZADANIE DODATKOWE ---
@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price

@pytest.mark.parametrize("invalid_percent", [-10, 150, 101])
def test_apply_discount_invalid_raises(product, invalid_percent):
    with pytest.raises(ValueError):
        product.apply_discount(invalid_percent)
