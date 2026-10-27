const { chromium } = require('@playwright/test');
const fs = require('fs');

(async () => {
  console.log('Launching browser...');
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();

  // Desktop Page
  const desktopPage = await context.newPage();
  await desktopPage.setViewportSize({ width: 1440, height: 900 });
  console.log('Navigating to https://robixx-128.webflow.io/ (desktop)...');
  await desktopPage.goto('https://robixx-128.webflow.io/', { waitUntil: 'networkidle' });
  await desktopPage.screenshot({ path: 'docs/screenshots/desktop-full.png', fullPage: true });
  await desktopPage.screenshot({ path: 'docs/screenshots/desktop-hero.png' });

  // Check interactive state: hover on first CTA or nav
  const navLink = desktopPage.locator('a').first();
  if (await navLink.isVisible()) {
    await navLink.hover();
    await desktopPage.screenshot({ path: 'docs/screenshots/desktop-hover.png' });
  }

  // Mobile Page
  const mobilePage = await context.newPage();
  await mobilePage.setViewportSize({ width: 390, height: 844 });
  console.log('Navigating to https://robixx-128.webflow.io/ (mobile)...');
  await mobilePage.goto('https://robixx-128.webflow.io/', { waitUntil: 'networkidle' });
  await mobilePage.screenshot({ path: 'docs/screenshots/mobile-full.png', fullPage: true });
  await mobilePage.screenshot({ path: 'docs/screenshots/mobile-hero.png' });

  // Try opening mobile nav menu if button exists
  const menuBtn = mobilePage.locator('.w-nav-button, [aria-label*="menu" i], button:has-text("Menu"), .menu-button').first();
  if (await menuBtn.isVisible()) {
    await menuBtn.click();
    await mobilePage.waitForTimeout(500);
    await mobilePage.screenshot({ path: 'docs/screenshots/mobile-menu-open.png' });
  }

  // Inspect page details
  const details = await desktopPage.evaluate(() => {
    const getStyles = (el) => {
      if (!el) return null;
      const cs = window.getComputedStyle(el);
      return {
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        color: cs.color,
        backgroundColor: cs.backgroundColor,
      };
    };

    const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => ({
      tag: h.tagName,
      text: h.innerText.trim(),
      styles: getStyles(h)
    }));

    const links = Array.from(document.querySelectorAll('a')).map(a => ({
      text: a.innerText.trim(),
      href: a.href
    })).filter(l => l.text);

    const sections = Array.from(document.querySelectorAll('section, div[class*="section"]')).map(s => ({
      class: s.className,
      id: s.id,
      textPreview: s.innerText.substring(0, 100).replace(/\s+/g, ' ')
    }));

    const bodyStyles = getStyles(document.body);

    return { headings, links, sections, bodyStyles };
  });

  fs.writeFileSync('docs/screenshots/page-data.json', JSON.stringify(details, null, 2));
  console.log('Extraction complete!');

  await browser.close();
})();
