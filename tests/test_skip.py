import pytest
from selene import browser, command


def test_github_desktop(browser_setting_skip):
    if browser_setting_skip == 'mobile':
        pytest.skip('Пропускаем мобильные тесты')
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_setting_skip):
    if browser_setting_skip == 'desktop':
        pytest.skip('Пропускаем тесты для десктопа')
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').perform(command.js.scroll_into_view).click()
