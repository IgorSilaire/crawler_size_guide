from crawler.browser import Browser
from analyzer.cookies import accept_cookies

def crawl(url :str, headless: bool = True) -> str:
    with Browser(headless=headless) as page:
        page.goto(url, timeout = 60_000)
        accept_cookies(page)
        page.wait_for_load_state("networkidle")
        return page.content() 