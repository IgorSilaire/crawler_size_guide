from cookies_data.dictWords import (
    ACCEPT_WORDS_FR,
    IFRAME_ACCEPT_SELECTORS,
    COMMON_ACCEPT_SELECTORS,
)

def accept_cookies(page, timeout: int = 3000):
    for selector in COMMON_ACCEPT_SELECTORS:
        try:
            page.click(selector, timeout = timeout)
            return True
        except:
            pass
        
    try:
        buttons = page.query_selector_all("buttons")
        for button in buttons:
            text = button.inner_text.lower()
            if any(word in text for word in ACCEPT_WORDS_FR):
                button.click()
                return True
    except:
        pass
    
    for frame in page.frames:
        for selector in IFRAME_ACCEPT_SELECTORS:
            try:
                frame.click(selector, timeout = timeout)
                return True
            except:
                pass
    
    return False

