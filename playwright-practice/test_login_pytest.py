import pytest
from playwright.sync_api import Page


class LoginPage:
    """Page Object pentru pagina de login."""

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")


class SecureAreaPage:
    """Page Object pentru pagina afișată după login reușit."""

    def __init__(self, page: Page):
        self.page = page

    def get_flash_message(self):
        return self.page.inner_text(".flash")


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "secure" in message
    assert "invalid" not in message


def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wronguser", "wrongpassword")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "invalid" in message
