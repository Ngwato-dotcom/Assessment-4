import uuid
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(page, test_data,):
    # Register & login
    reg_page = RegistrationPage(page)
    reg_page.open()
    email = f"user_{uuid.uuid4()}@test.com"
    reg_page.register_user(email, "Tosca1234!")
    reg_page.logout()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(email, "Tosca1234!")

    # Add product & checkout
    product_page = ProductPage(page)
    product_page.open()
    product_page.add_camera_to_cart()

    cart_page = CartPage(page)
    assert cart_page.validate_cart()

    checkout_page = CheckoutPage(page)
    assert checkout_page.complete_checkout(test_data)

    print("Product Checkout Successful")

