from crawler.browser import Browser
from analyzer.cookies import accept_cookies

def crawl(url: str, headless: bool = True) -> str:
    with Browser(headless=headless) as page:
        page.goto(url, timeout=60_000, wait_until="domcontentloaded")
        page.wait_for_timeout(2000)
        accept_cookies(page)
        page.wait_for_timeout(2000)
        return page.content()
