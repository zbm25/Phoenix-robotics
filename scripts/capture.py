import json
import os
import time
from playwright.sync_api import sync_playwright

def run():
    os.makedirs("docs/screenshots", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Desktop
        desktop_page = context.new_page()
        desktop_page.set_viewport_size({"width": 1440, "height": 900})
        print("Navigating desktop (1440px)...")
        desktop_page.goto("https://robixx-128.webflow.io/", wait_until="networkidle")
        time.sleep(1)

        desktop_page.screenshot(path="docs/screenshots/desktop-hero.png")
        desktop_page.screenshot(path="docs/screenshots/desktop-full.png", full_page=True)

        # Hover on first nav link or CTA button
        try:
            cta = desktop_page.locator("a, button").first
            cta.hover()
            desktop_page.screenshot(path="docs/screenshots/desktop-hover.png")
        except Exception as e:
            print("Hover error:", e)

        # Mobile
        mobile_page = context.new_page()
        mobile_page.set_viewport_size({"width": 390, "height": 844})
        print("Navigating mobile (390px)...")
        mobile_page.goto("https://robixx-128.webflow.io/", wait_until="networkidle")
        time.sleep(1)

        mobile_page.screenshot(path="docs/screenshots/mobile-hero.png")
        mobile_page.screenshot(path="docs/screenshots/mobile-full.png", full_page=True)

        # Try clicking nav menu button
        try:
            menu_btn = mobile_page.locator(".w-nav-button, button, [aria-label*='menu' i]").first
            if menu_btn.is_visible():
                menu_btn.click()
                time.sleep(0.5)
                mobile_page.screenshot(path="docs/screenshots/mobile-menu-open.png")
        except Exception as e:
            print("Mobile menu error:", e)

        # Detailed DOM and CSS inspection on desktop
        inspection = desktop_page.evaluate("""() => {
            const getStyles = (el) => {
                if (!el) return null;
                const cs = window.getComputedStyle(el);
                return {
                    fontFamily: cs.fontFamily,
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight,
                    lineHeight: cs.lineHeight,
                    color: cs.color,
                    backgroundColor: cs.backgroundColor,
                    borderColor: cs.borderColor,
                    borderRadius: cs.borderRadius,
                    padding: cs.padding,
                    margin: cs.margin,
                    maxWidth: cs.maxWidth
                };
            };

            const headings = Array.from(document.querySelectorAll('h1, h2, h3, h4, .heading, [class*="heading"]')).map(h => ({
                tag: h.tagName,
                class: h.className,
                text: h.innerText.trim().replace(/\\s+/g, ' '),
                styles: getStyles(h)
            }));

            const buttons = Array.from(document.querySelectorAll('a, button, .button, [class*="btn"]')).map(b => ({
                tag: b.tagName,
                class: b.className,
                text: b.innerText.trim().replace(/\\s+/g, ' '),
                href: b.getAttribute('href'),
                styles: getStyles(b)
            })).filter(b => b.text.length > 0);

            const sections = Array.from(document.querySelectorAll('section, header, footer, div[class*="section"], div[class*="hero"], div[class*="container"]')).map(s => ({
                tag: s.tagName,
                class: s.className,
                id: s.id,
                textSnippet: s.innerText.trim().substring(0, 150).replace(/\\s+/g, ' '),
                styles: getStyles(s)
            }));

            const images = Array.from(document.querySelectorAll('img')).map(img => ({
                src: img.src,
                alt: img.alt,
                width: img.width,
                height: img.height,
                naturalWidth: img.naturalWidth,
                naturalHeight: img.naturalHeight,
                class: img.className
            }));

            // Extract pages linked in header/footer
            const links = Array.from(document.querySelectorAll('a')).map(a => ({
                text: a.innerText.trim(),
                href: a.getAttribute('href')
            })).filter(l => l.href && !l.href.startsWith('javascript'));

            // Extract stylesheet links
            const stylesheets = Array.from(document.querySelectorAll('link[rel="stylesheet"]')).map(l => l.href);

            return {
                title: document.title,
                bodyStyles: getStyles(document.body),
                headings,
                buttons,
                sections,
                images,
                links,
                stylesheets
            };
        }""")

        with open("docs/screenshots/inspection-data.json", "w", encoding="utf-8") as f:
            json.dump(inspection, f, indent=2, ensure_ascii=False)

        print("Inspection and screenshots complete!")
        browser.close()

if __name__ == "__main__":
    run()
