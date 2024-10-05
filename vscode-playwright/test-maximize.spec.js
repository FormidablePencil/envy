const { test, expect } = require('@playwright/test');

test('Get left panel styles', async ({ page }) => {
    await page.goto('http://localhost:8080');

    // Wait for the left side panel to load with a longer timeout
    await page.waitForSelector('.left-panel-selector', { timeout: 60000 }); // 60 seconds timeout

    // Get the styles of the left side panel
    const styles = await page.evaluate(() => {
        const element = document.querySelector('.left-panel-selector'); // Replace with the actual selector
        return window.getComputedStyle(element).cssText;
    });

    console.log('Left Panel Styles:', styles);
});