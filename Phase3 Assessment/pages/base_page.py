class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, base_url="https://demowebshop.tricentis.com/"):
        self.page.goto(base_url)