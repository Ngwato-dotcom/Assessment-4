# pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage):
    def open(self):
        self.page.goto("https://demowebshop.tricentis.com/login")

    def login(self, email, password):
        self.page.fill("input#Email", email)
        self.page.fill("input#Password", password)
        self.page.click("input.button-1.login-button")
