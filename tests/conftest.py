import pytest
from selene import browser, command


@pytest.fixture(params=['1200x1800', '600x900', '320x600'])
def browser_setting_skip(request):
    browser.config.base_url = "https://github.com"
    window_width, window_height = map(int, request.param.split('x'))
    browser.config.window_height = window_height
    browser.config.window_width = window_width

    if request.param == '1200x1800':
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()


@pytest.fixture(params=['1200x1800', '600x900', '320x600'])
def browser_setting_param(request):
    browser.config.base_url = "https://github.com"
    window_width, window_height = map(int, request.param.split('x'))
    browser.config.window_height = window_height
    browser.config.window_width = window_width

    yield
    browser.quit()


@pytest.fixture(params=['1200x1200', '1500x1200', '1800x1200'])
def browser_setting_desktop(request):
    browser.config.base_url = "https://github.com"
    window_width, window_height = map(int, request.param.split('x'))
    browser.config.window_height = window_height
    browser.config.window_width = window_width

    yield
    browser.quit()


@pytest.fixture(params=['900x600', '600x600', '350x600'])
def browser_setting_mobile(request):
    browser.config.base_url = "https://github.com"
    window_width, window_height = map(int, request.param.split('x'))
    browser.config.window_height = window_height
    browser.config.window_width = window_width

    yield
    browser.quit()