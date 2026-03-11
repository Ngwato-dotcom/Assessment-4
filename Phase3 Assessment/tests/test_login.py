import uuid
import pytest
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage




@pytest.mark.parametrize(
    "credentials, expected_locator",
    [

        pytest.param(
            "registered_user",
            "a[href='/logout']",
            id="valid_login"
        ),
        pytest.param(
            ("wrong_user@test.com", "WrongPassword123!"),
            "div.validation-summary-errors",
            marks=pytest.mark.xfail,
            id="invalid_login"
        )
    ],
    indirect=["credentials"]
)
def test_login(page,registered_user, credentials, expected_locator):
    email, password = credentials

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(email, password)

    assert page.is_visible(expected_locator)