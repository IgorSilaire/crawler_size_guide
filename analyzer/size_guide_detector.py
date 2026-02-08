# analyzer\size_guide_detector.py

from analyzer.guide_size_selectors import SIZE_GUIDE_SELECTORS

def detect_size_guide(soup):
    
    links = []
    
    for a in soup.find_all("a"):
        text_to_analyze = a.get_text(strip = True).lower()
        if any (keywords in text_to_analyze for keywords in SIZE_GUIDE_SELECTORS):
            href = a.get("href")
            if href:
                links.append(href)
            
    return {
        "The website has a guide size" : len(links) > 0,
        "URLs to the size guide(s)" : list(set(links)),
    }    
        