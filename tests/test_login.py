import os
from dotenv import load_dotenv

from pages.login_page import LoginPage
from utils.test_data_reader import load_test_data


load_dotenv()

test_data = load_test_data()


def test_valid_login(page, base_url):

    username = os.getenv("SAUCE_USERNAME")
    password = os.getenv("SAUCE_PASSWORD")

    login_page = LoginPage(page)

    page.goto(base_url)
    login_page.login(username, password)

    assert "inventory.html" in page.url


def test_invalid_login(page, base_url):

    username = test_data["invalid_login"]["username"]
    password = test_data["invalid_login"]["password"]

    login_page = LoginPage(page)

    page.goto(base_url)
    login_page.login(username, password)

    assert login_page.is_error_message_visible()