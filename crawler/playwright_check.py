from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

KEYWORDS = [
    "guide des tailles",
    "guide de taille",
    "size guide",
    "size chart",
    "grille des pointures",
    "dimensions"
]

GENDER_KEYWORDS = {
    "homme": "Homme",
    "men": "Homme",
    "femme": "Femme",
    "women": "Femme",
}

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

    # 1️⃣ Nom du produit
    h1 = soup.find("h1")
    product_name = h1.get_text(strip=True) if h1 else "Unknown"

    # 2️⃣ Détection guide de taille (déjà OK)
    has_size_guide = any(k in html.lower() for k in KEYWORDS)

    # 3️⃣ Détection du genre (breadcrumbs + texte)
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
