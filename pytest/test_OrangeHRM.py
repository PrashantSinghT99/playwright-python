from playwright.sync_api import Page
import pytest



def test_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title()=="OrangeHRM"