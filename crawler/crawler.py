from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, headless: bool = True):
        self.headless = headless
        def __enter__(self):
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=self.headless)
            
            self.context = self.browser.new_context(
                viewport={"width": 1366, "height": 900},
                ignore_https_errors=True,
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
                ),
            )
            self.page = self.context.new_page()
            return self.page
                



