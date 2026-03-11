from pages.base_page import BasePage

class CartPage(BasePage):
    def validate_cart(self):
        assert self.page.is_visible("text=Digital SLR Camera")
        assert self.page.is_visible("text=1")
        return True
