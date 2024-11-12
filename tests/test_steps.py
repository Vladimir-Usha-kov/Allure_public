import allure
import pytest
from selene import browser, have, be, command, by
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('#query-builder-test').type('eroshenkoam/allure-example').submit()

    with allure.step('Переходим по ссылке в репозиторий '):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открывает таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text("#76")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number("76")



@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('#query-builder-test').type(repo).submit()

@allure.step('Переходим по ссылке в репозиторий {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step('Открывает таб Issues')
def open_issue_tab():
    s('#issues-tab').click()

@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text("#" + number)).should(be.visible)


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ushakov")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decoration_labels():
    pass