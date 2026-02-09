from bs4 import BeautifulSoup
from analyzer.size_guide_detector import detect_size_guide

def analyze_product(html: str, url: str):
    soup = BeautifulSoup(html, "html.parser")

    size_guide_info = detect_size_guide(soup)

    return {
        "product_url": url,
        "has_size_guide": size_guide_info["has_size_guide"],
        "guide_count": size_guide_info["count"],
        "guide_types": list(
            {g["type"] for g in size_guide_info["guides"]}
        ),
        "guide_urls": list(
            {g["url"] for g in size_guide_info["guides"] if g["url"]}
        )
    }
