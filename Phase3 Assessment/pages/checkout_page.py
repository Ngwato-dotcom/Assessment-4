from pages.base_page import BasePage
from playwright.sync_api import Page

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def complete_checkout(self, test_data):

        self.page.click("text=Shopping cart")
        self.page.click("input[name='termsofservice']")
        self.page.click("button#checkout")


        self.page.wait_for_selector("#BillingNewAddress_FirstName")
        self.page.fill("#BillingNewAddress_FirstName", "Test")
        self.page.fill("#BillingNewAddress_LastName", "User")
        self.page.fill("#BillingNewAddress_Email", test_data.get("email", "test@test.com"))
        self.page.select_option("#BillingNewAddress_CountryId", label=test_data["country"])
        self.page.fill("#BillingNewAddress_City", test_data["city"])
        self.page.fill("#BillingNewAddress_Address1", test_data["address"])
        self.page.fill("#BillingNewAddress_ZipPostalCode", test_data["zip"])
        self.page.fill("#BillingNewAddress_PhoneNumber", test_data["phone"])
        self.page.locator("#billing-buttons-container input.button-1.new-address-next-step-button").click(
            no_wait_after=True)


        self.page.wait_for_selector("select#shipping-address-select")
        self.page.select_option("select#shipping-address-select", index=0)
        self.page.locator("#shipping-buttons-container input.button-1.new-address-next-step-button").click(
            no_wait_after=True)

        self.page.wait_for_selector("input[name='shippingoption']")
        self.page.check("input[value='Ground___Shipping.FixedRate']")
        self.page.locator("#shipping-method-buttons-container input.button-1.shipping-method-next-step-button").click(
            no_wait_after=True)


        self.page.locator("input.button-1.payment-method-next-step-button").click(no_wait_after=True)


        self.page.locator("input.button-1.payment-info-next-step-button").click(no_wait_after=True)



        self.page.locator("#confirm-order-buttons-container input.button-1.confirm-order-next-step-button").click(
            no_wait_after=True)


        self.page.wait_for_selector("div.section.order-completed", timeout=15000)

        return self.page.is_visible("text=Your order has been successfully processed!")

