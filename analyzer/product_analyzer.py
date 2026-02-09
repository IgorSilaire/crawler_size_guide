from bs4 import BeautifulSoup
from analyzer.size_guide_detector import detect_size_guide

def analyze_product(html: str, url: str):
    soup = BeautifulSoup(html, "html.parser")

    size_guide_info = detect_size_guide(soup)

    product_name = soup.title.get_text(strip=True) if soup.title else ""
    gender = "Unknown"   
    product_type = "Unknown"
    
    return {
        "product_name": product_name,
        "gender": gender,
        "product_type": product_type,
        "product_url": url,
        "has_size_guide": 1 if size_guide_info["has_size_guide"] else 0
    }
