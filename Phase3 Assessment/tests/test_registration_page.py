import pytest, uuid
from playwright.sync_api import Playwright, expect

from pages.registration_page import RegistrationPage

def test_register_user(page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    email = f"user_{uuid.uuid4()}@gmail.com"
    assert registration_page.register_user(email, "Tosca1234!")
    assert registration_page.logout()
    print(email + " is registered")

