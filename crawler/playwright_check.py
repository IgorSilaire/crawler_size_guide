from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from config.keywords import SIZE_GUIDE_KEYWORDS, GENDER_KEYWORDS

def analyze_product_playwright(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1366, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=30_000)

        html = page.content()
        context.close()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")

    h1 = soup.find("h1")
    product_name = h1.get_text(strip=True) if h1 else "Unknown"

    has_size_guide = any(k in html.lower() for k in SIZE_GUIDE_KEYWORDS)

    gender = "Unisex"
    for el in soup.find_all(["nav", "ul", "ol"]):
        text = el.get_text(" ").lower()
        for key, value in GENDER_KEYWORDS.items():
            if key in text:
                gender = value
                break
        if gender != "Unisex":
            break

    return {
        "product_name": product_name,
        "gender": gender,
        "product_url": url,
        "has_size_guide": has_size_guide
    }
