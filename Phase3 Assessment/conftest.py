import uuid

import pytest
from playwright.sync_api import sync_playwright

from pages.registration_page import RegistrationPage
@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    browser.close()

@pytest.fixture
def test_data():
    return {
        "country": "Austria",
        "city": "Vienna",
        "address": "Vienna Street",
        "zip": "1234",
        "phone": "001122334455",
        "card_type": "Visa",
        "cardholder": "Barbara Gordon",
        "card_number": "4485564059489345",
        "expiry_month": "04",
        "expiry_year": "2026",
        "code": "123"
    }

@pytest.fixture
def credentials(request):
    if request.param == "registered_user":
        return request.getfixturevalue("registered_user")
    return request.param


@pytest.fixture
def registered_user(page):
    reg_page = RegistrationPage(page)
    reg_page.open()
    email = f"user_{uuid.uuid4()}@gmail.com"
    password = "Tosca1234!"
    reg_page.register_user(email, password)
    reg_page.logout()
    return email, password
