#module,function,class
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def browser(request):
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        # context = browser.new_context()
        
        # # Enable tracing for the context
        # context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # request.cls.context = context
        request.cls.browser=browser  # Attach the browser instance to the test class
        yield browser
        browser.close()

# Define a fixture with function-level scope      
@pytest.fixture(scope="function")
def page(browser):
    page=browser.new_page()
    print("within page start")
    yield page
    print("within page end")
    page.close()
    
    
# Use the 'browser' fixture for the following test class
@pytest.mark.usefixtures("browser")
class Test_titleClass():
    def test_google(self,page):
        print("within google start")
        page.goto("https://google.com")
        assert "Google" == page.title()
        
    def test_portfolio(self,page):
        print("within portfolio start")
        page.goto("https://github-portfolio-pst99.vercel.app/")
        assert "My Portfolio" == page.title()
        
    