from IPython.core import page


class RegistrationPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://demowebshop.tricentis.com/")

    def register_user(self, email, password):
        self.page.click("text=Register")
        self.page.check("#gender-male")
        self.page.fill("#FirstName", "Ngwato")
        self.page.fill("#LastName", "Shoes")
        self.page.fill("#Email", email)
        self.page.fill("#Password", password)
        self.page.fill("#ConfirmPassword", password)
        self.page.click("input[value='Register']")
        return self.page.is_visible("text=Your registration completed")

    def logout(self):
        self.page.click("text=Log out")
        return self.page.is_visible("text=Register")

