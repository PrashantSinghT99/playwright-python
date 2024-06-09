import asyncio
from playwright.async_api import async_playwright,expect

async def main():
   async with async_playwright() as p:
    browser= await p.chromium.launch(headless=False)
    context= await browser.new_context()
    await context.tracing.start(screenshots=True,snapshots=True,sources=True)
    page=await context.new_page()
    
    await page.set_viewport_size({"width":1800,"height":1200})
    await page.goto("https://demoqa.com/checkbox")

    await page.check("//*[@id='tree-node']/ol/li/span/label")
    await page.screenshot(path="screenshots/checkboxes.png")

    await page.is_checked("//*[@id='tree-node']/ol/li/span/label") is True
    await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")

    await context.tracing.stop(path="logs/checkbox.zip")
    
    await browser.close()

asyncio.run(main())