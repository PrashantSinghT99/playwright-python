#module,function,class
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        print("within browser start")
        yield browser
        print("within browser end")
        browser.close()
        
@pytest.fixture(scope="function")
def page(browser):
    page=browser.new_page()
    print("within page start")
    yield page
    print("within page end")
    page.close()
    
def test_google(page):
    print("within google start")
    page.goto("https://google.com")
    assert "Google" == page.title()
    
def test_portfolio(page):
    print("within portfolio start")
    page.goto("https://github-portfolio-pst99.vercel.app/")
    assert "My Portfolio" == page.title()
    
    