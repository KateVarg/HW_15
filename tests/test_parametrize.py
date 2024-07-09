import pytest
from selene import browser, command


@pytest.mark.parametrize('browser_setting_param', ['1100x900', '1950x900'], indirect=True)
def test_github_desktop(browser_setting_param):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_setting_param', ['650x900', '400x900'], indirect=True)
def test_github_mobile(browser_setting_param):
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').perform(command.js.scroll_into_view).click()
