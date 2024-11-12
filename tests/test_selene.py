import pytest
from selene import browser, have, be, command, by
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com')

    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('#query-builder-test').type('eroshenkoam/allure-example').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()

    s(by.partial_text("#76")).should(be.visible)
