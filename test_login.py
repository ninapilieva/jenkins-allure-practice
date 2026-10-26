
import allure
from playwright.sync_api import Page, expect

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"


@allure.title("Successful login with valid credentials")
def test_successful_login(page: Page):
    with allure.step("Open the login page"):
        page.goto(LOGIN_URL)

    with allure.step("Enter valid credentials"):
        page.locator("#username").fill("student")
        page.locator("#password").fill("Password123")

    with allure.step("Submit the login form"):
        page.locator("#submit").click()

    with allure.step("Verify successful login"):
        assert "/logged-in-successfully/" in page.url
        expect(page.get_by_text("Congratulations")).to_be_visible()
        expect(page.get_by_role("link", name="Log out")).to_be_visible()


@allure.title("Login fails with an invalid username")
def test_invalid_username(page: Page):
    with allure.step("Open the login page"):
        page.goto(LOGIN_URL)

    with allure.step("Enter an invalid username"):
        page.locator("#username").fill("student")
        page.locator("#password").fill("Password123")

    with allure.step("Submit the login form"):
        page.locator("#submit").click()

    with allure.step("Verify the error message"):
        expect(page.locator("#error")).to_have_text(
            "Your username is invalid!"
        )
