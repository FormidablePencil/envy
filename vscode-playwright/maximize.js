const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true }); // Set headless to true
    const context = await browser.newContext({
        viewport: { width: 1920, height: 1080 } // Set a large viewport size
    });
    const page = await context.newPage();

    // Replace with the URL of your VSCode instance
    await page.goto('http://localhost:8080');

    // Keep the browser open
    await page.waitForTimeout(10000);
    await browser.close();
})();