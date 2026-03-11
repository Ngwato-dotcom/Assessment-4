from pages.base_page import BasePage

class ProductPage(BasePage):
    def add_camera_to_cart(self):
        self.page.goto("https://demowebshop.tricentis.com/digital-slr-camera")


        self.page.wait_for_selector("h1:has-text('Digital SLR Camera')")


        if self.page.locator("select").count() > 0:
            dropdown = self.page.locator("select").first
            dropdown.select_option(index=0)

        self.page.click("#add-to-cart-button-18")

        self.page.wait_for_selector("span.cart-qty", timeout=10000)

        return self.page.is_visible("text=Shopping cart")
