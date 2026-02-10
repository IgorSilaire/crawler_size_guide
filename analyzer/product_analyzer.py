from bs4 import BeautifulSoup
from analyzer.size_guide_detector import detect_size_guide
from analyzer.product_attributes import (
    extract_from_breadcrumbs,
    extract_from_json_ld
)


def analyze_product(html: str, url: str):
    soup = BeautifulSoup(html, "html.parser")

    # 1. guide de taille (inchangé)
    size_guide_info = detect_size_guide(soup)

    # 2. breadcrumbs
    breadcrumbs = extract_from_breadcrumbs(soup)

    gender = "Unknown"
    product_type = "Unknown"

    for c in breadcrumbs:
        if c.lower() in ["homme", "femme", "men", "women"]:
            gender = c
    if breadcrumbs:
        product_type = breadcrumbs[-1]

    # 3. fallback JSON-LD (si breadcrumbs vides)
    if product_type == "Unknown":
        product_data = extract_from_json_ld(soup)
        product_type = product_data.get("category", "Unknown")

    return {
        "product_url": url,
        "gender": gender,
        "type": product_type,
        "has_size_guide": 1 if size_guide_info["has_size_guide"] else 0
    }
