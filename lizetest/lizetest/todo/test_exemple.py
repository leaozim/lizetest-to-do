
import re
from playwright.sync_api import Page, expect

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        yield browser
        browser.close()

def test_example_page(browser):
    page = browser.new_page()
    page.goto('http://localhost:8000/')
    page.wait_for_timeout(1000)
    # Realize asserções e ações adicionais no teste
    assert page.title() == 'To-do List'

def test_login_page(browser):
    context = browser.new_context()

    page = context.new_page()

    response = page.goto('http://localhost:8000/accounts/login/')

    page.fill('input[name="username"]', 'lade')
    page.fill('input[name="password"]', 'caneta@10')

    page.click('button[type="submit"]')
    assert response.status == 200
        
    page.wait_for_url("http://localhost:8000/", timeout=1000) 

        
        
def test_login_page_error(browser):
    context = browser.new_context()

    page = context.new_page()
    page.goto('http://localhost:8000/accounts/login/')
    page.wait_for_timeout(1000)

    
    page.fill('input[name="username"]', 'ladee')
    page.fill('input[name="password"]', 'caneta@10')

    page.click('button[type="submit"]')

    try:
        page.wait_for_url('http://localhost:8000/accounts/login/', timeout=5000) 
    except TimeoutError:
        assert False, "Tempo limite excedido ao aguardar o redirecionamento após o login"
        