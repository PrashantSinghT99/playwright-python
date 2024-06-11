import asyncio
from playwright.async_api import async_playwright


text_alert=[]

async def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    await dialog.accept()


async def main():
   async with async_playwright() as p:
        browser= await p.chromium.launch(headless=False)
        context= await browser.new_context()
        await context.tracing.start(screenshots=True,snapshots=True,sources=True)
        page=await context.new_page()

        await page.set_viewport_size({"width":1800,"height":1200})
        await page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        #page.on("dialog",lambda dialog: dialog.accept())
        #dialogd.dismiss() 
        #dialog.message
        page.on("dialog",handle_dialog)
        await page.locator('//button[text()="Click for JS Alert"]').click()
        await page.wait_for_timeout(2000)
        print(text_alert[0])
        await context.tracing.stop(path="logs/dialogs.zip")
        await browser.close()

asyncio.run(main())
    