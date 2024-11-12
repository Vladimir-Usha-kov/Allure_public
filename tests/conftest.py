import pytest
from _pytest.fixtures import fixture
from selene import browser

@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080