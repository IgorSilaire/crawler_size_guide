# analyzer\size_guide_detector.py

from utils.guide_size_selectors import SIZE_GUIDE_SELECTORS

def detect_size_guide(soup):
    
    results = []
    
    for el in soup.find_all(["a", "button", "span", "div"]):
        text_to_analyze = el.get_text(strip = True).lower()
        if any (keywords in text_to_analyze for keywords in SIZE_GUIDE_SELECTORS):
            href = el.get("href")
            results.append({
                "type": el.name,
                "text": text_to_analyze,
                "url": href
            })
            
    return {
        "The website has a guide size" : len(results) > 0,
        " way to the guide size" : len(results),
        "guides": results
    }    
        